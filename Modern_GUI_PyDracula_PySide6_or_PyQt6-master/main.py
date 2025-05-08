import sys
import os
import platform
import shutil
from datetime import datetime

# 1. 必须先导入 PySide6（GUI 模块优先）
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap, QImage

# 2. 再导入 OpenCV
import cv2

# 3. 其他路径、功能模块
sys.path.append(os.path.join(os.path.dirname(__file__), "code1_ALL", "Denoise", "MPMF-Net-master"))
sys.path.append(os.path.join(os.path.dirname(__file__), "YOLO"))

from utils import generate_result_image_path
from run_model import run_all_in_one_restore
from slide_compare_widget import SlideCompareWidget
from modules import *
from widgets import *
from generate_heatmap import generate_and_save_heatmaps
from QuantitativeAnalysisDialog import QuantitativeAnalysisDialog
from camera_handler import CameraHandler
from ultralytics import YOLO
from PySide6.QtWidgets import QApplication
from login_window import LoginDialog
from database import init_db
import sys
# 4. 设定 Qt 缩放环境变量
os.environ["QT_FONT_DPI"] = "160"

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
        title = "火 眼 金 睛"
        description = "面向智能驾驶的恶劣天气场景复原与检测系统"
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
        widgets.btn_image.clicked.connect(self.buttonClick)
        widgets.btn_video.clicked.connect(self.buttonClick)
        widgets.btn_realtime.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.btn_detect.clicked.connect(self.run_restore_if_needed)
        widgets.btn_heatmap.clicked.connect(self.show_heatmap_comparison)
        widgets.btn_psnr.clicked.connect(self.show_quantitative_analysis_dialog)

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
        self.camera_handler = CameraHandler(widgets.label_rt_video)
        widgets.btn_realtime_start.clicked.connect(self.toggle_camera)
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
            widgets.stackedWidget.setCurrentWidget(widgets.R_movie)  # 如果你有 video 页面
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        # #     # 需要删除
        #     left_video_path = "D:/MTM/wen/original/all.mp4"
        #     right_video_path = "D:/MTM/wen/restore/restored_fixed_duration.mp4"
        # if os.path.exists(left_video_path) and os.path.exists(right_video_path):
        #     widgets.video_compare_widget.load_videos(left_video_path, right_video_path)
        #     print("固定路径下视频加载成功，准备播放！")
        #     widgets.video_compare_widget.toggle_play()
        # else:
        #     print("找不到固定路径下的视频，请检查路径！")
        #
        # if btnName == "btn_psnr":
        #     print("打开定量分析弹窗")
        #     # 创建并显示定量分析弹窗
        #     psnr_dialog = QuantitativeAnalysisDialog(self)
        #     psnr_dialog.exec_()  # 显示弹窗并等待关闭

        if btnName == "btn_realtime":
            widgets.stackedWidget.setCurrentWidget(widgets.R_realtime_detect)
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

    # 打开图片
    def open_and_save_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择图像", "", "Image Files (*.png *.jpg *.jpeg)")
        if file_path:
            widgets.lineEdit_path.setText(file_path)  # 注意，只设置输入框，不保存！
            self.selected_input_path = file_path  # 保存一下选中的原图路径

    def run_restore_if_needed(self):
        mode = widgets.combo1.currentText()
        function = widgets.combo2.currentText()
        input_path = self.selected_input_path  # 用选中的原图路径

        if not input_path or not os.path.exists(input_path):
            print("路径不存在，请选择有效图像")
            return

        if mode == "ALL-IN-ONE" and function == "复原":
            # 开始保存原图副本
            save_path = self.generate_image_save_path()
            shutil.copy(input_path, save_path)
            print(f"原图已标准保存到: {save_path}")

            # 基于标准保存的图生成复原图
            output_path = generate_result_image_path()
            run_all_in_one_restore(save_path, output_path)

            # 更新滑动对比界面
            widgets.slide_compare.setImages(save_path, output_path)

            # 记录保存的标准图路径和复原图路径
            self.current_save_path = save_path
            self.current_output_path = output_path




        elif mode == "ALL-IN-ONE" and function == "复原+检测":
            def cv2_to_qpixmap(cv_img):
                if cv_img is None:
                    return QPixmap()
                rgb_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_img.shape
                return QPixmap(QImage(rgb_img.data, w, h, ch * w, QImage.Format_RGB888))

            if not hasattr(self, "current_output_path") or not os.path.exists(self.current_output_path):
                print("请先执行一次复原操作，再进行检测！")
                return

            original_img = cv2.imread(self.current_save_path)
            restored_img = cv2.imread(self.current_output_path)

            if original_img is None or restored_img is None:
                print("图像读取失败")
                return

            # 加载 YOLO 模型（原图使用 s，复原图使用 x）
            yolo_dir = os.path.join(os.path.dirname(__file__), "YOLO")
            model_o = YOLO(os.path.join(yolo_dir, "yolov12n.pt"))
            model_r = YOLO(os.path.join(yolo_dir, "yolov12x.pt"))

            # 检测原图
            results_o = model_o.predict(original_img, save=False)
            detected_o = results_o[0].plot()
            # 检测复原图
            results_r = model_r.predict(restored_img, save=False)
            detected_r = results_r[0].plot()
            # 展示检测图
            widgets.slide_compare.setImages(
                cv2_to_qpixmap(detected_o),
                cv2_to_qpixmap(detected_r)
            )
            print("原图与复原图检测完成，已显示对比图")

        else:
            print("未匹配到处理算法")

    # 展示热力图
    def show_heatmap_comparison(self):
        try:
            before_path = self.current_save_path
            after_path = self.current_output_path

            if not before_path or not after_path:
                print("没有检测结果，无法生成热力图")
                return
         # 打印标准保存的前后路径
            print(f"生成热力图的原图路径: {before_path}")
            print(f"生成热力图的复原图路径: {after_path}")
            base_dir = os.path.dirname(__file__)
            h_o_picture_dir = os.path.join(base_dir, "H_O_picture")
            h_r_picture_dir = os.path.join(base_dir, "H_R_picture")

            heatmap_before, heatmap_after = generate_and_save_heatmaps(
                before_path, after_path, h_o_picture_dir, h_r_picture_dir
            )

            widgets.slide_compare.setImages(heatmap_before, heatmap_after)
            print("成功生成并展示热力图")

        except Exception as e:
            print(f"生成热力图失败: {e}")
    # 定量分析
    def show_quantitative_analysis_dialog(self):
        print("打开定量分析弹窗")

        # 获取当前的复原前和复原后图像路径
        input_path = self.current_save_path
        output_path = self.current_output_path

        # 确保路径有效
        if not input_path or not os.path.exists(input_path):
            print("原始图像路径无效！")
            return
        if not output_path or not os.path.exists(output_path):
            print("复原图路径无效！")
            return

        # 设置路径并创建定量分析对话框
        psnr_dialog = QuantitativeAnalysisDialog(self)

        # 调用 set_image_paths 方法传递路径
        psnr_dialog.set_image_paths(input_path, output_path)  # 设置复原前和复原后图像路径

        # 打印路径以调试
        print(f"输入路径: {input_path}")
        print(f"输出路径: {output_path}")

        # 打开对话框
        psnr_dialog.exec()  # 弹出对话框并等待用户关闭

    def toggle_camera(self):
        self.camera_handler.toggle()
        if self.camera_handler.running:
            widgets.btn_realtime_start.setText("暂停")
            widgets.btn_realtime_start.setIcon(QIcon(":/icons/images/icons/cil-media-pause.png"))
            widgets.btn_realtime_start.setStyleSheet("""
                QPushButton {
                    background-color: #dc3545;  /* 红色 */
                    color: white;
                    border: none;
                    border-radius: 4px;
                    padding: 5px 10px;
                }
                QPushButton:hover {
                    background-color: #c82333;
                }
            """)
        else:
            widgets.btn_realtime_start.setText("开始")
            widgets.btn_realtime_start.setIcon(QIcon(":/icons/images/icons/cil-media-play.png"))
            widgets.btn_realtime_start.setStyleSheet("""
                QPushButton {
                    background-color: #28a745;  /* 绿色 */
                    color: white;
                    border: none;
                    border-radius: 4px;
                    padding: 5px 10px;
                }
                QPushButton:hover {
                    background-color: #218838;
                }
            """)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        # 更新缩放控件
        UIFunctions.resize_grips(self)

        # 自适应图片缩放
        if hasattr(widgets, 'label_before') and hasattr(widgets, 'label_after'):
            before_pixmap = widgets.label_before.pixmap()
            after_pixmap = widgets.label_after.pixmap()
            if before_pixmap:
                widgets.label_before.setPixmap(before_pixmap.scaled(widgets.label_before.size(), Qt.KeepAspectRatio))
            if after_pixmap:
                widgets.label_after.setPixmap(after_pixmap.scaled(widgets.label_after.size(), Qt.KeepAspectRatio))

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
    init_db()
    app = QApplication(sys.argv)
    login = LoginDialog()
    if login.exec() == QDialog.Accepted:
        app.setWindowIcon(QIcon("icon.ico"))
        window = MainWindow()  # 启动你的主界面
        window.show()
        sys.exit(app.exec())
    else:
        sys.exit()
