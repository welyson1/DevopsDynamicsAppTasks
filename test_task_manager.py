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
