# TO-DO LIST APPLICATION

import tkinter as tk

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def delete_task():
    try:
        index = listbox_tasks.curselection()
        listbox_tasks.delete(index)
    except:
        label_error.config(text="Please select a task to delete.")

# GUI setup
root = tk.Tk()
root.title("To-Do List")

label_task = tk.Label(root, text="Enter Task:")
label_task.pack()

entry_task = tk.Entry(root)
entry_task.pack()

button_add = tk.Button(root, text="Add Task", command=add_task)
button_add.pack()

listbox_tasks = tk.Listbox(root, height=10, width=50)
listbox_tasks.pack()

button_delete = tk.Button(root, text="Delete Task", command=delete_task)
button_delete.pack()

label_error = tk.Label(root, text="", fg="red")
label_error.pack()

root.mainloop()