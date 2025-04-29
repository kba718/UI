import os
import cv2
import numpy as np

def generate_and_save_heatmaps(before_path, after_path, h_o_dir, h_r_dir):
    """
    根据原图和复原图生成融合了差异 + 结构感知（束状效果）的热力图，并保存。
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

    # 差异图
    diff = cv2.absdiff(gray_before, gray_after)
    diff_normalized = cv2.normalize(diff, None, 0, 255, cv2.NORM_MINMAX)
    diff_color = cv2.applyColorMap(diff_normalized, cv2.COLORMAP_JET)

    # 结构方向性差异（类似束状效果）
    sobel_before = cv2.Sobel(gray_before, cv2.CV_64F, 1, 1, ksize=3)
    sobel_after = cv2.Sobel(gray_after, cv2.CV_64F, 1, 1, ksize=3)
    sobel_diff = cv2.absdiff(np.abs(sobel_before), np.abs(sobel_after))
    sobel_diff_norm = cv2.normalize(sobel_diff, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    sobel_heatmap = cv2.applyColorMap(sobel_diff_norm, cv2.COLORMAP_JET)

    # 合并两种热图：颜色差异 + 结构束状感
    combined_heatmap = cv2.addWeighted(diff_color, 0.5, sobel_heatmap, 0.5, 0)

    # 融合原图和热力图（叠加效果）
    overlay_before = cv2.addWeighted(img_before, 0.7, combined_heatmap, 0.3, 0)
    overlay_after = cv2.addWeighted(img_after, 0.7, combined_heatmap, 0.3, 0)

    # 创建输出文件夹
    os.makedirs(h_o_dir, exist_ok=True)
    os.makedirs(h_r_dir, exist_ok=True)

    base_before = os.path.basename(before_path)
    heatmap_before_path = os.path.join(h_o_dir, f"H_{base_before}")
    heatmap_after_path = os.path.join(h_r_dir, f"H_R_{base_before}")

    cv2.imwrite(heatmap_before_path, overlay_before)
    cv2.imwrite(heatmap_after_path, overlay_after)

    return heatmap_before_path, heatmap_after_path
