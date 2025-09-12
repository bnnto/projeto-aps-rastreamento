import random
import time

class JogoAdivinhacao:
    def _init_(self, jogador):
        self.jogador = jogador
        self.pontuacao = 0

    def jogar(self):
        print(f"\nBem-vindo, {self.jogador}! Vamos jogar 🎲")
        for rodada in range(1, 6):  # 5 rodadas
            print(f"\nRodada {rodada}/5")
            numero_secreto = random.randint(1, 20)
            tentativas = 3

            while tentativas > 0:
                try:
                    chute = int(input(f"Você tem {tentativas} tentativas. Digite um número entre 1 e 20: "))
                except ValueError:
                    print("⚠ Entrada inválida! Digite apenas números.")
                    continue

                if chute == numero_secreto:
                    print("🎉 Parabéns, você acertou!")
                    self.pontuacao += 10
                    break
                elif chute < numero_secreto:
                    print("📉 O número secreto é maior.")
                else:
                    print("📈 O número secreto é menor.")

                tentativas -= 1

            if tentativas == 0:
                print(f"❌ Acabaram as tentativas! O número era {numero_secreto}.")

        print(f"\nFim do jogo! 🏆 Sua pontuação final foi: {self.pontuacao}")

def ranking():
    print("\n===== Ranking dos Jogadores =====")
    jogadores = {
        "Alice": 30,
        "Bento": 20,
        "Carlos": 50,
        "Duda": 40
    }
    for nome, pontos in sorted(jogadores.items(), key=lambda x: x[1], reverse=True):
        print(f"{nome}: {pontos} pontos")

if _name_ == "_main_":
    nome = input("Digite seu nome: ")
    jogo = JogoAdivinhacao(nome)
    jogo.jogar()
    ranking()
]
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
