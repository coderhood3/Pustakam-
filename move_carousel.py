import shutil
import os

base_path = r"C:\Users\Ganesh_Sunkara\.gemini\antigravity\brain\0af57653-e282-49d8-bb3e-c0b0fac2beec"
dest_path = r"e:\pustak\pustakam\static\books\images"

files = [
    ("banner_book_fair_1767348198448.png", "banner_book_fair.png"),
    ("banner_weekend_read_1767348217124.png", "banner_weekend.png")
]

try:
    os.makedirs(dest_path, exist_ok=True)
    for src_name, dst_name in files:
        src = os.path.join(base_path, src_name)
        dst = os.path.join(dest_path, dst_name)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"Moved {src_name} to {dst_name}")
        else:
            print(f"Source not found: {src_name}")
except Exception as e:
    print(f"Error: {e}")
