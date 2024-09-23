import json
import os

# File to store tasks
TASKS_FILE = 'task.json'

# Check if tasks.json exists and load it, otherwise start with a default task list
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    else:
        return [
            {'task': 'quran', 'completed': True},
            {'task': 'salah', 'completed': True},
            {'task': 'study', 'completed': False},
            {'task': 'exercise', 'completed': True},
            {'task': 'sleep', 'completed': False},
            {'task': 'visit hamada', 'completed': True},
        ]

# Save tasks to tasks.json
def save_tasks(tasks):
    try:
        with open('task.json', 'w') as file:
            json.dump(tasks, file, indent=4)
        print("Tasks saved to task.json")
    except Exception as e:
        print(f"Error saving tasks: {e}")


def main ():
    global tasks
    tasks = load_tasks()  # Load tasks from the file
    
    message="""
     1- add task to list
     2- mark task as complete
     3- view tasks
     4- quit
     """
    
    while True :
        print(message)
        choice = input('enter your choice:')
        
        if choice == '1':
            add_task()
            
        elif choice == '2':
            mark_task_complete()
        elif choice =='3':
            view_task(tasks)
        elif choice =='4':
            save_tasks(tasks)
            break
        else :
            print('invalid choice, please enter a number between 1 to 4. ')



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
        try :
            j=int(input('which task to mark as completed: '))-1
            if j<1 or j>len(inc_task):
               print("invalid task number")
               return 
        except ValueError:
            print('invalid value, please enter showing index upbove ' )
        except IndexError:
            print('out of range value ')  
            
              
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
    
     

def view_task(tasks):
    
    if tasks:
        print('your tasks : ')
        for i,task in enumerate(tasks,start=1):
            print( f" {i}- {task['task']}  {'📌' if task['completed']==False else '✔'}  " )
    else:
        print("no task noted... ")
        


        
# print("the next line will print the value of __name__ ")
# print(__name__)
if __name__ == '__main__':
    main()


