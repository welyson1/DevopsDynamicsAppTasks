### Código base
Onde tudo começa!
```Python
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
```

### Tarefa 1
Primeira correção! O cliente disse para o PO que é muito chato ter que confirmar se realmente quer sair do Software quando clica no X.
Então... Dev Front
Remova toda a função def `on_close(self):` do código base.
Remova a linha de código `self.master.protocol("WM_DELETE_WINDOW", self.on_close)`

### Tarefa 2
Doc, a encarregada da documentação, recebeu a tarefa de revisar e atualizar a documentação da aplicação depois da implementação. Ao revisar o material existente, ela notou uma seção que descrevia detalhadamente a caixa de diálogo de fechamento, mas, ao ouvir do Dev Front: "Amigoo, eu só removi uma caixa de diálogo haha, tarefa mais fácil da minha vida haha", ela decidiu simplificar e remover essa parte da documentação.

No arquivo `Doc.md` remova o bloco de texto que fala sobre a função de fechamento

### Tarefa 3
QA, o experiente membro da equipe, recebeu a missão de testar a aplicação antes de colocá-la em produção. Confiante em sua habilidade, ele recordou as palavras do Dev Front: "Amigoo, eu só removi uma caixa de diálogo haha, tarefa mais fácil da minha vida haha". Com essa garantia, Ricardo deu apenas uma rápida olhada no código do GitHub e, confiante, enviou a aplicação para produção.

No GitHub somente de um marge na branch de produção

### Tarefa 4
Funcionalidade implementada, agora o cliente testa a aplicação.
Vixeee...

### Tarefa 5
Dev Back deve...
Ajuste o código para salvar as tarefas adicionando a linha `self.save_tasks_to_json()` dentro do `if` da função `add_task()`

### Tarefa 6
O QA deve..
Implementar um arquivo de teste unitario baseado no código existente adaptado abaixo:
```python
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

    def add_task(self):
        task_name = simpledialog.askstring("Adicionar Tarefa", "Digite o nome da tarefa:")
        if task_name:
            self.tasks.append({"name": task_name})            
            self.save_tasks_to_json()
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

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
```

Crie um arquivo chamado `test_task_manager.py`

```python
import unittest
from unittest.mock import patch, Mock
import os

from tkinter import Tk
from task_manager import TaskManager  # Substitua 'your_main_script' pelo nome do seu script principal

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.app = TaskManager(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('task_manager.simpledialog.askstring', return_value="Test Task")
    def test_add_task(self, mock_askstring):
        # Verifica se o arquivo 'tasks.json' não existe inicialmente
        self.assertFalse(os.path.exists("tasks.json"))

        # Chama a função add_task
        self.app.add_task()

        # Verifica se o arquivo 'tasks.json' foi criado após a chamada da função add_task
        self.assertTrue(os.path.exists("tasks.json"))

        # Carrega as tarefas do arquivo 'tasks.json'
        self.app.load_tasks_from_json()

        # Verifica se a tarefa adicionada está presente na lista de tarefas
        self.assertIn({"name": "Test Task"}, self.app.tasks)

if __name__ == "__main__":
    unittest.main()

```

---

### Tarefa 7
Novo membro na equipe... DevOps
Agora vamos implementar o arquivo YAML para executar o teste, gerar a documentação automaticamente e gerar um aarquivo exe.

### Tarefa 8
O Sec itentifica a falha de segurança no acesso as tarefas e pede a implementação de uma senha ao abrir o software para poder manipular o arquivo json com as tarefas.