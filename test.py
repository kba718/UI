from brisque import BRISQUE
import numpy as np
from PIL import Image

# 安全路径写法
img_path = r"D:\MTM\wen\p2\Rframe_000026.jpg"
img = Image.open(img_path)
img = np.asarray(img)

model = BRISQUE()

# 推荐自动适配写法
if hasattr(model, "score"):
    print("BRISQUE score:", model.score(img))
elif hasattr(model, "__call__"):
    print("BRISQUE score:", model(img))
else:
    print("BRISQUE接口不支持，请检查源码版本")
