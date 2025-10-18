# To-Do List System (TDD) - Projeto para disciplina 'Implementação e Teste de Software'

**Aluno:** Lucca Rocha Oliveira  
**Disciplina:** Projeto Implementação e Teste de Software - Prof. Dacio Machado

---

## Visão Geral

Projeto simples de uma _To-Do List_ (lista de tarefas) desenvolvido seguindo a abordagem **TDD (Test-Driven Development)**.
O objetivo é implementar funcionalidades básicas de CRUD (Create, Read, Update, Delete) para tarefas e controle de status ("em andamento" / "concluída"), com testes automatizados cobrindo os requisitos do enunciado.

## Estrutura do repositório

```
todo_tdd_repo/
├── todo.py              # Implementação da aplicação (classe ToDoList)
├── tests/
│   └── test_todo.py     # Testes unitários com unittest (TEST-01 a TEST-10)
├── README.md            # Este arquivo
├── .gitignore
└── requirements.txt     # Dependências (vazio - apenas python padrão)
```

## Requisitos funcionais (resumo)

- **REQ-01:** Adicionar tarefa (nome + descrição). Nome não pode ser vazio.
- **REQ-02:** Marcar tarefa como concluída.
- **REQ-03:** Marcar tarefa como em andamento.
- **REQ-04:** Editar nome e descrição de tarefa existente.
- **REQ-05:** Excluir tarefa.

## Matriz de rastreabilidade (REQ ↔ TEST)

- REQ-01 -> TEST-01, TEST-02
- REQ-02 -> TEST-03, TEST-04
- REQ-03 -> TEST-05, TEST-06
- REQ-04 -> TEST-07, TEST-08
- REQ-05 -> TEST-09, TEST-10

## Como executar os testes

1. Clone este repositório ou baixe o zip.
2. Entre na pasta do projeto:
   ```bash
   cd todo_tdd_repo
   ```
3. Execute os testes:
   ```bash
   python -m unittest discover -v
   ```
   ou
   ```bash
   python -m unittest tests/test_todo.py -v
   ```

## Decisões de projeto e observações

- Identificação de tarefas por **nome** (conforme enunciado e testes). Se preferir, posso adaptar para IDs únicos incrementais (recomendado para produção).
- Para situações inválidas (nome vazio, tarefa inexistente, remarcar concluída etc.) a implementação levanta `ValueError`. Isso facilita a verificação nos testes (com `assertRaises`).
- Permiti nomes duplicados na implementação. Se quiser, adiciono verificação para proibir duplicatas.

## TDD / Ciclo aplicado

Para cada requisito foi seguido o ciclo:

- **Red:** escrever o teste correspondente (falha inicialmente).
- **Green:** escrever o código mínimo para passar no teste.
- **Refactor:** melhorar clareza e organização sem alterar comportamento.

## Arquivos principais

- `todo.py`: contém a classe `ToDoList` com métodos:
  - `adicionar_tarefa(nome, descricao)`
  - `marcar_como_concluida(nome)`
  - `marcar_como_em_andamento(nome)`
  - `editar_tarefa(nome_atual, novo_nome=None, nova_descricao=None)`
  - `excluir_tarefa(nome)`
- `tests/test_todo.py`: contém 10 testes unitários cobrindo todos os cenários pedidos pelo enunciado.
