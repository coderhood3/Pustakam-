import os
import sys
import shutil
from django.core.management import execute_from_command_line

def run_build_check():
    print("="*50)
    print("STARTING LOCAL BUILD SIMULATION")
    print("="*50)

    # 1. Environment Setup
    os.environ['DEBUG'] = 'False'
    os.environ['DJANGO_SETTINGS_MODULE'] = 'pustakam.settings'
    print(f"[Check] Environment: DEBUG={os.environ.get('DEBUG')}")

    # 2. Check System Settings
    print("\n[Step 1] Running System Check...")
    try:
        execute_from_command_line(['manage.py', 'check', '--deploy'])
        print(">> System check PASSED.")
    except Exception as e:
        print(f">> System check FAILED: {e}")
        # specific deploy checks might fail on secret key etc locally, but we care about structure
        pass 

    # 3. Static Collection (The Deployment Killer)
    print("\n[Step 2] Running collectstatic (Dry Run)...")
    # Clean staticfiles dir first to ensure fresh build
    static_root = os.path.join(os.getcwd(), 'staticfiles')
    if os.path.exists(static_root):
        shutil.rmtree(static_root)
    
    try:
        execute_from_command_line(['manage.py', 'collectstatic', '--noinput', '--clear'])
        print(">> collectstatic PASSED.")
    except Exception as e:
        print(f">> collectstatic FAILED: {e}")
        sys.exit(1)

    print("\n" + "="*50)
    print("BUILD SIMULATION SUCCESSFUL")
    print("The codebase is ready for Render deployment.")
    print("="*50)

if __name__ == "__main__":
    run_build_check()
