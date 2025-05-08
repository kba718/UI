from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QFrame, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon
import os
from database import register_user, get_db_connection
from crypto import hash_password


class RegisterDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用户注册")
        self.setWindowIcon(QIcon("icon.png"))
        self.setFixedSize(500, 600)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 30, 40, 40)
        main_layout.setSpacing(20)

        # ========================= Logo 区域 =========================
        logo_frame = QFrame()
        logo_layout = QHBoxLayout(logo_frame)
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
        main_layout.addWidget(logo_frame)

        # ========================= 用户名输入 =========================
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("请输入用户名")
        self.username_input.setStyleSheet(
            "padding: 15px; font-size: 16px; border-radius: 5px; border: 2px solid #bdc3c7;"
        )
        main_layout.addWidget(self.username_input)

        # ========================= 密码输入 =========================
        password_layout = QHBoxLayout()
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("请输入密码")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(
            "padding: 15px; font-size: 16px; border-radius: 5px; border: 2px solid #bdc3c7;"
        )
        password_layout.addWidget(self.password_input)

        # 锁定按钮
        lock_icon_path = os.path.abspath(os.path.join(base_dir, "images", "icons", "cil-lock-locked.png"))
        unlock_icon_path = os.path.abspath(os.path.join(base_dir, "images", "icons", "cil-lock-unlocked.png"))
        self.toggle_lock_button = QPushButton()
        self.toggle_lock_button.setIcon(QIcon(lock_icon_path))
        self.toggle_lock_button.setFixedSize(40, 40)
        self.toggle_lock_button.setStyleSheet("border: none;")
        self.toggle_lock_button.setCheckable(True)
        self.toggle_lock_button.clicked.connect(self.toggle_password_visibility)

        password_layout.addWidget(self.toggle_lock_button)
        main_layout.addLayout(password_layout)

        # ========================= 确认密码 =========================
        confirm_password_layout = QHBoxLayout()
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("确认密码")
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.confirm_password_input.setStyleSheet(
            "padding: 15px; font-size: 16px; border-radius: 5px; border: 2px solid #bdc3c7;"
        )
        confirm_password_layout.addWidget(self.confirm_password_input)

        # 锁定按钮
        self.toggle_confirm_lock_button = QPushButton()
        self.toggle_confirm_lock_button.setIcon(QIcon(lock_icon_path))
        self.toggle_confirm_lock_button.setFixedSize(40, 40)
        self.toggle_confirm_lock_button.setStyleSheet("border: none;")
        self.toggle_confirm_lock_button.setCheckable(True)
        self.toggle_confirm_lock_button.clicked.connect(self.toggle_confirm_password_visibility)

        confirm_password_layout.addWidget(self.toggle_confirm_lock_button)
        main_layout.addLayout(confirm_password_layout)

        # ========================= 注册按钮 =========================
        self.register_button = QPushButton("注 册")
        self.register_button.setFixedSize(150, 50)
        self.register_button.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border-radius: 8px;
                border: none;
                font-size: 18px;
            }
            QPushButton:hover { background-color: #27ae60; }
            QPushButton:pressed { background-color: #219a52; }
        """)
        self.register_button.clicked.connect(self.handle_register)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.register_button)
        main_layout.addLayout(button_layout)

        # ========================= 提示信息 =========================
        hint_label = QLabel("请填写完整信息进行注册")
        hint_label.setAlignment(Qt.AlignCenter)
        hint_label.setStyleSheet("color: #95a5a6; font-size: 14px;")
        main_layout.addWidget(hint_label)

        self.setLayout(main_layout)

    def toggle_password_visibility(self):
        if self.toggle_lock_button.isChecked():
            self.password_input.setEchoMode(QLineEdit.Normal)
            unlock_icon_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "images", "icons", "cil-lock-unlocked.png"))
            self.toggle_lock_button.setIcon(QIcon(unlock_icon_path))
        else:
            self.password_input.setEchoMode(QLineEdit.Password)
            lock_icon_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "images", "icons", "cil-lock-locked.png"))
            self.toggle_lock_button.setIcon(QIcon(lock_icon_path))

    def toggle_confirm_password_visibility(self):
        if self.toggle_confirm_lock_button.isChecked():
            self.confirm_password_input.setEchoMode(QLineEdit.Normal)
            unlock_icon_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "images", "icons", "cil-lock-unlocked.png"))
            self.toggle_confirm_lock_button.setIcon(QIcon(unlock_icon_path))
        else:
            self.confirm_password_input.setEchoMode(QLineEdit.Password)
            lock_icon_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "images", "icons", "cil-lock-locked.png"))
            self.toggle_confirm_lock_button.setIcon(QIcon(lock_icon_path))

    def handle_register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "输入错误", "用户名和密码不能为空")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "输入错误", "两次输入的密码不一致")
            return

        encrypted_password = hash_password(password)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        if cursor.fetchone():
            QMessageBox.warning(self, "注册失败", "用户名已存在，请选择其他用户名")
            conn.close()
            return

        cursor.execute("INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
                       (username, encrypted_password[0], encrypted_password[1]))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "注册成功", "用户已创建，请返回登录")
        self.accept()
