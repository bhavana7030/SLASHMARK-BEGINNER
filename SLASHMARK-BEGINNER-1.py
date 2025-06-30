#To -Do list
tasks=[]
def display():
    if not tasks:
        print("empty")
    else:

        print("Tasks are :")
        for i,task in enumerate(tasks,start=1):
            status="Done" if task["completed"] else "not done"
            print(f"{i-1} {task['task']} ({status})")
def addtasks():
    t=input("Enter a task to add:")
    task={"task":t,"completed":False}
    tasks.append(task)
def markcomplete():
    print("task to be completed")
    e=int(input("Enter number  of the task:"))
    if 1<=e<=len(tasks):
        tasks[e-1]["completed"]=True
    else:
        print("Invalid task number")
def removingtask():
    rmv=int(input("Enter a task number to remove:"))
    print("removed task is ",tasks.pop(rmv))

print("To-Do List Application Instructions"
          "1. Display To-Do List:"
          "- Enter '1' to display your current to-do list. It will show the tasks and their completion status."
          "2. Add a Task:"
          "- Enter '2' to add a new task to your to-do list. You'll be prompted to enter the task's name."
          "3. Mark a Task as Completed:"
          "- Enter '3' to mark a task as completed. You'll see the current list of tasks, and you'll be asked to enter the task number you want to mark as completed."
          "4. Remove a Task:"
          "- Enter '4' to remove a task from your to-do list. You'll see the current list of tasks and will be prompted to enter the task number you want to remove."
          "5. Quit:"
          " - Enter '5' to exit the application.")
while(True):
    choice=int(input("Enter number from ranging 1 to 5:"))
    if choice==1:
        print(" items")
        display()
    elif choice==2:
        print("Adding a task")
        addtasks()
    elif choice==3:
        print("Mark completed")
        markcomplete()
    elif choice==4:
        print("Removing element from tasks")
        removingtask()
    elif choice==5:
        break
    else:
        print("Sorry!!!Enter a valid choice")
