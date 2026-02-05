import json
import re
from datetime import datetime

USERS_FILE = "users.json"
PROJECTS_FILE = "projects.json"


def load_data(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)



def register():
    users = load_data(USERS_FILE)

    first_name = input("First name: ")
    if not first_name.isalpha():
        print("First name must contain only letters.")
        return
    last_name = input("Last name: ")
    if not last_name.isalpha():
        print("Last name must contain only letters.")
        return


    email = input("Email: ")
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.fullmatch(email_pattern, email):
        print("Invalid email format.")
        return
    else:
        for u in users:
            if u["email"] == email:
                print("Email already exists.")
                return

    password = input("Password: ")
    confirm = input("Confirm Password: ")
    if password != confirm:
        print("Passwords do not match.")
        return

    phone = input("Mobile phone: ")
    if not re.fullmatch(r"^01[0-2,5][0-9]{8}$", phone):
        print("Invalid Egyptian phone number.")
        return

    user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone
    }

    users.append(user)
    save_data(USERS_FILE, users)
    print("Registration successful")


def login():
    try:
        users = load_data(USERS_FILE)
    except FileNotFoundError:
        print("No users registered yet.")
        return None

    email = input("Email: ")
    password = input("Password: ")

    for user in users:
        if user["email"] == email and user["password"] == password:
            print(f"Welcome {user['first_name']} ")
            return user

    print("Invalid credentials ")
    return None


# ---------- Projects ----------

def create_project(user):
    projects = load_data(PROJECTS_FILE)

    start = input("Start date (YYYY-MM-DD): ")
    end = input("End date (YYYY-MM-DD): ")

    try:
        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")
        if start_date >= end_date:
            print("Start date must be before end date.")
            return
    except ValueError:
        print("Invalid date format.")
        return
    
    target = input("Total target (EGP): ")
    if not target.isdigit() or int(target) <= 0:
        print("Target must be a positive number.")
        return

    project = {
        "owner": user["email"],
        "title": input("Title: "),
        "details": input("Details: "),
        "target": target,
        "start": start,
        "end": end
    }

    projects.append(project)
    save_data(PROJECTS_FILE, projects)
    print("Project created ")


def view_projects():
    projects = load_data(PROJECTS_FILE)
    if not projects:
        print("No projects found.")
        return

    for i, p in enumerate(projects, 1):
        print(f"""
                {i}. {p['title']}
                Target: {p['target']} EGP
                Start: {p['start']} | End: {p['end']}
            """)


def delete_project(user):
    projects = load_data(PROJECTS_FILE)
    my_projects = []
    for p in projects:
        if p["owner"] == user["email"]:
            my_projects.append(p)

    if not my_projects:
        print("No projects to delete.")
        return

    for i, p in enumerate(my_projects, 1):
        print(f"{i}. {p['title']}")

    choice = input("Select project number: ")
    try:
        choice = int(choice) - 1
    except:
        print("Enter a valid project numebr ")
    else:
        projects.remove(my_projects[choice])
        save_data(PROJECTS_FILE, projects)
        print("Project deleted ")

def search_by_date():
    projects = load_data(PROJECTS_FILE)
    date = input("Enter date (YYYY-MM-DD): ")

    for p in projects:
        if p["start"] <= date and date <= p["end"]:
            print(f"{p['title']} (Active)")