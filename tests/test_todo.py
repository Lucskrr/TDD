# tests/test_todo.py
import unittest
from todo import ToDoList

class TestToDoList(unittest.TestCase):
    # TEST-01: Verificar se uma nova tarefa é criada corretamente quando fornecidos nome e descrição válidos.
    def test_adicionar_tarefa_valida(self):
        todo = ToDoList()
        todo.adicionar_tarefa("Estudar", "Estudar Python TDD")
        self.assertEqual(len(todo.tarefas), 1)
        tarefa = todo.tarefas[0]
        self.assertEqual(tarefa["nome"], "Estudar")
        self.assertEqual(tarefa["descricao"], "Estudar Python TDD")
        self.assertEqual(tarefa["status"], "em andamento")

    # TEST-02: Verificar se o sistema rejeita a criação de tarefa sem nome (ou com nome vazio).
    def test_adicionar_tarefa_sem_nome_deve_levantar_erro(self):
        todo = ToDoList()
        with self.assertRaises(ValueError):
            todo.adicionar_tarefa("", "Sem nome")

        with self.assertRaises(ValueError):
            todo.adicionar_tarefa(None, "Nome None")

        with self.assertRaises(ValueError):
            todo.adicionar_tarefa("   ", "Apenas espaços")

    # TEST-03: Verificar se, ao marcar uma tarefa como concluída, seu status é atualizado corretamente.
    def test_marcar_como_concluida_atualiza_status(self):
        todo = ToDoList()
        todo.adicionar_tarefa("Lavar o carro", "Lavar no domingo")
        todo.marcar_como_concluida("Lavar o carro")
        self.assertEqual(todo.tarefas[0]["status"], "concluída")

    # TEST-04: Verificar se tarefas já concluídas não podem ser marcadas novamente.
    def test_nao_pode_marcar_concluida_novamente(self):
        todo = ToDoList()
        todo.adicionar_tarefa("Pagar conta", "Luz e internet")
        todo.marcar_como_concluida("Pagar conta")
        with self.assertRaises(ValueError):
            todo.marcar_como_concluida("Pagar conta")

    # TEST-05: Verificar se uma tarefa pode ser marcada como “em andamento”.
    def test_marcar_como_em_andamento(self):
        todo = ToDoList()
        todo.adicionar_tarefa("Fazer exercício", "Corrida de 30 minutos")
        # já está 'em andamento' por padrão; chamar explicitamente para garantir comportamento
        todo.marcar_como_em_andamento("Fazer exercício")  # não deve levantar erro
        self.assertEqual(todo.tarefas[0]["status"], "em andamento")

    # TEST-06: Verificar se não é possível marcar como “em andamento” uma tarefa já concluída.
    def test_nao_pode_marcar_em_andamento_se_concluida(self):
        todo = ToDoList()
        todo.adicionar_tarefa("Enviar relatório", "Relatório mensal")
        todo.marcar_como_concluida("Enviar relatório")
        with self.assertRaises(ValueError):
            todo.marcar_como_em_andamento("Enviar relatório")

    # TEST-07: Verificar se é possível atualizar o nome e a descrição de uma tarefa existente.
    def test_editar_tarefa_existente(self):
        todo = ToDoList()
        todo.adicionar_tarefa("Comprar pão", "Padaria")
        todo.editar_tarefa("Comprar pão", novo_nome="Comprar pão e leite", nova_descricao="Padaria + supermercado")
        self.assertEqual(todo.tarefas[0]["nome"], "Comprar pão e leite")
        self.assertEqual(todo.tarefas[0]["descricao"], "Padaria + supermercado")

    # TEST-08: Verificar se o sistema impede edição de uma tarefa inexistente.
    def test_editar_tarefa_inexistente_deve_levantar_erro(self):
        todo = ToDoList()
        with self.assertRaises(ValueError):
            todo.editar_tarefa("Tarefa que não existe", novo_nome="Novo nome")

    # TEST-09: Verificar se uma tarefa pode ser removida da lista com sucesso.
    def test_excluir_tarefa_existente(self):
        todo = ToDoList()
        todo.adicionar_tarefa("Tarefa A", "Descricao A")
        self.assertEqual(len(todo.tarefas), 1)
        todo.excluir_tarefa("Tarefa A")
        self.assertEqual(len(todo.tarefas), 0)

    # TEST-10: Verificar se o sistema trata corretamente a tentativa de excluir uma tarefa inexistente.
    def test_excluir_tarefa_inexistente_deve_levantar_erro(self):
        todo = ToDoList()
        with self.assertRaises(ValueError):
            todo.excluir_tarefa("Inexistente")

if __name__ == "__main__":
    unittest.main()
