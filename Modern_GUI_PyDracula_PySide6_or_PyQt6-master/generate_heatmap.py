# generate_heatmap.py

import os
import cv2
import numpy as np

def generate_and_save_heatmaps(before_path, after_path, h_o_dir, h_r_dir):
    """
    根据原图和复原图生成各自的叠加热力图，并保存到指定文件夹。
    返回两个热力图文件的路径。
    """
    if not os.path.exists(before_path) or not os.path.exists(after_path):
        raise FileNotFoundError("原图或复原图路径不存在")

    img_before = cv2.imread(before_path)
    img_after = cv2.imread(after_path)

    if img_before is None or img_after is None:
        raise ValueError("无法加载原图或复原图")

    # 灰度化
    gray_before = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)
    gray_after = cv2.cvtColor(img_after, cv2.COLOR_BGR2GRAY)

    # 计算差异
    diff = cv2.absdiff(gray_before, gray_after)
    diff_normalized = cv2.normalize(diff, None, 0, 255, cv2.NORM_MINMAX)

    # 将差异映射成彩色热力图
    diff_color = cv2.applyColorMap(diff_normalized, cv2.COLORMAP_JET)

    # 融合原图和热力图（叠加效果，权重可调）
    overlay_before = cv2.addWeighted(img_before, 0.7, diff_color, 0.3, 0)
    overlay_after = cv2.addWeighted(img_after, 0.7, diff_color, 0.3, 0)

    # 创建输出文件夹
    os.makedirs(h_o_dir, exist_ok=True)
    os.makedirs(h_r_dir, exist_ok=True)

    base_before = os.path.basename(before_path)  # 例如 1_4_26_1242.png
    # 注意：只基于原图名生成 H_ 和 H_R_ 文件名！

    heatmap_before_path = os.path.join(h_o_dir, f"H_{base_before}")
    heatmap_after_path = os.path.join(h_r_dir, f"H_R_{base_before}")

    # 保存图片
    cv2.imwrite(heatmap_before_path, overlay_before)
    cv2.imwrite(heatmap_after_path, overlay_after)

    return heatmap_before_path, heatmap_after_path
