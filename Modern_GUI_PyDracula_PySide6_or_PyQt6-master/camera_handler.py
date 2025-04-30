# camera_handler.py
import cv2
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QPixmap

class CameraHandler:
    def __init__(self, label_display):
        self.label = label_display
        self.cap = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.running = False

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
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = frame.shape
                qimg = QImage(frame.data, w, h, ch * w, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(qimg)
                self.label.setPixmap(pixmap.scaled(self.label.size()))
