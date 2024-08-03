import json

tasks = []


def display_list():
    if not tasks:
        print('You currently have no tasks.')
    else:
        print("Here are your current tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index+1}. {task}")


def add_to_list():
    description = input("Enter a description: ")

    priority = input("Enter a priority: L/M/H ").capitalize()
    if priority == "L":
        priority = "Low"
    elif priority == "M":
        priority = "Medium"
    elif priority == "H":
        priority = "High"
    elif priority == "Skip":
        print("_")
    else:
        "Please choose a valid priority between (L/M/H) or 'skip'"

    due_date = input("Enter a due date (YYYY-MM-DD): ")

    task = {
        'description': description,
        'priority': priority,
        'due_date': due_date
    }
    tasks.append(task)
    print(f"Task'{description}' has been added to the list.")


def remove_from_list():
    display_list()
    try:
        removetask = int(input("What # would you like to remove from the list: ")) - 1
        if removetask >= 0 and removetask < len(tasks):
            task = tasks.pop(removetask)
            print(f"Task'{removetask + 1}' has been removed from the list.")
        else:
            print(f"Task #{removetask + 1} is not in the list.")
    except ValueError:
        print("Please enter a valid number.")

def save_tasks(filename='task.json'):
     with open(filename, 'w') as f:
         json.dump(tasks, f, indent=4)

def load_tasks(filename='task.json'):
    global tasks
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
    except json.JSONDecodeError:
        tasks = []


if __name__ == '__main__':
    print("Hello User,")
    task_decision = input("Do you have an existing to-do list? ")
    task_decision = task_decision.lower()

    if task_decision == "yes":
        load_tasks()

    while True:
        print("This is your to-do list. What would you like to do?")
        print("---------------------------------------------------")
        print("1. Add task")
        print("2. Remove task")
        print("3. Display list")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_to_list()
            save_tasks()
        elif choice == "2":
            remove_from_list()
            save_tasks()
        elif choice == "3":
            display_list()
        elif choice == "4":
            save_tasks()
            break
        else:
           print("Invalid choice")
        print("Goodbye\n")
