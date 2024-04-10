import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def update(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def __str__(self):
        return f"Description: {self.description},\nDue Date: {self.due_date},\nPriority: {self.priority}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def get_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None

    def display_task_list(self):
        if len(self.tasks) == 0:
            print("Task list is empty.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"Task {index + 1}:")
                print(task)
                print()

    def get_task_count(self):
        return len(self.tasks)


class CompletedTasks:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def get_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None

    def display_task_list(self):
        if len(self.tasks) == 0:
            print("Completed tasks list is empty.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"Task {index + 1}:")
                print(task)
                print()

    def get_task_count(self):
        return len(self.tasks)


class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List App")
        self.master.configure(bg="#f0f0f0")
        
        self.todo_list = TodoList()
        self.completed_tasks = CompletedTasks()

        self.heading_label = tk.Label(master, text="TODO LIST", bg="#000", fg="white", font=("Helvetica", 20))
        self.heading_label.pack(fill=tk.X, padx=10, pady=10)

        self.task_label = tk.Label(master, text="Task Description:", bg="#f0f0f0")
        self.task_label.pack(anchor=tk.W, padx=10, pady=5)
        self.task_entry = tk.Entry(master, bg="white")
        self.task_entry.pack(fill=tk.X, padx=10, pady=5)

        self.date_label = tk.Label(master, text="Due Date:", bg="#f0f0f0")
        self.date_label.pack(anchor=tk.W, padx=10, pady=5)
        self.date_entry = tk.Entry(master, bg="white")
        self.date_entry.pack(fill=tk.X, padx=10, pady=5)

        self.priority_label = tk.Label(master, text="Priority:", bg="#f0f0f0")
        self.priority_label.pack(anchor=tk.W, padx=10, pady=5)
        self.priority_entry = tk.Entry(master, bg="white")
        self.priority_entry.pack(fill=tk.X, padx=10, pady=5)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, bg="#008CBA", fg="white")
        self.add_button.pack(fill=tk.X, padx=10, pady=5)

        self.task_listbox = tk.Listbox(master, width=50, bg="white")
        self.task_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.display_tasks()

        self.complete_button = tk.Button(master, text="Mark as Completed", command=self.mark_completed, bg="#4CAF50", fg="white")
        self.complete_button.pack(fill=tk.X, padx=10, pady=5)

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task, bg="#f44336", fg="white")
        self.remove_button.pack(fill=tk.X, padx=10, pady=5)

    def add_task(self):
        description = self.task_entry.get()
        due_date = self.date_entry.get()
        priority = self.priority_entry.get()

        if description and due_date and priority:
            task = Task(description, due_date, priority)
            self.todo_list.add_task(task)
            self.display_tasks()
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = int(selected_index[0])
            task = self.todo_list.get_task(task_index)
            if task:
                self.todo_list.remove_task(task_index)
                self.completed_tasks.add_task(task)
                self.display_tasks()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = int(selected_index[0])
            self.todo_list.remove_task(task_index)
            self.display_tasks()

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            self.task_listbox.insert(tk.END, str(task))

    def clear_entries(self):
        self.task_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
