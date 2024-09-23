

message="""
1- add task to list
2- mark task as complete
3- view tasks
4- quit
"""

task=[]


def add_task():
    pass

def mark_task_complete():
    pass

def view_task():
    pass




while True :
    print(message)
    choice = input('enter your choice:')
    
    if choice == '1':
        add_task()
    elif choice == '2':
        mark_task_complete()
    elif choice =='3':
        view_task()
    elif choice =='4':
        break
    else :
        print('invalid choice, please enter a number between 1 to 4. ')



        



