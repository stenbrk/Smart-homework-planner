from datetime import datetime, timedelta

tasks = []

def add_task():
    name = input("Task name: ")
    deadline_str = input("Deadline (YYYY-MM-DD): ")
    deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
    tasks.append({"name": name, "deadline": deadline})

def generate_plan():
    today = datetime.today()
    tasks.sort(key=lambda x: x["deadline"])

    print("\n📅 Your Homework Plan:\n")

    for task in tasks:
        days_left = (task["deadline"] - today).days
        if days_left <= 0:
            print(f"⚠️ {task['name']} is overdue!")
        else:
            print(f"{task['name']} → work on it within {days_left} days")

def main():
    while True:
        print("\n1. Add task")
        print("2. Generate plan")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            generate_plan()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()