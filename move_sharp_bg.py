import shutil
import os

src = r"C:\Users\Ganesh_Sunkara\.gemini\antigravity\brain\0af57653-e282-49d8-bb3e-c0b0fac2beec\library_sharp_real_1767345604038.png"
dst = r"e:\pustak\pustakam\static\books\images\bg_main.png"

try:
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        print(f"Successfully moved sharp background to {dst}")
    else:
        print(f"Source file not found: {src}")
except Exception as e:
    print(f"Error: {e}")
