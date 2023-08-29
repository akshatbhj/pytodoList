import tkinter as tk
from tkinter import messagebox

# Function to add a new task to the list


def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove a selected task from the list


def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        pass


app = tk.Tk()
app.title("To-Do List App")
app.geometry("300x350")


task_entry = tk.Entry(app, font=("Arial", 12))
task_entry.pack(pady=10, padx=20, fill=tk.X)


add_button = tk.Button(app, text="Add", command=add_task, font=("Arial", 12))
add_button.pack(pady=5, padx=20, fill=tk.X)


remove_button = tk.Button(
    app, text="Remove", command=remove_task, font=("Arial", 12))
remove_button.pack(pady=5, padx=20, fill=tk.X)


task_listbox = tk.Listbox(app, selectmode=tk.SINGLE, font=("Arial", 12))
task_listbox.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)


scrollbar = tk.Scrollbar(task_listbox)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)


app.mainloop()
