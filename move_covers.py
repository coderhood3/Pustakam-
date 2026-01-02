import shutil
import os

base_path = r"C:\Users\Ganesh_Sunkara\.gemini\antigravity\brain\0af57653-e282-49d8-bb3e-c0b0fac2beec"
dest_path = r"e:\pustak\pustakam\static\books\images"

files = [
    ("cover_fiction_1767347787584.png", "cover_fiction.png"),
    ("cover_business_1767347804310.png", "cover_business.png"),
    ("cover_thriller_1767347823534.png", "cover_thriller.png"),
    ("cover_kids_1767347842295.png", "cover_kids.png")
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
