from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPixmap, QMouseEvent, QCursor
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QColor
from PySide6.QtGui import QPen, QColor
class SlideCompareWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.before_pixmap = None
        self.after_pixmap = None
        self.split_ratio = 0.5  # 默认中间分割
        self.dragging = False
        self.setMouseTracking(True)  # 启用鼠标移动追踪
        self.setMinimumHeight(400)

    def setImages(self, before_path, after_path):
        # 保存路径给热力图 做输入
        self.before_path = before_path
        self.after_path = after_path
        self.before_pixmap = QPixmap(before_path)
        self.after_pixmap = QPixmap(after_path)
        self.update()

    def paintEvent(self, event):
        if not self.before_pixmap or not self.after_pixmap:
            return

        painter = QPainter(self)
        w, h = self.width(), self.height()

        before_scaled = self.before_pixmap.scaled(w, h, Qt.KeepAspectRatioByExpanding)
        after_scaled = self.after_pixmap.scaled(w, h, Qt.KeepAspectRatioByExpanding)

        split_x = int(self.split_ratio * w)

        # 先画 after 图左侧
        painter.drawPixmap(QRect(0, 0, split_x, h), after_scaled, QRect(0, 0, split_x, h))
        # 再画 before 图右侧
        painter.drawPixmap(QRect(split_x, 0, w - split_x, h),
                           before_scaled, QRect(split_x, 0, w - split_x, h))

        # 绘制竖线（滑块）
        pen = QPen(QColor("#5a6ea8"))
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawLine(split_x, 0, split_x, h)
        # color: rgb(255, 121, 198); 粉色
        painter.drawLine(split_x, 0, split_x, h)

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
