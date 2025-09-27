import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.config(bg="#f0f0f0")

tasks = []

# Functions
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        del tasks[index]
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def mark_done():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        task = tasks[index]
        if not task.startswith("✓ "):
            tasks[index] = "✓ " + task
            update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Widgets
title_label = tk.Label(root, text="📝 To-Do List", font=("Arial", 18), bg="#f0f0f0")
title_label.pack(pady=10)

task_entry = tk.Entry(root, font=("Arial", 14), width=25)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task, bg="#90ee90")
add_button.pack(pady=5)

done_button = tk.Button(root, text="Mark as Done", width=15, command=mark_done, bg="#add8e6")
done_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task, bg="#ff7f7f")
delete_button.pack(pady=5)

task_listbox = tk.Listbox(root, font=("Arial", 14), width=35, height=10)
task_listbox.pack(pady=10)

# Start the application
root.mainloop()
