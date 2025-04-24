import os
import sys
import torch
import torch.nn.functional as F
from torchvision.utils import save_image
from model import MPMFNet
from options import Options
from datasets import MyTestDataSet
from torch.utils.data import DataLoader
from PIL import Image
import torchvision.transforms as transforms
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from utils import generate_result_image_path

def run_all_in_one_restore(input_path, output_path):
    """
    使用 ALL-IN-ONE 模型对指定图片进行复原，输出路径统一由 utils 生成
    """
    # 初始化配置和模型
    opt = Options()
    opt.CUDA_USE = torch.cuda.is_available()
    device = torch.device("cuda" if opt.CUDA_USE else "cpu")

    model = MPMFNet()
    model = torch.nn.DataParallel(model)
    model.load_state_dict(torch.load(opt.MODEL_RESUME_PATH, map_location=device))
    model.to(device)
    model.eval()

    # 读取图像并预处理
    image = Image.open(input_path).convert('RGB')
    transform = transforms.ToTensor()
    input_tensor = transform(image).unsqueeze(0).to(device)  # [1, C, H, W]

    # 记录原始尺寸并 resize 到网络输入大小
    original_size = image.size[::-1]  # (H, W)
    input_resized = F.interpolate(input_tensor, size=(400, 700), mode='bilinear')

    # 推理
    with torch.no_grad():
        output, _ = model(input_resized)
        output = F.interpolate(output, size=original_size, mode='bilinear')

    # 使用工具函数生成保存路径
    output_path = generate_result_image_path()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    save_image(output, output_path)
    print(f"ALL-IN-ONE 恢复完成：{output_path}")
