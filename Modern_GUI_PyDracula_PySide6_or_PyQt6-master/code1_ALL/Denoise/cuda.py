import torch
import torch.nn as nn

dummy_model = nn.Conv2d(3, 64, kernel_size=3, padding=1).cuda()
size = 128
while True:
    try:
        dummy_input = torch.randn(1, 3, size, size).cuda()
        dummy_output = dummy_model(dummy_input)
        print(f"Success with size: {size}x{size}")
        size += 64
    except RuntimeError as e:
        print(f"OOM at size: {size}x{size}")
        break
