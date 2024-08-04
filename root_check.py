import os
import subprocess

def check_su_binary():
    """Check for su binary in common locations."""
    paths = ["/system/bin/su", "/system/xbin/su", "/sbin/su", "/system/su", "/su/bin/su"]
    for path in paths:
        if os.path.exists(path):
            return True
    return False

def check_superuser_apk():
    """Check for Superuser APK."""
    paths = ["/system/app/Superuser.apk", "/system/app/SuperSU.apk", "/system/app/Magisk.apk"]
    for path in paths:
        if os.path.exists(path):
            return True
    return False

def execute_su_command():
    """Attempt to execute a command with su."""
    try:
        result = subprocess.run(['su', '-c', 'id'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if 'uid=0' in result.stdout:
            return True
    except Exception as e:
        pass
    return False

def check_root():
    """Perform all checks to determine root status."""
    if check_su_binary():
        print("Root check: su binary found. Your device is rooted.")
    elif check_superuser_apk():
        print("Root check: Superuser app found. Your device is rooted.")
    elif execute_su_command():
        print("Root check: su command executed successfully. Your device is rooted.")
    else:
        print("Your device is not rooted.")

if __name__ == "__main__":
    check_root()
