import os, shutil, string


def show_disk_usage():
    drives = [f"{d}:/" for d in string.ascii_uppercase
             if os.path.exists(f"{d}:/")]
    
    for drive in drives:
        total, used, free = shutil.disk_usage(drive)
        print(f"Disk usage for {drive}")
        print(f" -Total: {total // (2**30)} GB")
        print(f" -Used: {used // (2**30)} GB")
        print(f" -free: {free // (2**30)} GB \n")
    
    
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