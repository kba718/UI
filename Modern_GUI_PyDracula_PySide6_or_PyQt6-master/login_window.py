from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QFrame, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon
import os
from database import get_db_connection, init_db
from crypto import verify_password
from register_window import RegisterDialog


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("火眼金睛 - 用户登录")
        self.setWindowIcon(QIcon("icon.png"))
        self.setFixedSize(500, 800)
        self.failed_attempts = 0
        init_db()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 30, 40, 40)
        main_layout.setSpacing(20)

        # ========================= Logo 区域 =========================
        logo_frame = QFrame()
        logo_layout = QVBoxLayout(logo_frame)
        logo_layout.setContentsMargins(0, 0, 0, 0)
        logo_label = QLabel()

        # 获取相对路径
        base_dir = os.path.dirname(__file__)
        image_path = os.path.abspath(os.path.join(base_dir, "images", "images", "PyDracula_vertical.png"))

        # 加载图片
        logo_pixmap = QPixmap(image_path).scaled(180, 180, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        if logo_pixmap.isNull():
            logo_label.setText("图片加载失败")
        else:
            logo_label.setPixmap(logo_pixmap)

        logo_layout.addWidget(logo_label, 0, Qt.AlignCenter)

        # ✅ 插入一个垂直的 SpacerItem 来增加间距
        spacer = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)
        logo_layout.addSpacerItem(spacer)

        main_layout.addWidget(logo_frame)

        # ========================= 账号输入框 =========================
        username_layout = QHBoxLayout()
        username_label = QLabel("账号:")
        username_label.setStyleSheet("font-size: 14px; margin-right: 5px;")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("请输入用户名")
        self.username_input.setStyleSheet(
            "padding: 8px; font-size: 14px; border-radius: 5px; border: 1px solid #bdc3c7;")
        self.username_input.setFixedHeight(40)

        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_input)
        main_layout.addLayout(username_layout)

        # ========================= 密码输入框 =========================
        password_layout = QHBoxLayout()
        password_label = QLabel("密码:")
        password_label.setStyleSheet("font-size: 14px; margin-right: 5px;")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("请输入密码")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(
            "padding: 8px; font-size: 14px; border-radius: 5px; border: 1px solid #bdc3c7;")
        self.password_input.setFixedHeight(40)

        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)
        main_layout.addLayout(password_layout)

        # ========================= 按钮区域 =========================
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)  # 调整按钮之间的间距

        # 增加上方的空白距离
        button_layout.addSpacerItem(QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.login_button = QPushButton("登录")
        self.login_button.setFixedSize(120, 45)
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 8px;
                border: none;
                font-size: 16px;
            }
            QPushButton:hover { background-color: #2980b9; }
            QPushButton:pressed { background-color: #1d6fa5; }
        """)
        self.login_button.clicked.connect(self.handle_login)

        self.register_button = QPushButton("注册")
        self.register_button.setFixedSize(120, 45)
        self.register_button.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border-radius: 8px;
                border: none;
                font-size: 16px;
            }
            QPushButton:hover { background-color: #27ae60; }
            QPushButton:pressed { background-color: #219a52; }
        """)
        self.register_button.clicked.connect(self.handle_register)

        self.exit_button = QPushButton("退出")
        self.exit_button.setFixedSize(120, 45)
        self.exit_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border-radius: 8px;
                border: none;
                font-size: 16px;
            }
            QPushButton:hover { background-color: #c0392b; }
            QPushButton:pressed { background-color: #a93226; }
        """)
        self.exit_button.clicked.connect(self.close)

        button_layout.addWidget(self.login_button)
        button_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))
        button_layout.addWidget(self.register_button)
        button_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))
        button_layout.addWidget(self.exit_button)

        main_layout.addLayout(button_layout)
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))
        # ========================= 提示信息 =========================
        hint_label = QLabel("提示：请使用您的用户名和密码登录")
        hint_label.setAlignment(Qt.AlignCenter)
        hint_label.setStyleSheet("color: #95a5a6; font-size: 14px; margin-top: 5px;")
        main_layout.addWidget(hint_label)

        # ========================= 版权标识 =========================
        copyright_label = QLabel("开发团队：风雨无阻队 @2025 v1.0.0")
        copyright_label.setAlignment(Qt.AlignRight)
        copyright_label.setStyleSheet("color: #95a5a6; font-size: 12px; margin-right: 15px;")

        # 使用 QHBoxLayout 将它放到底部，并居右对齐
        footer_layout = QHBoxLayout()
        footer_layout.addStretch()  # 增加左边空白
        footer_layout.addWidget(copyright_label)

        # 增加底部的垂直空白，避免贴边
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        main_layout.addLayout(footer_layout)

        self.setLayout(main_layout)

    def handle_register(self):
        """ 打开注册窗口并处理注册结果 """
        dialog = RegisterDialog()
        result = dialog.exec()
        if result == QDialog.Accepted:
            QMessageBox.information(self, "注册成功", "用户注册成功，请使用新账号登录")
        else:
            QMessageBox.warning(self, "注册失败", "注册未完成或取消。")

    def handle_login(self):
        """ 处理登录逻辑 """
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "登录失败", "用户名或密码不能为空！")
            return

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash, salt FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user:
            stored_password, salt = user
            if verify_password(stored_password, salt, password):
                QMessageBox.information(self, "登录成功", f"欢迎回来, {username}!")
                self.accept()
            else:
                QMessageBox.warning(self, "登录失败", "用户名或密码错误！")
        else:
            QMessageBox.warning(self, "登录失败", "用户名不存在，请先注册！")
