lst=[]
ch=0
while ch!=6:
    print("MENU:-\n1. Create\n2. Update\n3. Track\n4. Delete\n5. View all tasks\n6. Exit")
    ch=int(input("Enter your choice: "))
    print("\n")
    if ch==1:
        lst.append(input("Enter new task: "))
    elif ch==2:
        task=input("Enter the task you want to update: ")
        if task in lst:
            task2=input("Enter the updated task: ")
            lst[lst.index(task)]=task2
        else:
            print("Task not found!")
    elif ch==3:
        task=input("Enter the task you want to track: ")
        if task in lst:
            print("Task found at location",lst.index(task)+1,"in the list")
        else:
            print("Task not found!")
    elif ch==4:
        ind=int(input("Enter the task no. you want to delete: "))
        if lst[ind-1] in lst:
            lst.pop(ind-1)
        else:
            print("Task not found!")
    elif ch==5:
        if len(lst)==0:
            print("No tasks found!")
        for i in range(len(lst)):
            print(i+1,". ",lst[i],sep="")
    elif ch==6:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
    print("\n")
