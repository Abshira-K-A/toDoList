tasks = []
n = 0
def addTask(): 
        task = input("write a new task: ")
        tasks.append(task)
        print(f"your new task '{task}' added succesfully")

def listTask():
    if not tasks:
        print("There are no tasks currently. Please add a new task.  ")
    else:
        print(f"your currect tasks are...: '{tasks}'")
        for i, task in enumerate(tasks):
            print(f"Task #{i}:{task}") 
            
    
def deleteTask():
    listTask()
    if not tasks:
        return
    try:
        Delete_task = int(input("enter index  you want to delete: "))
        if  Delete_task >= 0 and Delete_task < len(tasks):
            tasks.pop(Delete_task)
            print(f"The task {Delete_task} has been removed.")
            print(f"\nRemaining tasks : {tasks}")
        else:
            print("Invalid")
    except:
        print("invalid....")

    
print("Welcome to  your To Do List ")

while True:
    print("\n please select the options: ")
    print("\n1. Add task")
    print("\n2. List tasks")
    print("\n3. Delete tasks")
    print("\n4. Quit")
    
    choice =int(input("Enter your choice: "))
    


    if choice == 1:
        addTask()
    elif choice == 2:
        listTask()
    elif choice == 3:
        deleteTask()
    elif choice == 4 :
        print("See you soon.....")
    else:
        print("invalid Input, try a valid one ")