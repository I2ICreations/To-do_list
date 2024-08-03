tasks = []


def display_list():
    if not tasks:
        print('No tasks currently in list.')
    else:
        print("Here are your current tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def add_to_list():
    task = input("What would you like to add to the list: ")
    tasks.append(task)
    print(f"Task'{task}' has been added to the list.")


def remove_from_list():
    display_list()
    removetask = int(input("What # would you like to remove from the list: "))
    if removetask < len(tasks):
        tasks.pop(removetask)
        print(f"Task'{removetask}' has been removed from the list.")
    else:
        print(f"Task #{removetask} is not in the list.")


if __name__ == '__main__':
    print("Hello User,")
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
        elif choice == "2":
            remove_from_list()
        elif choice == "3":
            display_list()
        elif choice == "4":
            break
        else:
            print("Invalid choice")
        print("Goodbye\n")

