# todo.py
"""Implementação simples de ToDoList para atividade TDD.

Cada tarefa é representada por um dicionário:
{
    "nome": str,
    "descricao": str,
    "status": "em andamento" | "concluída"
}
"""

class ToDoList:
    def __init__(self):
        self.tarefas = []

    def _buscar_indice_por_nome(self, nome):
        for idx, t in enumerate(self.tarefas):
            if t["nome"] == nome:
                return idx
        return None

    def adicionar_tarefa(self, nome, descricao):
        if not nome or not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Nome da tarefa inválido.")
        tarefa = {
            "nome": nome,
            "descricao": descricao or "",
            "status": "em andamento"
        }
        self.tarefas.append(tarefa)
        return tarefa

    def marcar_como_concluida(self, nome):
        idx = self._buscar_indice_por_nome(nome)
        if idx is None:
            raise ValueError("Tarefa não encontrada.")
        tarefa = self.tarefas[idx]
        if tarefa["status"] == "concluída":
            raise ValueError("Tarefa já está marcada como concluída.")
        tarefa["status"] = "concluída"
        return tarefa

    def marcar_como_em_andamento(self, nome):
        idx = self._buscar_indice_por_nome(nome)
        if idx is None:
            raise ValueError("Tarefa não encontrada.")
        tarefa = self.tarefas[idx]
        if tarefa["status"] == "concluída":
            raise ValueError("Não é possível marcar como 'em andamento' uma tarefa já concluída.")
        tarefa["status"] = "em andamento"
        return tarefa

    def editar_tarefa(self, nome_atual, novo_nome=None, nova_descricao=None):
        idx = self._buscar_indice_por_nome(nome_atual)
        if idx is None:
            raise ValueError("Tarefa não encontrada.")
        if novo_nome is not None:
            if not isinstance(novo_nome, str) or novo_nome.strip() == "":
                raise ValueError("Novo nome inválido.")
            self.tarefas[idx]["nome"] = novo_nome
        if nova_descricao is not None:
            self.tarefas[idx]["descricao"] = nova_descricao
        return self.tarefas[idx]

    def excluir_tarefa(self, nome):
        idx = self._buscar_indice_por_nome(nome)
        if idx is None:
            raise ValueError("Tarefa não encontrada.")
        tarefa = self.tarefas.pop(idx)
        return tarefa
