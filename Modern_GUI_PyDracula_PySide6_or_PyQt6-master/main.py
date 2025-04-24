
import sys
import os
import platform
import shutil
from datetime import datetime
from PySide6.QtWidgets import QFileDialog
sys.path.append(os.path.join(os.path.dirname(__file__), "code1_ALL", "Denoise", "MPMF-Net-master"))
from utils import generate_result_image_path
from run_model import run_all_in_one_restore
from PySide6.QtGui import QPixmap

from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "PyDracula - Modern GUI"
        description = "PyDracula APP - Theme with colors based on Dracula for Python."
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.btn_image.clicked.connect(self.buttonClick)
        widgets.btn_video.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_detect.clicked.connect(self.run_restore_if_needed)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = True
        themeFile = "themes/py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        widgets.btn_browse.clicked.connect(self.open_and_save_image)
    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_save":
            print("Save BTN clicked!")
        print(f'Button "{btnName}" pressed!')

        if btnName == "btn_image":
            widgets.stackedWidget.setCurrentWidget(widgets.R_image)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_video":
            print("打开视频页面")
            # widgets.stackedWidget.setCurrentWidget(widgets.video_page)  # 如果你有 video 页面
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

    # 生成保存路径：带编号 + 日期 + 时间
    def generate_image_save_path(self):
        base_dir = os.path.join(os.path.dirname(__file__), "O_picture")
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

        now = datetime.now()
        date_str = f"{now.month}_{now.day}"
        time_str = now.strftime("%H%M")

        existing_numbers = []
        for fname in os.listdir(base_dir):
            if fname.endswith((".jpg", ".png", ".jpeg")) and fname.count("_") >= 2:
                num = fname.split("_")[0]
                if num.isdigit():
                    existing_numbers.append(int(num))
        next_index = max(existing_numbers + [0]) + 1
        filename = f"{next_index}_{date_str}_{time_str}.png"
        return os.path.join(base_dir, filename)

    # 打开图片并保存到指定路径
    def open_and_save_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择图像", "", "Image Files (*.png *.jpg *.jpeg)")
        if file_path:
            save_path = self.generate_image_save_path()
            shutil.copy(file_path, save_path)
            print(f"图像已保存到: {save_path}")
            widgets.lineEdit_path.setText(file_path)

    # 自动检测并执行 ALL-IN-ONE 复原操作
    def run_restore_if_needed(self):
        mode = widgets.combo1.currentText()
        function = widgets.combo2.currentText()
        input_path = widgets.lineEdit_path.text()

        if not os.path.exists(input_path):
            print("路径不存在，请选择有效图像")
            return

        # 显示恢复前图像（原图）
        pixmap_before = QPixmap(input_path)
        widgets.label_before.setPixmap(pixmap_before.scaled(
            widgets.label_before.size(), Qt.KeepAspectRatio))

        # 处理 ALL-IN-ONE + 复原
        if mode == "ALL-IN-ONE" and function == "复原":
            output_path = generate_result_image_path()
            run_all_in_one_restore(input_path, output_path)

            # 显示恢复后图像
            pixmap_after = QPixmap(output_path)
            widgets.label_after.setPixmap(pixmap_after.scaled(
                widgets.label_after.size(), Qt.KeepAspectRatio))

        # 处理 ALL-IN-ONE + 复原+检测
        elif mode == "ALL-IN-ONE" and function == "复原+检测":
            # TODO: 这里未来可接入检测算法逻辑
            widgets.label_after.setText("检测模块尚未集成")

        else:
            print("未匹配到处理算法")
    # 让图片适应尺寸
    def resizeEvent(self, event):
        super().resizeEvent(event)
        # 自适应缩放
        if hasattr(widgets, 'label_before') and hasattr(widgets, 'label_after'):
            before_pixmap = widgets.label_before.pixmap()
            after_pixmap = widgets.label_after.pixmap()
            if before_pixmap:
                widgets.label_before.setPixmap(before_pixmap.scaled(widgets.label_before.size(), Qt.KeepAspectRatio))
            if after_pixmap:
                widgets.label_after.setPixmap(after_pixmap.scaled(widgets.label_after.size(), Qt.KeepAspectRatio))

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
