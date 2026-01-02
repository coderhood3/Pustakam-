import shutil
import os

src = r"C:\Users\Ganesh_Sunkara\.gemini\antigravity\brain\0af57653-e282-49d8-bb3e-c0b0fac2beec\premium_library_bg_1767344202752.png"
dst = r"e:\pustak\pustakam\static\books\images\bg_main.png"

try:
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)
    print(f"Successfully copied to {dst}")
except Exception as e:
    print(f"Error: {e}")
