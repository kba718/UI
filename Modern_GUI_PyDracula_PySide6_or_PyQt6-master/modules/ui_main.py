

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from slide_compare_widget import SlideCompareWidget
from . resources_rc import *
from video_compare_widget import VideoCompareWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        # 创建一个垂直布局，用于整个窗口的外层布局
        self.appMargins = QVBoxLayout(self.styleSheet)  # 使用QVBoxLayout布局
        self.appMargins.setSpacing(0)  # 设置布局内组件之间的间距为0
        self.appMargins.setObjectName(u"appMargins")  # 设置布局对象的名称
        self.appMargins.setContentsMargins(10, 10, 10, 10)  # 设置布局的外边距为10

        # 创建一个背景容器，用于放置整个应用的布局
        self.bgApp = QFrame(self.styleSheet)  # 使用QFrame作为背景容器
        self.bgApp.setObjectName(u"bgApp")  # 设置背景容器对象的名称
        self.bgApp.setStyleSheet(u"")  # 设置背景容器的样式表为空
        self.bgApp.setFrameShape(QFrame.NoFrame)  # 设置背景容器的边框样式为无边框
        self.bgApp.setFrameShadow(QFrame.Raised)  # 设置背景容器的阴影样式为凸起

        # 创建一个水平布局，用于背景容器的内部布局
        self.appLayout = QHBoxLayout(self.bgApp)  # 使用QHBoxLayout布局
        self.appLayout.setSpacing(0)  #  左右两部分距离
        self.appLayout.setObjectName(u"appLayout")  # 设置布局对象的名称
        self.appLayout.setContentsMargins(0, 0, 0, 0)  # 设置布局的外边距为0

        # 创建左侧菜单栏的背景容器
        self.leftMenuBg = QFrame(self.bgApp)  # 使用QFrame作为左侧菜单栏的背景
        self.leftMenuBg.setObjectName(u"leftMenuBg")  # 设置左侧菜单栏背景对象的名称
        self.leftMenuBg.setMinimumSize(QSize(60, 0))  # 设置左侧菜单栏的最小宽度为60
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))  # 设置左侧菜单栏的最大宽度为60
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)  # 设置左侧菜单栏背景的边框样式为无边框
        self.leftMenuBg.setFrameShadow(QFrame.Raised)  # 设置左侧菜单栏背景的阴影样式为凸起

        # 创建一个垂直布局，用于左侧菜单栏的内部布局
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)  # 使用QVBoxLayout布局
        self.verticalLayout_3.setSpacing(0)  # 设置布局内组件之间的间距为0
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")  # 设置布局对象的名称
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)  # 设置布局的外边距为0

        # 创建左侧菜单栏顶部的Logo区域
        self.topLogoInfo = QFrame(self.leftMenuBg)  # 使用QFrame作为Logo区域
        self.topLogoInfo.setObjectName(u"topLogoInfo")  # 设置Logo区域对象的名称
        self.topLogoInfo.setMinimumSize(QSize(0, 50))  # 设置Logo区域的最小高度为50
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))  # 设置Logo区域的最大高度为50
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)  # 设置Logo区域的边框样式为无边框
        self.topLogoInfo.setFrameShadow(QFrame.Raised)  # 设置Logo区域的阴影样式为凸起

        # 创建Logo区域内的Logo图标
        self.topLogo = QFrame(self.topLogoInfo)  # 使用QFrame作为Logo图标
        self.topLogo.setObjectName(u"topLogo")  # 设置Logo图标对象的名称
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))  # 设置Logo图标的位置和大小
        self.topLogo.setMinimumSize(QSize(42, 42))  # 设置Logo图标的最小大小为42x42
        self.topLogo.setMaximumSize(QSize(42, 42))  # 设置Logo图标的最大大小为42x42
        self.topLogo.setFrameShape(QFrame.NoFrame)  # 设置Logo图标的边框样式为无边框
        self.topLogo.setFrameShadow(QFrame.Raised)  # 设置Logo图标的阴影样式为凸起

        # 创建Logo区域内的应用标题
        self.titleLeftApp = QLabel(self.topLogoInfo)  # 使用QLabel作为应用标题
        self.titleLeftApp.setObjectName(u"titleLeftApp")  # 设置应用标题对象的名称
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))  # 设置应用标题的位置和大小
        font1 = QFont()  # 创建字体对象
        font1.setFamily(u"Segoe UI Semibold")  # 设置字体为Segoe UI Semibold
        font1.setPointSize(14)
        font1.setBold(True)  # 设置字体非加粗
        font1.setItalic(False)  # 设置字体非斜体
        self.titleLeftApp.setFont(font1)  # 应用字体设置
        self.titleLeftApp.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)  # 设置文本对齐方式为左对齐、顶部对齐

        # 创建Logo区域内的应用描述
        self.titleLeftDescription = QLabel(self.topLogoInfo)  # 使用QLabel作为应用描述
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")  # 设置应用描述对象的名称
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))  # 设置应用描述的位置和大小
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))  # 设置应用描述的最大高度为16
        font2 = QFont()  # 创建字体对象
        font2.setFamily(u"Segoe UI")  # 设置字体为Segoe UI
        font2.setPointSize(8)
        font2.setBold(True)  # 设置字体非加粗
        font2.setItalic(False)  # 设置字体非斜体
        self.titleLeftDescription.setFont(font2)  # 应用字体设置
        self.titleLeftDescription.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)  # 设置文本对齐方式为左对齐、顶部对齐

        # 将Logo区域添加到左侧菜单栏的垂直布局中
        self.verticalLayout_3.addWidget(self.topLogoInfo)

        # 创建左侧菜单栏的主体部分
        self.leftMenuFrame = QFrame(self.leftMenuBg)  # 使用QFrame作为左侧菜单栏的主体
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")  # 设置左侧菜单栏主体对象的名称
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)  # 设置左侧菜单栏主体的边框样式为无边框
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)  # 设置左侧菜单栏主体的阴影样式为凸起

        # 创建一个垂直布局，用于左侧菜单栏主体的内部布局（展开按钮）
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)  # 使用QVBoxLayout布局
        self.verticalMenuLayout.setSpacing(0)  # 设置布局内组件之间的间距为0
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")  # 设置布局对象的名称
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)  # 设置布局的外边距为0

        # 创建一个容器，用于放置可折叠菜单按钮
        self.toggleBox = QFrame(self.leftMenuFrame)  # 使用QFrame作为容器
        self.toggleBox.setObjectName(u"toggleBox")  # 设置容器对象的名称
        self.toggleBox.setMaximumSize(QSize(16777215, 45))  # 设置容器的最大高度为45
        self.toggleBox.setFrameShape(QFrame.NoFrame)  # 设置容器的边框样式为无边框
        self.toggleBox.setFrameShadow(QFrame.Raised)  # 设置容器的阴影样式为凸起

        # 创建一个垂直布局，用于容器的内部布局
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)  # 使用QVBoxLayout布局
        self.verticalLayout_4.setSpacing(0)  # 设置布局内组件之间的间距为0
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")  # 设置布局对象的名称
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)  # 设置布局的外边距为0

        # 创建可折叠菜单按钮
        self.toggleButton = QPushButton(self.toggleBox)  # 使用QPushButton作为按钮
        self.toggleButton.setObjectName(u"toggleButton")  # 设置按钮对象的名称
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # 创建尺寸策略
        sizePolicy.setHorizontalStretch(0)  # 设置水平方向的伸缩因子为0
        sizePolicy.setVerticalStretch(0)  # 设置垂直方向的伸缩因子为0
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())# 设置高度是否随宽度变化

        # 设置可折叠菜单按钮的尺寸策略
        self.toggleButton.setSizePolicy(sizePolicy)  # 应用之前定义的尺寸策略
        self.toggleButton.setMinimumSize(QSize(0, 45))  # 设置按钮的最小高度为45
        self.toggleButton.setFont(font)  # 设置按钮的字体
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))  # 设置鼠标悬停时的光标样式为手形
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)  # 设置布局方向为从左到右
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")  # 设置按钮的背景图像
        self.verticalLayout_4.addWidget(self.toggleButton)# 将可折叠菜单按钮添加到其父布局中

        # 将可折叠菜单按钮的容器（toggleBox）添加到左侧菜单栏的主体布局中
        self.verticalMenuLayout.addWidget(self.toggleBox)

        # 创建一个容器，用于放置左侧菜单栏按钮
        self.topMenu = QFrame(self.leftMenuFrame)  # 使用QFrame作为容器
        self.topMenu.setObjectName(u"topMenu")  # 设置容器对象的名称
        self.topMenu.setFrameShape(QFrame.NoFrame)  # 设置容器的边框样式为无边框
        self.topMenu.setFrameShadow(QFrame.Raised)  # 设置容器的阴影样式为凸起

        # 创建一个垂直布局，用于左侧菜单按钮的布局
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)  # 使用QVBoxLayout布局
        self.verticalLayout_8.setSpacing(0)  # 设置布局内组件之间的间距为0
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")  # 设置布局对象的名称
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)  # 设置布局的外边距为0

        # 创建“主页”按钮
        self.btn_home = QPushButton(self.topMenu)  # 使用QPushButton作为按钮
        self.btn_home.setObjectName(u"btn_home")  # 设置按钮对象的名称
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())  # 设置高度是否随宽度变化
        self.btn_home.setSizePolicy(sizePolicy)  # 应用尺寸策略
        self.btn_home.setMinimumSize(QSize(0, 45))  # 设置按钮的最小高度为45
        self.btn_home.setFont(font)  # 设置按钮的字体
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))  # 设置鼠标悬停时的光标样式为手形
        self.btn_home.setLayoutDirection(Qt.LeftToRight)  # 设置布局方向为从左到右
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")  # 设置按钮的背景图像
        # 将“主页”按钮添加到顶部菜单的布局中
        self.verticalLayout_8.addWidget(self.btn_home)

        # 新增 图片按钮
        self.btn_image = QPushButton(self.topMenu)
        self.btn_image.setObjectName(u"btn_image")
        self.btn_image.setMinimumSize(QSize(0, 45))
        self.btn_image.setFont(font)
        self.btn_image.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_image.setLayoutDirection(Qt.LeftToRight)
        self.btn_image.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-image1.png);")
        self.verticalLayout_8.addWidget(self.btn_image)

        # 新增 视频按钮
        self.btn_video = QPushButton(self.topMenu)
        self.btn_video.setObjectName(u"btn_video")
        self.btn_video.setMinimumSize(QSize(0, 45))
        self.btn_video.setFont(font)
        self.btn_video.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_video.setLayoutDirection(Qt.LeftToRight)
        self.btn_video.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-movie.png);")
        self.verticalLayout_8.addWidget(self.btn_video)

        self.btn_realtime = QPushButton(self.topMenu)
        self.btn_realtime.setObjectName(u"btn_realtime")
        self.btn_realtime.setMinimumSize(QSize(0, 45))
        self.btn_realtime.setFont(font)
        self.btn_realtime.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_realtime.setLayoutDirection(Qt.LeftToRight)
        self.btn_realtime.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-camera.png);")
        self.verticalLayout_8.addWidget(self.btn_realtime)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png);")

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-history.png)")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.verticalLayout_8.addWidget(self.btn_widgets)





        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)

        # 将顶部菜单容器（topMenu）添加到左侧菜单栏的主体布局中，并设置对齐方式为顶部对齐
        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        # 创建底部菜单容器
        self.bottomMenu = QFrame(self.leftMenuFrame)  # 使用QFrame作为底部菜单的容器
        self.bottomMenu.setObjectName(u"bottomMenu")  # 设置容器对象的名称
        self.bottomMenu.setFrameShape(QFrame.NoFrame)  # 设置容器的边框样式为无边框
        self.bottomMenu.setFrameShadow(QFrame.Raised)  # 设置容器的阴影样式为凸起

        # 创建底部菜单左下角的垂直布局
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)  # 使用QVBoxLayout布局
        self.verticalLayout_9.setSpacing(0)  # 设置布局内组件之间的间距为0
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")  # 设置布局对象的名称
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)  # 设置布局的外边距为0

        # 创建底部菜单中的“设置”按钮
        self.toggleLeftBox = QPushButton(self.bottomMenu)  # 使用QPushButton作为按钮
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")  # 设置按钮对象的名称
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())  # 设置高度是否随宽度变化
        self.toggleLeftBox.setSizePolicy(sizePolicy)  # 应用尺寸策略
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))  # 设置按钮的最小高度为45
        self.toggleLeftBox.setFont(font)  # 设置按钮的字体
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))  # 设置鼠标悬停时的光标样式为手形
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)  # 设置布局方向为从左到右
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")  # 设置按钮的背景图像
        # 将“设置”按钮添加到底部菜单的布局中
        self.verticalLayout_9.addWidget(self.toggleLeftBox)

        # 将底部菜单容器（bottomMenu）添加到左侧菜单栏的主体布局中，并设置对齐方式为底部对齐
        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)
        # 将左侧菜单栏的主体容器（leftMenuFrame）添加到左侧菜单栏的背景容器的布局中
        self.verticalLayout_3.addWidget(self.leftMenuFrame)
        # 将左侧菜单栏的背景容器（leftMenuBg）添加到应用的主布局中
        self.appLayout.addWidget(self.leftMenuBg)

        # 创建一个额外的左侧扩展区域 左侧设置按钮
        self.extraLeftBox = QFrame(self.bgApp)  # 使用QFrame作为额外左侧区域的容器
        self.extraLeftBox.setObjectName(u"extraLeftBox")  # 设置容器对象的名称
        self.extraLeftBox.setMinimumSize(QSize(0, 0))  # 设置最小尺寸为0
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))  # 设置最大宽度为0（默认隐藏）
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)  # 设置容器的边框样式为无边框
        self.extraLeftBox.setFrameShadow(QFrame.Raised)  # 设置容器的阴影样式为凸起

        # 创建额外左侧区域的垂直布局 左侧设置按钮的垂直布局
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)  # 使用QVBoxLayout布局
        self.extraColumLayout.setSpacing(0)  # 设置布局内组件之间的间距为0
        self.extraColumLayout.setObjectName(u"extraColumLayout")  # 设置布局对象的名称
        self.extraColumLayout.setContentsMargins(10, 0, 0, 0)  # 设置布局的外边距为0

        # 创建额外左侧区域的顶部背景容器
        self.extraTopBg = QFrame(self.extraLeftBox)  # 使用QFrame作为顶部背景容器
        self.extraTopBg.setObjectName(u"extraTopBg")  # 设置容器对象的名称
        self.extraTopBg.setMinimumSize(QSize(0, 50))  # 设置最小高度为50
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))  # 设置最大高度为50
        self.extraTopBg.setFrameShape(QFrame.NoFrame)  # 设置容器的边框样式为无边框
        self.extraTopBg.setFrameShadow(QFrame.Raised)  # 设置容器的阴影样式为凸起

        # 创建额外左侧区域顶部背景容器的垂直布局
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)  # 使用QVBoxLayout布局
        self.verticalLayout_5.setSpacing(0)  # 设置布局内组件之间的间距为0
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")  # 设置布局对象的名称
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)  # 设置布局的外边距为0

        # 创建额外左侧区域顶部的网格布局
        self.extraTopLayout = QGridLayout()  # 使用QGridLayout布局
        self.extraTopLayout.setObjectName(u"extraTopLayout")  # 设置布局对象的名称
        self.extraTopLayout.setHorizontalSpacing(10)  # 设置水平间距为10
        self.extraTopLayout.setVerticalSpacing(0)  # 设置垂直间距为0
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)  # 设置布局的外边距

        # 创建额外左侧区域顶部的图标
        self.extraIcon = QFrame(self.extraTopBg)  # 使用QFrame作为图标容器
        self.extraIcon.setObjectName(u"extraIcon")  # 设置图标容器对象的名称
        self.extraIcon.setMinimumSize(QSize(20, 0))  # 设置最小宽度为20
        self.extraIcon.setMaximumSize(QSize(20, 20))  # 设置最大大小为20x20
        self.extraIcon.setFrameShape(QFrame.NoFrame)  # 设置容器的边框样式为无边框
        self.extraIcon.setFrameShadow(QFrame.Raised)  # 设置容器的阴影样式为凸起

        # 将图标添加到额外左侧区域顶部的网格布局中
        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        # 创建额外左侧区域顶部的标签
        self.extraLabel = QLabel(self.extraTopBg)  # 使用QLabel作为标签
        self.extraLabel.setObjectName(u"extraLabel")  # 设置标签对象的名称
        self.extraLabel.setMinimumSize(QSize(150, 0))  # 设置最小宽度为150

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)
        # 创建额外左侧区域顶部的关闭按钮
        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)
        # 创建额外左侧区域的内容部分
        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        # 创建额外左侧区域内容部分的垂直布局
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        # 创建额外左侧区域的顶部菜单部分
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        # 创建额外左侧区域顶部菜单的垂直布局
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        # # 创建“分享”按钮
        # self.btn_share = QPushButton(self.extraTopMenu)
        # self.btn_share.setObjectName(u"btn_share")
        # sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        # self.btn_share.setSizePolicy(sizePolicy)
        # self.btn_share.setMinimumSize(QSize(0, 45))
        # self.btn_share.setFont(font)
        # self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        # self.btn_share.setLayoutDirection(Qt.LeftToRight)
        # self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")
        #
        # self.verticalLayout_11.addWidget(self.btn_share)
        #
        # # 创建“调整”按钮
        # self.btn_adjustments = QPushButton(self.extraTopMenu)
        # self.btn_adjustments.setObjectName(u"btn_adjustments")
        # sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        # self.btn_adjustments.setSizePolicy(sizePolicy)
        # self.btn_adjustments.setMinimumSize(QSize(0, 45))
        # self.btn_adjustments.setFont(font)
        # self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        # self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        # self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")
        #
        # self.verticalLayout_11.addWidget(self.btn_adjustments)
        #
        # # 创建“更多”按钮
        # self.btn_more = QPushButton(self.extraTopMenu)
        # self.btn_more.setObjectName(u"btn_more")
        # sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        # self.btn_more.setSizePolicy(sizePolicy)
        # self.btn_more.setMinimumSize(QSize(0, 45))
        # self.btn_more.setFont(font)
        # self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        # self.btn_more.setLayoutDirection(Qt.LeftToRight)
        # self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")
        #
        # self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)
        # 创建额外左侧区域的中心部分
        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        # 创建一个文本编辑框
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)
        # 将文本编辑框添加到中心部分的布局中
        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)
        # 创建应用的主要内容区域
        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        # 创建主要内容区域的垂直布局
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        # 创建主要内容区域的顶部背景容器
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        # 创建主要内容区域顶部背景容器的水平布局
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        # 创建左侧盒子，用于放置标题信息
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        # 创建左侧盒子的水平布局
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        # 创建标题信息标签
        self.titleRightInfo = QLabel(self.leftBox)  # 使用QLabel作为标题信息标签
        self.titleRightInfo.setObjectName(u"titleRightInfo")  # 设置标签对象的名称
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)  # 创建尺寸策略
        sizePolicy2.setHorizontalStretch(0)  # 设置水平方向的伸缩因子为0
        sizePolicy2.setVerticalStretch(0)  # 设置垂直方向的伸缩因子为0
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())  # 设置高度是否随宽度变化
        self.titleRightInfo.setSizePolicy(sizePolicy2)  # 应用尺寸策略
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))  # 设置最大高度为45
        self.titleRightInfo.setFont(font)  # 设置标签的字体
        self.titleRightInfo.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)  # 设置文本对齐方式为左对齐、垂直居中
        # 将标题信息标签添加到左侧盒子的水平布局中
        self.horizontalLayout_3.addWidget(self.titleRightInfo)
        # 将左侧盒子添加到主要内容区域顶部背景容器的水平布局中
        self.horizontalLayout.addWidget(self.leftBox)
        # 创建右侧按钮容器
        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        # 创建右侧按钮容器的水平布局
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        # 创建设置按钮（右上角）
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))
        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        # 创建最小化按钮
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))
        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)
        # 创建最大化/还原按钮
        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))
        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        # 创建关闭按钮
        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)

        # 设置右上角按钮右对齐
        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        # 右下角栏
        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        # 创建主要内容区域的中心内容部分
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        # 创建中心内容部分的水平布局
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        # 创建页面容器
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        # 创建页面容器的垂直布局
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)

        # 创建堆叠窗口（用于切换不同的页面）
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")

        # 创建首页
        self.home = QWidget()  # 使用QWidget作为首页
        self.home.setObjectName(u"home")  # 设置首页对象的名称
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
                                "background-position: center;\n"
                                "background-repeat: no-repeat;")  # 设置首页的背景图像
        self.stackedWidget.addWidget(self.home)  # 将首页添加到堆叠窗口中

        # 创建小部件页面
        self.widgets = QWidget()  # 使用QWidget作为小部件页面
        self.widgets.setObjectName(u"widgets")  # 设置小部件页面对象的名称
        self.widgets.setStyleSheet(u"b")  # 设置小部件页面的样式表（可能有误，应检查是否为有效样式）
        # 创建小部件页面的垂直布局
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)

        # 创建第一行小部件
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)

        # 创建第一行小部件的垂直布局
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        # 创建第一行小部件的内容容器
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        # 创建第一行小部件内容容器的垂直布局
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        # 创建路径输入框
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        # 创建“选择文件夹”按钮
        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        # 创建一个标签（用于显示版本信息等提示）
        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)

        # 将整个网格布局添加到水平布局中
        self.horizontalLayout_9.addLayout(self.gridLayout)

        # 将内容区域容器加入到上级布局中
        self.verticalLayout_17.addWidget(self.frame_content_wid_1)

        # 将整体内容（标题 + 输入）加入到 row_1 的布局中
        self.verticalLayout_16.addWidget(self.frame_div_content_1)
        self.verticalLayout.addWidget(self.row_1)

        # 创建第二行组件容器 row_2（用于展示各种控件）
        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon5)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.row_2)

        # 创建第三行 row_3，用于显示 QTableWidget 表格
        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)

        # 创建 QTableWidget 表格控件
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        # 设置行数为16（如果当前行数不足）
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label = QLabel(self.new_page)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label)

        self.stackedWidget.addWidget(self.new_page)

        # 创建图像复原页面 R_image，采用 row_1 / row_2 / row_3 风格构建，支持动态对比恢复效果
        self.R_image = QWidget()
        self.R_image.setObjectName("R_image") # 设置背景为白色
        self.R_image.setStyleSheet("background-color: white;")
        self.verticalLayout_R_image = QVBoxLayout(self.R_image)
        self.verticalLayout_R_image.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_R_image.setSpacing(0) # 设置各部分之间的间距为 0 像素

        # ========================= row_1 文件选择 =========================
        self.row_1 = QFrame(self.R_image)
        self.row_1.setMinimumHeight(100)
        self.row_1.setMaximumHeight(100)
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)

        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        # 输入路径和按钮
        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        # 路径输入框
        self.lineEdit_path = QLineEdit(self.frame_content_wid_1)
        self.lineEdit_path.setPlaceholderText("请选择图像文件路径...")
        self.lineEdit_path.setMinimumSize(QSize(0, 30))
        self.lineEdit_path.setStyleSheet(
            "background-color: #5a6ea8; color: white; border-radius: 5px; padding: 6px; border: none;")
        self.gridLayout.addWidget(self.lineEdit_path, 0, 0, 1, 1)
        # 选择文件按钮
        self.btn_browse = QPushButton("选择图片", self.frame_content_wid_1)
        self.btn_browse.setIcon(QIcon(":/icons/images/icons/cil-folder-open.png"))
        self.btn_browse.setMinimumSize(QSize(150, 30))
        self.btn_browse.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_browse.setStyleSheet(
            "background-color: #5a6ea8; color: white; border-radius: 5px; padding: 6px 12px; border: none;")
        self.gridLayout.addWidget(self.btn_browse, 0, 1, 1, 1)
        # 说明文字
        self.label_description = QLabel("选择算法  →  开始检测  →  执行操作"
                                     "      （左侧：复原后图像 右侧：复原前图像）", self.frame_content_wid_1)

        self.label_description.setStyleSheet("color: #6a7ba8; font-size: 9pt;")
        self.gridLayout.addWidget(self.label_description, 1, 0, 1, 2)

        self.horizontalLayout_9.addLayout(self.gridLayout)
        self.verticalLayout_17.addWidget(self.frame_content_wid_1)
        self.verticalLayout_16.addWidget(self.frame_div_content_1)
        self.verticalLayout_R_image.addWidget(self.row_1)

        # ========================= row_2 控制栏 =========================
        self.row_2 = QFrame(self.R_image)
        self.row_2.setMinimumHeight(30)
        self.row_2.setMaximumHeight(40)
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10 = QHBoxLayout(self.row_2)
        self.horizontalLayout_10.setContentsMargins(0, 0, 10, 0)  # 右侧留 10 像素空隙更贴边
        self.horizontalLayout_10.setSpacing(10)

        # 模式选择下拉框
        self.combo1 = QComboBox()
        self.combo1.addItems(["去雨", "去雾", "低光增强", "ALL-IN-ONE"])
        self.combo1.setFixedSize(150, 30)
        self.combo1.setStyleSheet("""
            QComboBox {
                background-color: #ffffff;
                color: black;
                border: 2px solid #5a6ea8;
                border-radius: 5px;
                padding: 5px;
            }
        """)

        # 功能选择下拉框
        self.combo2 = QComboBox()
        self.combo2.addItems(["复原", "复原+检测"])
        self.combo2.setFixedSize(150, 30)
        self.combo2.setStyleSheet("""
            QComboBox {
                background-color: #ffffff;
                color: black;
                border: 2px solid #5a6ea8;
                border-radius: 5px;
                padding: 5px;
            }
        """)



        # 检测按钮
        self.btn_detect = QPushButton("开始")
        self.btn_detect.setIcon(QIcon(":/icons/images/icons/cil-media-play.png"))
        self.btn_detect.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_detect.setFixedSize(110, 30)
        self.btn_detect.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)

        # 热力图按钮
        self.btn_heatmap = QPushButton("热力图")
        self.btn_heatmap.setIcon(QIcon(":/icons/images/icons/cil-fire.png"))
        self.btn_heatmap.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_heatmap.setFixedSize(110, 30)
        self.btn_heatmap.setStyleSheet("""
                   QPushButton {
                       background-color: #ff5722;
                       color: white;
                       border: none;
                       border-radius: 4px;
                       padding: 5px 10px;
                   }
                   QPushButton:hover {
                       background-color: #e64a19;
                   }
               """)

        # PSNR分析按钮
        self.btn_psnr = QPushButton("定量分析")
        self.btn_psnr.setIcon(QIcon(":/icons/images/icons/cil-clipboard.png"))
        self.btn_psnr.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_psnr.setFixedSize(110, 30)
        self.btn_psnr.setStyleSheet("""
            QPushButton {
                background-color: #03a9f4;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #0288d1;
            }
        """)

        # 添加控件到布局
        self.horizontalLayout_10.addWidget(self.combo1)
        self.horizontalLayout_10.addWidget(self.combo2)
        self.horizontalLayout_10.addStretch()  # 弹性空间：按钮靠右
        self.horizontalLayout_10.addWidget(self.btn_detect)
        self.horizontalLayout_10.addWidget(self.btn_heatmap)
        self.horizontalLayout_10.addWidget(self.btn_psnr)

        # 添加 row_2 到页面主布局
        self.verticalLayout_R_image.addWidget(self.row_2)

        # ========================= row_3 图像对比区域 =========================
        self.row_3 = QFrame(self.R_image)
        self.row_3.setMinimumHeight(400)
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_30 = QVBoxLayout(self.row_3)
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30.setSpacing(0)

        # 创建滑动对比组件
        self.slide_compare = SlideCompareWidget(self.row_3)  # 这里注意名字，最好叫 slide_compare（保持和 main.py 一致）
        self.verticalLayout_30.addWidget(self.slide_compare)

        # 把 row_3 加到页面
        self.verticalLayout_R_image.addWidget(self.row_3)
        # 把页面加到 stackedWidget
        self.stackedWidget.addWidget(self.R_image)

        # 创建实时检测页面 R_realtime_detect
        self.R_realtime_detect = QWidget()
        self.R_realtime_detect.setObjectName("R_realtime_detect")
        self.R_realtime_detect.setStyleSheet("background-color: white;")
        self.verticalLayout_R_realtime = QVBoxLayout(self.R_realtime_detect)
        self.verticalLayout_R_realtime.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_R_realtime.setSpacing(0)

        # ========================= row_1 顶部信息栏 =========================
        self.row_rt_1 = QFrame(self.R_realtime_detect)
        self.row_rt_1.setMinimumHeight(20)
        self.row_rt_1.setMaximumHeight(20)
        self.row_rt_1.setFrameShape(QFrame.StyledPanel)
        self.row_rt_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_rt_1 = QHBoxLayout(self.row_rt_1)
        self.horizontalLayout_rt_1.setContentsMargins(0, 0, 0, 0)

        self.label_rt_info = QLabel("点击下方按钮开始调用摄像头并实时检测", self.row_rt_1)
        self.label_rt_info.setStyleSheet("color: #6a7ba8; font-size: 10pt;")
        self.horizontalLayout_rt_1.addWidget(self.label_rt_info)

        self.verticalLayout_R_realtime.addWidget(self.row_rt_1)

        # ========================= row_2 控制栏 =========================
        self.row_rt_2 = QFrame(self.R_realtime_detect)
        self.row_rt_2.setMinimumHeight(40)
        self.row_rt_2.setMaximumHeight(40)
        self.row_rt_2.setFrameShape(QFrame.StyledPanel)
        self.row_rt_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_rt_2 = QHBoxLayout(self.row_rt_2)
        self.horizontalLayout_rt_2.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_rt_2.setSpacing(10)

        self.btn_realtime_start = QPushButton("开始")
        self.btn_realtime_start.setIcon(QIcon(":/icons/images/icons/cil-media-play.png"))
        self.btn_realtime_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_realtime_start.setFixedSize(140, 30)
        self.btn_realtime_start.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        self.horizontalLayout_rt_2.addStretch()
        self.horizontalLayout_rt_2.addWidget(self.btn_realtime_start)

        self.verticalLayout_R_realtime.addWidget(self.row_rt_2)

        # ========================= row_3 视频显示区域 =========================
        self.row_rt_3 = QFrame(self.R_realtime_detect)
        self.row_rt_3.setMinimumHeight(480)
        self.row_rt_3.setFrameShape(QFrame.StyledPanel)
        self.row_rt_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_rt_3 = QVBoxLayout(self.row_rt_3)
        self.verticalLayout_rt_3.setContentsMargins(0, 0, 0, 0)
        self.label_rt_video = QLabel("视频画面显示区", self.row_rt_3)
        self.label_rt_video.setAlignment(Qt.AlignCenter)
        self.label_rt_video.setStyleSheet("background-color: transparent; color: white;")
        self.row_rt_3.setStyleSheet("background-color: transparent;")
        self.verticalLayout_rt_3.addWidget(self.label_rt_video)
        self.verticalLayout_R_realtime.addWidget(self.row_rt_3)
        # 加入 stackedWidget 页面管理器
        self.stackedWidget.addWidget(self.R_realtime_detect)

        # 创建视频处理页面 R_movie
        self.R_movie = QWidget()
        self.R_movie.setObjectName("R_movie")
        self.R_movie.setStyleSheet("background-color: white;")
        self.verticalLayout_R_movie = QVBoxLayout(self.R_movie)
        self.verticalLayout_R_movie.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_R_movie.setSpacing(0)

        # ========================= row_1 文件选择 =========================
        self.row_1_movie = QFrame(self.R_movie)
        self.row_1_movie.setMinimumHeight(100)
        self.row_1_movie.setMaximumHeight(100)
        self.row_1_movie.setFrameShape(QFrame.StyledPanel)
        self.row_1_movie.setFrameShadow(QFrame.Raised)
        self.verticalLayout_row1_movie = QVBoxLayout(self.row_1_movie)
        self.verticalLayout_row1_movie.setSpacing(0)
        self.verticalLayout_row1_movie.setContentsMargins(0, 0, 0, 0)

        # 复用选择路径和按钮（跟R_image的一样）
        self.frame_div_content_1_movie = QFrame(self.row_1_movie)
        self.frame_div_content_1_movie.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1_movie.setFrameShadow(QFrame.Raised)
        self.verticalLayout_frame_div_movie = QVBoxLayout(self.frame_div_content_1_movie)
        self.verticalLayout_frame_div_movie.setSpacing(0)
        self.verticalLayout_frame_div_movie.setContentsMargins(0, 0, 0, 0)

        self.frame_content_wid_1_movie = QFrame(self.frame_div_content_1_movie)
        self.frame_content_wid_1_movie.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1_movie.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_content_movie = QHBoxLayout(self.frame_content_wid_1_movie)
        self.gridLayout_movie = QGridLayout()
        self.gridLayout_movie.setContentsMargins(-1, -1, -1, 0)

        # 路径输入框
        self.lineEdit_path_movie = QLineEdit(self.frame_content_wid_1_movie)
        self.lineEdit_path_movie.setPlaceholderText("请选择视频文件路径...")
        self.lineEdit_path_movie.setMinimumSize(QSize(0, 30))
        self.lineEdit_path_movie.setStyleSheet(
            "background-color: #5a6ea8; color: white; border-radius: 5px; padding: 6px; border: none;")
        self.gridLayout_movie.addWidget(self.lineEdit_path_movie, 0, 0, 1, 1)

        # 选择文件按钮
        self.btn_browse_movie = QPushButton("选择视频", self.frame_content_wid_1_movie)
        self.btn_browse_movie.setIcon(QIcon(":/icons/images/icons/cil-folder-open.png"))
        self.btn_browse_movie.setMinimumSize(QSize(150, 30))
        self.btn_browse_movie.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_browse_movie.setStyleSheet(
            "background-color: #5a6ea8; color: white; border-radius: 5px; padding: 6px 12px; border: none;")
        self.gridLayout_movie.addWidget(self.btn_browse_movie, 0, 1, 1, 1)

        # 说明文字
        self.label_description_movie = QLabel("选择算法  →  开始检测  →  执行操作"
                                              "      （左侧：原始视频 右侧：复原后视频）", self.frame_content_wid_1_movie)
        self.label_description_movie.setStyleSheet("color: #6a7ba8; font-size: 9pt;")
        self.gridLayout_movie.addWidget(self.label_description_movie, 1, 0, 1, 2)

        self.horizontalLayout_content_movie.addLayout(self.gridLayout_movie)
        self.verticalLayout_frame_div_movie.addWidget(self.frame_content_wid_1_movie)
        self.verticalLayout_row1_movie.addWidget(self.frame_div_content_1_movie)
        self.verticalLayout_R_movie.addWidget(self.row_1_movie)

        # ========================= row_2 控制栏 =========================
        self.row_2_movie = QFrame(self.R_movie)
        self.row_2_movie.setMinimumHeight(30)
        self.row_2_movie.setMaximumHeight(40)
        self.row_2_movie.setFrameShape(QFrame.StyledPanel)
        self.row_2_movie.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_controls_movie = QHBoxLayout(self.row_2_movie)
        self.horizontalLayout_controls_movie.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_controls_movie.setSpacing(10)

        # 模式选择下拉框
        self.combo1_movie = QComboBox()
        self.combo1_movie.addItems(["去雨", "去雾", "低光增强", "ALL-IN-ONE"])
        self.combo1_movie.setFixedSize(150, 30)
        self.combo1_movie.setStyleSheet("""
            QComboBox {
                background-color: #ffffff;
                color: black;
                border: 2px solid #5a6ea8;
                border-radius: 5px;
                padding: 5px;
            }
        """)

        # 功能选择下拉框
        self.combo2_movie = QComboBox()
        self.combo2_movie.addItems(["复原", "复原+检测"])
        self.combo2_movie.setFixedSize(150, 30)
        self.combo2_movie.setStyleSheet("""
            QComboBox {
                background-color: #ffffff;
                color: black;
                border: 2px solid #5a6ea8;
                border-radius: 5px;
                padding: 5px;
            }
        """)

        # 检测按钮
        self.btn_detect_movie = QPushButton("开始")
        self.btn_detect_movie.setIcon(QIcon(":/icons/images/icons/cil-media-play.png"))
        self.btn_detect_movie.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_detect_movie.setFixedSize(110, 30)
        self.btn_detect_movie.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)

        # 播放/暂停 按钮
        self.btn_pause_movie = QPushButton("暂停")
        self.btn_pause_movie.setIcon(QIcon(":/icons/images/icons/cil-media-pause.png"))
        self.btn_pause_movie.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pause_movie.setFixedSize(110, 30)
        self.btn_pause_movie.setStyleSheet("""
             QPushButton {
                 background-color: #ff5722;
                 color: white;
                 border: none;
                 border-radius: 4px;
                 padding: 5px 10px;
             }
             QPushButton:hover {
                 background-color: #e64a19;
             }
         """)
        # 加入布局
        self.horizontalLayout_controls_movie.addWidget(self.combo1_movie)
        self.horizontalLayout_controls_movie.addWidget(self.combo2_movie)
        self.horizontalLayout_controls_movie.addStretch()
        self.horizontalLayout_controls_movie.addWidget(self.btn_detect_movie)
        self.horizontalLayout_controls_movie.addWidget(self.btn_pause_movie)
        # 加入到页面
        self.verticalLayout_R_movie.addWidget(self.row_2_movie)

        # ========================= row_3 视频对比播放区域 =========================
        # row_3 视频对比播放区域
        self.row_3_movie = QFrame(self.R_movie)
        self.row_3_movie.setMinimumHeight(400)
        self.row_3_movie.setFrameShape(QFrame.StyledPanel)
        self.row_3_movie.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_video_compare = QHBoxLayout(self.row_3_movie)
        self.horizontalLayout_video_compare.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_video_compare.setSpacing(0)

        # 添加视频对比组件
        self.video_compare_widget = VideoCompareWidget(self.row_3_movie)
        self.horizontalLayout_video_compare.addWidget(self.video_compare_widget)

        # 把 row_3 加到整个页面布局
        self.verticalLayout_R_movie.addWidget(self.row_3_movie)

        # 最后！把整个R_movie页面注册到stackedWidget
        self.stackedWidget.addWidget(self.R_movie)





        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setBold(True)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"火 眼 金 睛 🔥", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"风雨无阻队 © 2025", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"展开", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"主页", None))
        self.btn_image.setText(QCoreApplication.translate("MainWindow", u"图片处理", None))
        self.btn_video.setText(QCoreApplication.translate("MainWindow", u"视频处理", None))
        self.btn_realtime.setText(QCoreApplication.translate("MainWindow", u"实时监测", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"历史数据", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"日志记录", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"退出", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"系统信息", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"系统信息", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"关闭", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"""
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
        <html>
        <head>
          <meta name="qrichtext" content="1" />
          <meta charset="utf-8" />
          <style type="text/css">
            p, li { white-space: pre-wrap; }
          </style>
        </head>
        <body style=" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;">

<!-- 系统名称 -->
<p align="left" style="margin-top:0px; margin-bottom:6px;">
  <span style="font-family:'Segoe UI', '微软雅黑', sans-serif; font-size:18pt; font-weight:600; letter-spacing:1px; color:#ff79c6;">    火 眼 金 睛</span>
</p>

<!-- 简介 -->
<p align="left" style="margin-top:6px; margin-bottom:20px; line-height:130%;">
  <span style="font-family:'Segoe UI', '微软雅黑', sans-serif; font-size:7.5pt; color:#ffb6f2;">面向交通场景的恶劣天气图像复原与检测系统</span>
</p>

<!-- 系统功能定位 -->
<p align="left" style="margin-top:12px; margin-bottom:6px;">
<span style="font-size:10pt; font-weight:600; color:#ff79c6;">系统功能定位:</span>
</p>
<p align="left" style="margin-top:6px; margin-bottom:12px; line-height:130%;">
<span style="font-size:9pt; color:#ffffff;">致力于提升智能交通系统在极端天气下的视觉感知能力。</span>
</p>

<!-- 视觉复原模块 -->
<p align="left" style="margin-top:12px; margin-bottom:6px;">
<span style="font-size:10pt; font-weight:600; color:#ff79c6;">视觉复原模块:</span>
</p>
<p align="left" style="margin-top:6px; margin-bottom:12px; line-height:130%;">
<span style="font-size:9pt; color:#ffffff;">采用MPMF-Net All-in-One 网络，支持雨、雾、雪、低光等恶劣天气图像的一体化增强复原。</span>
</p>

<!-- 目标检测模块 -->
<p align="left" style="margin-top:12px; margin-bottom:6px;">
<span style="font-size:10pt; font-weight:600; color:#ff79c6;">目标检测模块:</span>
</p>
<p align="left" style="margin-top:6px; margin-bottom:12px; line-height:130%;">
<span style="font-size:9pt; color:#ffffff;">系统集成 YOLOv12 高性能目标检测框架，兼顾速度与精度，适应复杂交通场景检测需求。</span>
</p>



<!-- 技术说明 -->
<p align="left" style="margin-top:12px; margin-bottom:12px; line-height:130%;">
<span style="font-size:9pt; color:#bbbbbb;">本系统复原模块基于我团队发表于 AAAI 2024 的 MPMF-Net 算法，具备领先的清晰度恢复能力与目标检测友好性。</span>
</p>

<p align="left" style="margin-top:25px; margin-bottom:6px; line-height:130%;">
<span style="font-size:9pt; color:#bd93f9;">开发团队：风雨无阻队</span>
</p>
<p align="left" style="margin-top:6px; margin-bottom:6px; line-height:130%;">
<span style="font-size:9pt; color:#bd93f9;">系统版本：v1.0.0</span>
</p>
<p align="left" style="margin-top:6px; margin-bottom:6px; line-height:130%;">
<span style="font-size:9pt; color:#bd93f9;">系统最后编译时间：2025/05/06</span>
</p>

        </body>
        </html>
        """, None))

        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"面向智能驾驶的恶劣天气图像复原与检测系统", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"NEW PAGE TEST", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"制作人： 风雨无阻队", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi