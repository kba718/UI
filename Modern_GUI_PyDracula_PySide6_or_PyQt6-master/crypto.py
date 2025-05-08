# crypto.py
import hashlib
import os
from hmac import compare_digest

# 配置 PBKDF2 参数
HASH_NAME = 'sha256'
ITERATIONS = 100_000
SALT_SIZE = 16
KEY_LENGTH = 32


def hash_password(password: str):
    """使用 PBKDF2 进行密码哈希处理"""
    salt = os.urandom(SALT_SIZE)
    hashed_password = hashlib.pbkdf2_hmac(HASH_NAME, password.encode(), salt, ITERATIONS, KEY_LENGTH)
    return hashed_password.hex(), salt.hex()


def verify_password(stored_password: str, stored_salt: str, provided_password: str):
    """验证密码是否匹配"""
    salt = bytes.fromhex(stored_salt)
    hashed_password = hashlib.pbkdf2_hmac(HASH_NAME, provided_password.encode(), salt, ITERATIONS, KEY_LENGTH)
    return compare_digest(stored_password, hashed_password.hex())
