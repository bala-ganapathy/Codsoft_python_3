import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task:
            tasks[selected_task_index] = new_task
            update_task_list()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to update.")

def clear_tasks():
    if messagebox.askyesno("Clear Tasks", "Are you sure you want to clear all tasks?"):
        tasks.clear()
        update_task_list()

task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=20, pady=10)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

task_listbox = tk.Listbox(root, height=10, width=50)
task_listbox.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

update_button = tk.Button(root, text="Update Task", width=15, command=update_task)
update_button.grid(row=2, column=0, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.grid(row=2, column=1, padx=10, pady=10)

clear_button = tk.Button(root, text="Clear Tasks", width=15, command=clear_tasks)
clear_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
