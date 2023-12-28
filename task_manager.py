### Welyson que fez
import tkinter as tk
from tkinter import simpledialog, messagebox
import json

class TaskManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciador de Tarefas")

        self.tasks = []

        self.load_tasks_from_json()

        self.task_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, height=10, width=50)
        self.task_listbox.pack(pady=10)

        self.refresh_task_listbox()

        self.add_button = tk.Button(self.master, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self.master, text="Remover Tarefa", command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

    def add_task(self):
        task_name = simpledialog.askstring("Adicionar Tarefa", "Digite o nome da tarefa:")
        if task_name:
            self.tasks.append({"name": task_name})
            self.refresh_task_listbox()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            del self.tasks[task_index]
            self.save_tasks_to_json()
            self.refresh_task_listbox()

    def refresh_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task["name"])

    def save_tasks_to_json(self):
        with open("tasks.json", "w") as json_file:
            json.dump(self.tasks, json_file)

    def load_tasks_from_json(self):
        try:
            with open("tasks.json", "r") as json_file:
                self.tasks = json.load(json_file)
        except FileNotFoundError:
            pass

    def on_close(self):
        if messagebox.askokcancel("Fechar", "Deseja realmente fechar o aplicativo?"):
            self.save_tasks_to_json()
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()