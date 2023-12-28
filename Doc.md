# Gerenciador de Tarefas em Tkinter

Este é um simples aplicativo de gerenciamento de tarefas implementado em Python usando a biblioteca Tkinter. Ele permite adicionar e remover tarefas, salvando os dados em um arquivo JSON para persistência.

## Classes e Funções

### `TaskManager`

#### `__init__(self, master)`

O construtor da classe `TaskManager` inicializa a interface gráfica e os elementos principais do aplicativo.

- `master`: A janela principal do Tkinter.

#### `add_task(self)`

Método para adicionar uma nova tarefa à lista de tarefas.

#### `remove_task(self)`

Método para remover a tarefa selecionada da lista de tarefas.

#### `refresh_task_listbox(self)`

Método para atualizar o conteúdo da caixa de listagem de tarefas.

#### `save_tasks_to_json(self)`

Método para salvar as tarefas em um arquivo JSON chamado "tasks.json".

#### `load_tasks_from_json(self)`

Método para carregar as tarefas a partir do arquivo JSON "tasks.json".

#### `on_close(self)`

Método chamado ao fechar a janela principal, perguntando ao usuário se deseja fechar o aplicativo.

### Execução Principal

```python
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
```

Verifica se o script está sendo executado diretamente e, nesse caso, inicia a aplicação Tkinter.

## Elementos Gráficos

- `task_listbox`: Caixa de listagem para exibir as tarefas.
- `add_button`: Botão para adicionar uma nova tarefa.
- `remove_button`: Botão para remover a tarefa selecionada.

## Fluxo de Funcionamento

1. A lista de tarefas é carregada a partir do arquivo JSON no início da execução.
2. A interface gráfica é criada com a lista de tarefas, botões e funcionalidades associadas.
3. O usuário pode adicionar tarefas usando o botão "Adicionar Tarefa".
4. O usuário pode remover tarefas selecionando uma da lista e clicando no botão "Remover Tarefa".
5. Quando a janela é fechada, o usuário é solicitado a confirmar antes de encerrar o aplicativo, salvando as tarefas no arquivo JSON.

## Persistência de Dados

As tarefas são salvas e carregadas de/para um arquivo JSON chamado "tasks.json". Se o arquivo não existir, o aplicativo continuará normalmente sem tarefas preexistentes.

---

**Observação:** Certifique-se de ter as bibliotecas `tkinter` e `json` instaladas para executar este código.