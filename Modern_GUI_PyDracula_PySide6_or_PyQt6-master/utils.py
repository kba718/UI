
import os
from datetime import datetime


def generate_result_image_path():
    base_dir = os.path.join(os.path.dirname(__file__), "R_picture")
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    now = datetime.now()
    date_str = f"{now.month}_{now.day}"
    time_str = now.strftime("%H%M")

    existing_numbers = []
    for fname in os.listdir(base_dir):
        if fname.startswith("R_") and fname.endswith(".png"):
            try:
                num = int(fname.split("_")[1])
                existing_numbers.append(num)
            except:
                continue
    next_index = max(existing_numbers + [0]) + 1
    filename = f"R_{next_index}_{date_str}_{time_str}.png"
    return os.path.join(base_dir, filename)
