from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPixmap, QMouseEvent, QCursor, QFont
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QColor, QPen

class SlideCompareWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.before_pixmap = None
        self.after_pixmap = None
        self.split_ratio = 0.5
        self.dragging = False
        self.setMouseTracking(True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAutoFillBackground(False)

    def setImages(self, before_path, after_path):
        self.before_path = before_path
        self.after_path = after_path
        self.before_pixmap = QPixmap(before_path)
        self.after_pixmap = QPixmap(after_path)
        self.updateSizeToImage()
        self.update()

    def updateSizeToImage(self):
        """根据图像宽高比和容器宽度，自适应设置高度，实现宽度最大化展示"""
        pix = self.before_pixmap or self.after_pixmap
        if not pix:
            return

        img_w, img_h = pix.width(), pix.height()
        container_w = self.parent().width() if self.parent() else self.width()
        target_h = int(container_w * img_h / img_w)

        self.setFixedHeight(target_h)
        self.setMinimumWidth(container_w)
        self.update()

        if self.parent() and self.parent().layout():
            self.parent().layout().activate()

    def paintEvent(self, event):
        if not self.before_pixmap or not self.after_pixmap:
            return

        painter = QPainter(self)
        w, h = self.width(), self.height()

        before_scaled = self.before_pixmap.scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        after_scaled = self.after_pixmap.scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        bx = (w - before_scaled.width()) // 2
        by = (h - before_scaled.height()) // 2
        ax = (w - after_scaled.width()) // 2
        ay = (h - after_scaled.height()) // 2

        split_x = int(self.split_ratio * w)

        # 绘制左侧 after
        painter.setClipRect(QRect(0, 0, split_x, h))
        painter.drawPixmap(ax, ay, after_scaled)
        painter.setClipping(False)

        # 绘制右侧 before
        painter.setClipRect(QRect(split_x, 0, w - split_x, h))
        painter.drawPixmap(bx, by, before_scaled)
        painter.setClipping(False)

        # 滑动分割线
        pen = QPen(QColor("#5a6ea8"))
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawLine(split_x, 0, split_x, h)

        # 半透明标签文字：复原前/后
        painter.setFont(QFont("Arial", 14, QFont.Bold))
        painter.setPen(QColor(255, 255, 255, 180))

        margin = 12
        text_after = "复原前"
        text_before = "复原后"
        text_width_after = painter.fontMetrics().horizontalAdvance(text_after)
        text_height = painter.fontMetrics().height()

        if self.split_ratio < 0.95:
            painter.drawText(w - text_width_after - margin, margin + text_height, text_after)

        if self.split_ratio > 0.05:
            painter.drawText(margin, margin + text_height, text_before)

    def mousePressEvent(self, event: QMouseEvent):
        if event.buttons() & Qt.LeftButton:
            self.dragging = True
            self.updateSplit(event.position().x())

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging:
            self.updateSplit(event.position().x())
        else:
            x = event.position().x()
            if abs(x - self.split_ratio * self.width()) < 6:
                self.setCursor(QCursor(Qt.SplitHCursor))
            else:
                self.setCursor(QCursor(Qt.ArrowCursor))

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.dragging = False

    def updateSplit(self, x):
        self.split_ratio = min(max(x / self.width(), 0.0), 1.0)
        self.update()