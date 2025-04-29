import os
import cv2
import numpy as np
import math
from PySide6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from PySide6.QtGui import QFont, QColor
from PySide6.QtCore import Qt
from scipy.ndimage import convolve
from scipy.special import gamma
from brisque import BRISQUE
from PIL import Image
from skimage import color
import pyiqa
import torchvision.transforms as T
from PIL import Image
import torch
piqe_model = pyiqa.create_metric('piqe', as_loss=False)
# 以下是你提供的代码，计算 NIQE
def estimate_aggd_param(block):
    """Estimate AGGD (Asymmetric Generalized Gaussian Distribution) parameters."""
    block = block.flatten()
    gam = np.arange(0.2, 10.001, 0.001)  # len = 9801
    gam_reciprocal = np.reciprocal(gam)
    r_gam = np.square(gamma(gam_reciprocal * 2)) / (gamma(gam_reciprocal) * gamma(gam_reciprocal * 3))

    left_std = np.sqrt(np.mean(block[block < 0]**2))
    right_std = np.sqrt(np.mean(block[block > 0]**2))
    gammahat = left_std / right_std
    rhat = (np.mean(np.abs(block)))**2 / np.mean(block**2)
    rhatnorm = (rhat * (gammahat**3 + 1) * (gammahat + 1)) / ((gammahat**2 + 1)**2)
    array_position = np.argmin((r_gam - rhatnorm)**2)

    alpha = gam[array_position]
    beta_l = left_std * np.sqrt(gamma(1 / alpha) / gamma(3 / alpha))
    beta_r = right_std * np.sqrt(gamma(1 / alpha) / gamma(3 / alpha))
    return (alpha, beta_l, beta_r)


def compute_feature(block):
    """Compute features."""
    feat = []
    alpha, beta_l, beta_r = estimate_aggd_param(block)
    feat.extend([alpha, (beta_l + beta_r) / 2])

    shifts = [[0, 1], [1, 0], [1, 1], [1, -1]]
    for i in range(len(shifts)):
        shifted_block = np.roll(block, shifts[i], axis=(0, 1))
        alpha, beta_l, beta_r = estimate_aggd_param(block * shifted_block)
        mean = (beta_r - beta_l) * (gamma(2 / alpha) / gamma(1 / alpha))
        feat.extend([alpha, mean, beta_l, beta_r])
    return feat


