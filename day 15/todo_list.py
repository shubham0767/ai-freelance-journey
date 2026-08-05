print("=" * 40)
print("To-Do List")
print("=" * 40)

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        task = input("Enter Task: ")
        tasks.append(task)
        print("Task Added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No Tasks.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

    elif choice == "3":
        try:
            number = int(input("Enter Task Number: "))
            removed = tasks.pop(number - 1)
            print("Removed:", removed)

        except ValueError:
            print("Please enter a valid number.")

        except IndexError:
            print("Invalid Task Number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice.")