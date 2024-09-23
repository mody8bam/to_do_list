import os

message="""
1- add task to list
2- mark task as complete
3- view tasks
4- quit
"""

tasks=[]


def add_task():
    #get task 
    task=input('Enter your task: ')
    if task:
        
        #define task status
        task_info={'task':task,'completed':False }
        
        #add task to the list of tasks
        tasks.append(task_info)
        
        print('your task is added successfuly to the list. ')
        for t in tasks:
            print(t['task'],' : ',t['completed'])
    else :
        print('enter task please ')
        add_task()
    
    

def mark_task_complete():
    #get list of task incompleted
    inc_task= [task for task in tasks if task['completed'] == False ]
    
    #show them to user
    print("\n tasks of incompleted yet: \n")
    if inc_task:
        
        for i,task in enumerate(inc_task):
            print(f"{i+1}- {task['task']}")
            
        #get the task from user
        j=int(input('which task to mark as completed: '))-1
        
        # mark the task 
        inc_task[j]['completed']=True
        '''
        nameOfTask=inc_task[j]['task']
        for t in tasks:
            if t['task']== nameOfTask:
                t['completed']=True
        print(tasks)
        '''
    else :
        print('no task to complete.. ')
    
    

def view_task():
    
    if tasks:
        print('your tasks : ')
        for i,task in enumerate(tasks,start=1):
            print( f" {i}- {task['task']}  {'📌' if task['completed']==False else '✔'}  " )
    else:
        print("no task noted... ")
        




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



        



