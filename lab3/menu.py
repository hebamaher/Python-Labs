from console_app import register, login, create_project, view_projects, delete_project, search_by_date
import console_app
import json

while True:
    print("""
                1. Register
                2. Login
                3. Exit
            """)
    choice = input("Choose: ")

    if choice == "1":
        register()
    elif choice == "2":
        user = login()
        if user:
            while True:
                print("""
                            1. Create Project
                            2. View Projects
                            3. Delete My Project
                            4. Search by Date
                            5. Logout
                    """)
                action = input("Choose: ")
                if action == "1":
                    create_project(user)
                elif action == "2":
                    view_projects()
                elif action == "3":
                    delete_project(user)
                elif action == "4":
                    search_by_date()
                elif action == "5":
                    break
    elif choice == "3":
        break


