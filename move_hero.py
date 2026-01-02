import shutil
import os

src = r"C:\Users\Ganesh_Sunkara\.gemini\antigravity\brain\0af57653-e282-49d8-bb3e-c0b0fac2beec\hero_3d_books_1767346276287.png"
dst = r"e:\pustak\pustakam\static\books\images\hero_3d.png"

try:
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)
    print(f"Successfully moved 3D Hero to {dst}")
except Exception as e:
    print(f"Error: {e}")
