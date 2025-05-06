import cv2
import os
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QImage, QPixmap
from ultralytics import YOLO

class CameraHandler:
    def __init__(self, label_display):
        self.label = label_display
        self.cap = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.running = False
        # 加载 yolov12x.pt 模型（只加载一次）
        yolo_dir = os.path.join(os.path.dirname(__file__), "YOLO")
        self.model = YOLO(os.path.join(yolo_dir, "yolov12x.pt"))

    def start(self):
        if not self.cap:
            self.cap = cv2.VideoCapture(0)
        if self.cap.isOpened():
            self.timer.start(66)  # ~15fps
            self.running = True

    def stop(self):
        self.timer.stop()
        if self.cap:
            self.cap.release()
            self.cap = None
        # self.label.clear()
        self.running = False

    def toggle(self):
        if self.running:
            self.stop()
        else:
            self.start()

    def update_frame(self):
        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                # 做检测并绘制框（保持原图分辨率）
                results = self.model.predict(frame, save=False, verbose=False)
                frame = results[0].plot()  # 这一步会直接在原frame上画框

                # 保持原来的展示逻辑（和你最早的一样）
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = frame.shape
                qimg = QImage(frame.data, w, h, ch * w, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(qimg)
                self.label.setPixmap(pixmap.scaled(self.label.size()))

