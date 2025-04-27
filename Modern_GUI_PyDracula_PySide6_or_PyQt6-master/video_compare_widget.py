from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPixmap, QImage
import cv2

class VideoCompareWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.left_video_path = None
        self.right_video_path = None

        self.left_cap = None
        self.right_cap = None

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frames)

        # 创建左右两个视频展示标签
        self.left_label = QLabel("原视频")
        self.right_label = QLabel("复原视频")
        self.left_label.setAlignment(Qt.AlignCenter)
        self.right_label.setAlignment(Qt.AlignCenter)

        self.left_label.setStyleSheet("background-color: black;")
        self.right_label.setStyleSheet("background-color: black;")

        # 播放暂停按钮
        self.play_button = QPushButton("播放")
        self.play_button.clicked.connect(self.toggle_play)

        # 布局
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.left_label)
        h_layout.addWidget(self.right_label)

        v_layout = QVBoxLayout(self)
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.play_button)

        self.is_playing = False

    def load_videos(self, left_path, right_path):
        self.left_video_path = left_path
        self.right_video_path = right_path

        if self.left_cap:
            self.left_cap.release()
        if self.right_cap:
            self.right_cap.release()

        self.left_cap = cv2.VideoCapture(left_path)
        self.right_cap = cv2.VideoCapture(right_path)

    def toggle_play(self):
        if not self.left_cap or not self.right_cap:
            print("请先加载视频")
            return

        if self.is_playing:
            self.timer.stop()
            self.play_button.setText("播放")
        else:
            self.timer.start(30)  # 每30ms刷新一帧（大约33fps）
            self.play_button.setText("暂停")

        self.is_playing = not self.is_playing

    def update_frames(self):
        if not self.left_cap.isOpened() or not self.right_cap.isOpened():
            return

        ret1, frame1 = self.left_cap.read()
        ret2, frame2 = self.right_cap.read()

        if ret1 and ret2:
            frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
            frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)

            h, w, ch = frame1.shape
            img1 = QImage(frame1.data, w, h, ch * w, QImage.Format_RGB888)
            img2 = QImage(frame2.data, w, h, ch * w, QImage.Format_RGB888)

            self.left_label.setPixmap(QPixmap.fromImage(img1).scaled(self.left_label.size(), Qt.KeepAspectRatio))
            self.right_label.setPixmap(QPixmap.fromImage(img2).scaled(self.right_label.size(), Qt.KeepAspectRatio))
        else:
            # 到达视频末尾，停止
            self.timer.stop()
            self.is_playing = False
            self.play_button.setText("播放")
