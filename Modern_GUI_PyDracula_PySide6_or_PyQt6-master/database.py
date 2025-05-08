import sqlite3
import os

DB_NAME = "users.db"


def get_db_connection():
    """
    获取数据库连接对象
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    初始化数据库，如果表不存在则创建
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # 创建用户表
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       username
                       TEXT
                       NOT
                       NULL
                       UNIQUE,
                       password_hash
                       TEXT
                       NOT
                       NULL,
                       salt
                       TEXT
                       NOT
                       NULL
                   )
                   ''')
    conn.commit()
    conn.close()


def register_user(username, password_hash, salt):
    """
    注册新用户
    :param username: 用户名
    :param password_hash: 哈希后的密码
    :param salt: 密码盐值
    :return: True 如果成功，False 如果失败
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
                       (username, password_hash, salt))

        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # 用户名重复
        return False
    finally:
        conn.close()
