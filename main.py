import os, shutil, string
import subprocess, platform
from datetime import datetime


def log_action(action_type, data):
    with open("system_log.txt", "a") as log_file:
        log_file.write(f"\n[{datetime.now()}] ==== {action_type} ===\n{data}\n")

def show_disk_usage():
    drives = [f"{a}:/" for a in string.ascii_uppercase if os.path.exists(f"{a}:/")]
    
    for drive in drives:
        total, used, free = shutil.disk_usage(drive)
        total_gb = total // (2**30)
        used_gb = used // (2**30)
        free_gb = free // (2**30)

        print(f"Disk usage for {drive}")
        print(f" -Total: {total_gb} GB")
        print(f" -Used: {used_gb} GB")
        print(f" -Free: {free_gb} GB\n")

        log_data = f"{drive} - Total: {total_gb} GB, Used: {used_gb} GB, Free: {free_gb} GB"
        log_action("Disk Usage", log_data)


def create_user_cross_platform():
    os_name = platform.system()
    
    username = input("Enter the new username: ")
    
    if os_name == "linux":
        cmd = ["sudo", "useradd", username]
    elif os_name == "Windows":
        password = input(f"Enter password for ({username}) this user name: ")
        cmd = [ "net", "user", username, password, "/add"]
    else:
        print(f"Unsupported OS: {os_name}")
        return
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"User '{username}' created successfully on {os_name}")
    else:
        print(f"Failed to create user '{username}': {result.stderr}")




def show_menu():
    print('''
===== System Automation Toolkit =====
1. Show Disk Usage
2. Create New User
3. Show System Uptime
4. Exit
          ''')

while True:
    show_menu()
    choice = int(input("Enter your choice (1-4): "))
    
    try:
        if choice == 1:
            print("Showing Disk Usage...\n")
            show_disk_usage()
        elif choice == 2:
            print("Creating a New User...\n")
            create_user_cross_platform()
        elif choice == 3:
            print("Show System Uptime...\n")
        elif choice == 4:
            print("Good Bye....")
            break
        else:
            print("Invalid Choice.....")
    except Exception as e:
        print("Someting is wrong.....!!", e)
    
show_menu()