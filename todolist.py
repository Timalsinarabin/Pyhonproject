print("==================================")
print("          To Do List  ")
print("==================================")
print("1. Create a new task")
print("2. Task completed")
print("3. list all tasks")
print("4. Exit")
choice=0
new_task=[]

while choice!=5:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        task= input("Enter a new task: ")
        new_task.append(task)
        print(f"Added task: {task}")

    elif choice == 2:
        completed_task =input("Enter a completed task: ")
        print(f"Completed task: {completed_task}")
        if completed_task in new_task:
            new_task.remove(completed_task)
            print(f"Task '{completed_task}' removed from the list")
        else:
            print(f"Task '{completed_task}' not found in the list")
    
    elif choice == 3:
        print("ALL tasks:")
        i=0
        for task in new_task:
            print(f"{i+1}. {task}")
            i+=1
    
    else:
        print("Please choose appropiate number!")
  