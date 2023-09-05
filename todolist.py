import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.configure(bg="#3cdfff")

        self.tasks = []

        self.dark_mode = False

        self.create_widgets()
        self.load_tasks()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="To-Do List", font=("Times New Roman", 20))
        self.title_label.pack(pady=10)

        self.task_input = tk.Entry(self.root, font=("Helvetica", 14))
        self.task_input.pack(fill=tk.BOTH, padx=20, pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, bg="black", fg="white")
        self.add_button.pack(fill=tk.BOTH, padx=20, pady=5)

        self.tasks_frame = tk.Frame(self.root, bg="white")
        self.tasks_frame.pack(fill=tk.BOTH, padx=20)

        self.dark_mode_button = tk.Button(self.root, text="Dark Mode", command=self.toggle_dark_mode, bg="black", fg="white")
        self.dark_mode_button.pack(fill=tk.BOTH, padx=20, pady=10)

        self.save_button = tk.Button(self.root, text="Save Tasks", command=self.save_tasks, bg="black", fg="white")
        self.save_button.pack(fill=tk.BOTH, padx=20, pady=5)

        self.load_button = tk.Button(self.root, text="Load Tasks", command=self.load_tasks, bg="black", fg="white")
        self.load_button.pack(fill=tk.BOTH, padx=20, pady=5)

        self.sort_button = tk.Button(self.root, text="Sort Alphabetically", command=self.sort_tasks, bg="black", fg="white")
        self.sort_button.pack(fill=tk.BOTH, padx=20, pady=5)

    def add_task(self):
        task_text = self.task_input.get().strip()
        if task_text:
            self.tasks.append(task_text)
            self.update_task_list()
            self.task_input.delete(0, tk.END)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.update_task_list()

    def toggle_task_status(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = "✔ " + self.tasks[index] if not self.tasks[index].startswith("✔ ") else self.tasks[index][2:]
            self.update_task_list()

    def edit_task(self, index):
        if 0 <= index < len(self.tasks):
            edited_text = self.tasks[index]
            edited_text = edited_text[2:] if edited_text.startswith("✔ ") else edited_text  # Remove completion mark if present
            new_text = tk.simpledialog.askstring("Edit Task", "Edit task text:", initialvalue=edited_text)
            if new_text is not None:
                self.tasks[index] = "✔ " + new_text if self.tasks[index].startswith("✔ ") else new_text
                self.update_task_list()

    def update_task_list(self):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        for index, task in enumerate(self.tasks):
            task_label = tk.Label(self.tasks_frame, text=task, bg="white", anchor="w")
            task_label.pack(fill=tk.BOTH, padx=5, pady=2)

            delete_button = tk.Button(self.tasks_frame, text="Delete", command=lambda i=index: self.delete_task(i), bg="#F44336", fg="white")
            delete_button.pack(fill=tk.BOTH, padx=5, pady=2)

            status_button = tk.Button(self.tasks_frame, text="Complete", command=lambda i=index: self.toggle_task_status(i), bg="#4CAF50", fg="white")
            status_button.pack(fill=tk.BOTH, padx=5, pady=2)

            edit_button = tk.Button(self.tasks_frame, text="Edit", command=lambda i=index: self.edit_task(i), bg="#2196F3", fg="white")
            edit_button.pack(fill=tk.BOTH, padx=5, pady=2)

    def toggle_dark_mode(self):
        if self.dark_mode:
            self.root.configure(bg="white")
            self.title_label.configure(bg="white", fg="black")
            self.tasks_frame.configure(bg="white")
            self.dark_mode_button.configure(text="Dark Mode", bg="black", fg="white")
            self.dark_mode = False
        else:
            self.root.configure(bg="black")
            self.title_label.configure(bg="black", fg="white")
            self.tasks_frame.configure(bg="black")
            self.dark_mode_button.configure(text="Light Mode", bg="white", fg="black")
            self.dark_mode = True

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

        messagebox.showinfo("Save Tasks", "Tasks have been saved.")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
            self.update_task_list()
            messagebox.showinfo("Load Tasks", "Tasks have been loaded.")
        except FileNotFoundError:
            messagebox.showinfo("Load Tasks", "No saved tasks found.")

    def sort_tasks(self):
        self.tasks.sort()
        self.update_task_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoList(root)
    root.mainloop()
