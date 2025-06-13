

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