import json
import tkinter as tk
from tkinter import messagebox

try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

except FileNotFoundError:
    tasks = []
    
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

root = tk.Tk()

root.title("To-Do List")
root.geometry("500x500")

# Task Title
title_label = tk.Label(root, text="Task Title:")
title_label.grid(row=0, column=0)   #.pack() gives vertucal box,grid.() gives horizontal

title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1)

# Priority
priority_label = tk.Label(root, text="Priority:")
priority_label.grid(row=1, column=0)

# priority_entry = tk.Entry(root)
# priority_entry.pack()

priority_var = tk.StringVar()

priority_var.set("Medium")
priority_menu = tk.OptionMenu(
    root,
    priority_var,
    "High",
    "Medium",
    "Low"
)

priority_menu.grid(row=1, column=1)


# Due Date
due_date_label = tk.Label(root, text="Due Date:")
due_date_label.grid(row=2, column=0)

due_date_entry = tk.Entry(root)
due_date_entry.grid(row=2, column=1)


def add_task():

    title = title_entry.get()
    priority = priority_var.get()
    due_date = due_date_entry.get()

    if not title:
     messagebox.showwarning(
        "Warning",
        "Title cannot be empty"
     )
     return
    
    task = {
        "title": title,
        "status": "Pending",
        "priority": priority,
        "due_date": due_date
    }

    tasks.append(task)

    save_tasks()

    task_listbox.insert(
        tk.END,
        f"{title} | Pending | {priority} | {due_date}"
    )
    messagebox.showinfo(
    "Success",
    "Task added successfully!"
    )
    title_entry.delete(0, tk.END)
    priority_var.set("Medium")
    due_date_entry.delete(0, tk.END)
    
    
def remove_task():
    selected = task_listbox.curselection()

    if not selected:
        messagebox.showwarning(
      "Warning",
      "No task selected"
     )
        return

    index = selected[0]

    task_listbox.delete(index)
    tasks.pop(index)   #list update
    save_tasks()    
    
    
def complete_task():

    selected = task_listbox.curselection()

    if not selected:
        messagebox.showwarning(
      "Warning",
      "No task selected"
     )
        return

    index = selected[0]

    tasks[index]["status"] = "Completed"

    save_tasks()

    task_listbox.delete(index)

    task_listbox.insert(
        index,
        f"{tasks[index]['title']} | "
        f"{tasks[index]['status']} | "
        f"{tasks[index]['priority']} | "
        f"{tasks[index]['due_date']}"
    )
    
def clear_all_tasks():
    
    answer = messagebox.askyesno(
    "Confirm",
    "Delete all tasks?"
)
    if answer:
     tasks.clear()

     save_tasks()

     task_listbox.delete(0, tk.END)
     
    
add_button = tk.Button(
    root,
    text="Add Task",
    command=add_task
)
add_button.grid(row=3, column=0, columnspan=2)

task_listbox = tk.Listbox(
    root,
    width=60,
    height=10
)
task_listbox.grid(row=4, column=0, columnspan=2)

complete_button = tk.Button(
    root,
    text="Complete Task",
    command=complete_task
)
complete_button.grid(row=5, column=0)

remove_button = tk.Button(
    root,
    text="Remove Task",
    command=remove_task
)
remove_button.grid(row=5, column=1)

clear_button = tk.Button(
    root,
    text="Clear All Tasks",
    command=clear_all_tasks
)
clear_button.grid(row=6, column=0, columnspan=2)


for task in tasks:

    task_listbox.insert(
        tk.END,
        f"{task['title']} | "
        f"{task['status']} | "
        f"{task['priority']} | "
        f"{task['due_date']}"
    )
      
root.mainloop()






#import json
# try:
#     with open("tasks.json","r")as file:
#         tasks = json.load(file)     #json->python files
#         #tasks=file.readlines()
#         #tasks=[task.strip() for task in tasks]   #
    
# except FileNotFoundError:
#    tasks=[]
   
   
# def save_tasks():
#     with open("tasks.json","w")as file:
#         json.dump(tasks, file, indent=4)    #python->json files
#         # for task in tasks:
#         #     file.write(task + "\n")
   
   
# while True:
    
#     print("\n--- TO DO LIST ---")
#     print("1. View Tasks")
#     print("2. Add Task")
#     print("3. Remove Task")
#     print("4. Mark Task Completed")
#     print("5. Clear all Tasks")
#     print("6. Exit")
    
#     choice=input("Enter your choice:")
    
#     if choice=='1':
        
#       if len(tasks)==0:
#           print("No tasks available")
          
#       else:
#           for i, task in enumerate(tasks,start=1):      #print(i,".",task)   
#             print(f"""
#             {i}. {task['title']}   
#             Status: {task['status']}
#             Priority: {task['priority']}
#             Due Date: {task['due_date']}
#             """)              #f-string is used to insert variable in string
#                               #""" are used  for multiple line string
            
#             # for i in range(len(tasks)):
#             # print(i+1,".",tasks[i])  
      
        
#     elif choice=='2':
        
#         title= input("Enter task title: ")
#         priority=input("Enter priority(High/Medium/Low)")
#         due_date=input("Enter due date: ")
        
#         task={
#             "title":title,
#             "status":"Pending",
#             "priority":priority,
#             "due_date":due_date            
#         }
        
#         tasks.append(task)
#         save_tasks()
#         print("New task added!")
        
#     elif choice =='3':
            
#         for i,task in enumerate(tasks,start=1):
#             print(i,".",task["title"])   
              
#         if len(tasks) == 0:
#             print("No tasks available to remove.")    
                 
#         else:
#             task_num=int(input("Enter the task number to remove:"))
#             if 1 <= task_num <= len(tasks):
#              tasks.pop(task_num-1)    #tasks.remove(tasks[task_num-1])   in pop,we write index 
#              save_tasks()
#             else:
#              print("Invalid task number!")
        
#     elif choice == '4':
        
#       task_num=int(input("Enter the task number to mark as completed:"))
#       if 1 <= task_num <= len(tasks):
#          tasks[task_num-1]["status"]="Completed"
#          save_tasks()
#       else:
#          print("Invalid task number!")
      
#     elif choice == '5':
        
#       tasks.clear()
#       save_tasks()
      
#       print("All tasks cleared!")
        
#     elif choice == '6':
        
#       print("Goodbye!")
#       break              
     