def niqe(img, mu_pris_param, cov_pris_param, gaussian_window, block_size_h=96, block_size_w=96):
    """Calculate NIQE metric."""
    assert img.ndim == 2, ('Input image must be a gray or Y (of YCbCr) image with shape (h, w).')
    h, w = img.shape
    num_block_h = math.floor(h / block_size_h)
    num_block_w = math.floor(w / block_size_w)
    img = img[0:num_block_h * block_size_h, 0:num_block_w * block_size_w]

    distparam = []
    for scale in (1, 2):
        mu = convolve(img, gaussian_window, mode='nearest')
        sigma = np.sqrt(np.abs(convolve(np.square(img), gaussian_window, mode='nearest') - np.square(mu)))
        img_nomalized = (img - mu) / (sigma + 1)

        feat = []
        for idx_w in range(num_block_w):
            for idx_h in range(num_block_h):
                block = img_nomalized[idx_h * block_size_h // scale:(idx_h + 1) * block_size_h // scale,
                                      idx_w * block_size_w // scale:(idx_w + 1) * block_size_w // scale]
                feat.append(compute_feature(block))

        distparam.append(np.array(feat))

        if scale == 1:
            img = cv2.resize(img / 255., (int(img.shape[1] * 0.5), int(img.shape[0] * 0.5)), interpolation=cv2.INTER_CUBIC)
            img = img * 255.

    distparam = np.concatenate(distparam, axis=1)
    mu_distparam = np.nanmean(distparam, axis=0)
    distparam_no_nan = distparam[~np.isnan(distparam).any(axis=1)]
    cov_distparam = np.cov(distparam_no_nan, rowvar=False)

    invcov_param = np.linalg.pinv((cov_pris_param + cov_distparam) / 2)
    quality = np.matmul(np.matmul((mu_pris_param - mu_distparam), invcov_param),
                        np.transpose((mu_pris_param - mu_distparam)))
    quality = np.sqrt(quality)
    quality = float(np.squeeze(quality))
    return quality

def get_arrow(diff, reverse=False):
    """返回⬆或⬇，根据质量改善方向"""
    return "🟢  提高" if (diff < 0 if reverse else diff > 0) else "🔴  降低"


def calculate_niqe(img, crop_border, params_path, input_order='HWC', convert_to='y', **kwargs):
    """Calculate NIQE metric."""
    niqe_pris_params = np.load(os.path.join(params_path, 'niqe_pris_params.npz'))
    mu_pris_param = niqe_pris_params['mu_pris_param']
    cov_pris_param = niqe_pris_params['cov_pris_param']
    gaussian_window = niqe_pris_params['gaussian_window']

    img = img.astype(np.float32)
    if img.ndim == 3 and img.shape[2] == 3:  # 彩色图像 (h, w, 3)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)  # 转换为 YCbCr 图像
        img = img[:, :, 0]  # 只提取 Y 通道

    # 如果是Y通道（YCbCr），直接使用
    if convert_to == 'y':
        img = img  # 已经是 Y 通道

    img = np.squeeze(img)

    if crop_border != 0:
        img = img[crop_border:-crop_border, crop_border:-crop_border]

    img = img.round()

    # 计算 NIQE 得分
    niqe_result = niqe(img, mu_pris_param, cov_pris_param, gaussian_window)
    return niqe_result

def calculate_brisque_score(img):
    """使用 BRISQUE 计算图像无参考质量分数"""
    model = BRISQUE()
    # OpenCV图像需要转为 PIL 格式
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    img_array = np.array(img_pil)
    return model.score(img_array)

def calculate_piqe_score(img_bgr):
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    tensor = T.ToTensor()(img_pil).unsqueeze(0)  # shape: [1, 3, H, W]
    score = piqe_model(tensor).item()
    return score


class QuantitativeAnalysisDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("定量分析结果")
        self.setFixedSize(1000, 600)

        layout = QVBoxLayout(self)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(0)  # 初始不设行数
        self.tableWidget.setColumnCount(5)  # 列数
        self.tableWidget.setHorizontalHeaderLabels(["", "原始图像", "恢复后图像", "比较差值","比对结果"])
        self.tableWidget.setColumnWidth(0, 120)  # 指标名
        self.tableWidget.setColumnWidth(1, 200)  # 原图
        self.tableWidget.setColumnWidth(2, 200)  # 复原图
        self.tableWidget.setColumnWidth(3, 200)  # 差值
        self.tableWidget.setColumnWidth(4, 120)  # 比对结果
        layout.addWidget(self.tableWidget)


        self.setLayout(layout)

    def set_image_paths(self, input_path, output_path):
        self.saved_input_path = input_path
        self.saved_output_path = output_path

        # 加载图像
        original_image = cv2.imread(self.saved_input_path)
        restored_image = cv2.imread(self.saved_output_path)

        if original_image is None or restored_image is None:
            print("图像加载失败！请检查路径！")
            return

        # 计算 NIQE 评分
        params_path = os.path.join(os.path.dirname(__file__))
        niqe_original = calculate_niqe(original_image, crop_border=0, params_path=params_path)
        niqe_restored = calculate_niqe(restored_image, crop_border=0, params_path=params_path)
        brisque_original = calculate_brisque_score(original_image)
        brisque_restored = calculate_brisque_score(restored_image)
        diff_niqe = niqe_restored - niqe_original
        diff_brisque = brisque_restored - brisque_original
        piqe_original = calculate_piqe_score(original_image)
        piqe_restored = calculate_piqe_score(restored_image)
        diff_piqe = piqe_restored - piqe_original

        data = [
            ["NIQE", f"{niqe_original:.4f}", f"{niqe_restored:.4f}", f"{diff_niqe:.4f}",
             get_arrow(diff_niqe, reverse=True)],
            ["BRISQUE", f"{brisque_original:.4f}", f"{brisque_restored:.4f}", f"{diff_brisque:.4f}",
             get_arrow(diff_brisque, reverse=True)],
            ["PIQE", f"{piqe_original:.4f}", f"{piqe_restored:.4f}", f"{diff_piqe:.4f}",
             get_arrow(diff_piqe, reverse=True)]
        ]
        self.tableWidget.setRowCount(len(data))
        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignCenter)
                if col == 0:
                    item.setBackground(QColor(220, 220, 220))
                    item.setFont(QFont('Arial', 10, QFont.Bold))
                self.tableWidget.setItem(row, col, item)
