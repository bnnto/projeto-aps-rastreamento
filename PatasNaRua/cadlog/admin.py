class ToDoList:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, tarefa):
        self.tarefas.append({"nome": tarefa, "feito": False})
        print(f"✅ Tarefa '{tarefa}' adicionada.")

    def listar(self):
        if not self.tarefas:
            print("📭 Nenhuma tarefa ainda.")
        for i, t in enumerate(self.tarefas, 1):
            status = "✔️" if t["feito"] else "❌"
            print(f"{i}. {t['nome']} - {status}")

    def concluir(self, indice):
        if 0 < indice <= len(self.tarefas):
            self.tarefas[indice-1]["feito"] = True
            print("🎉 Tarefa concluída!")
        else:
            print("⚠️ Índice inválido.")

    def remover(self, indice):
        if 0 < indice <= len(self.tarefas):
            removida = self.tarefas.pop(indice-1)
            print(f"🗑️ Tarefa '{removida['nome']}' removida.")
        else:
            print("⚠️ Índice inválido.")

def menu():
    lista = ToDoList
