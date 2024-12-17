import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")

# Listbox to display tasks
task_listbox = tk.Listbox(root, height=15, width=50, selectmode=tk.SINGLE)
task_listbox.pack(pady=20)

# Entry widget to input tasks
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)  # Clear the entry field
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

# Function to delete the selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()  # Get the index of the selected task
        task_listbox.delete(selected_task_index)  # Delete the selected task
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete!")

# Function to clear all tasks
def clear_all_tasks():
    task_listbox.delete(0, tk.END)  # Delete all tasks in the listbox

# Buttons to control tasks
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All", width=20, command=clear_all_tasks)
clear_button.pack(pady=5)

# Run the main event loop
root.mainloop()
