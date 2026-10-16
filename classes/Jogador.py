import random

class Jogador:
    def __init__(self, id_jogador, meu_tab, frota = []):
        self.id_jogador = id_jogador
        self.meu_tabuleiro = meu_tab
        self.ataques = []
        self.frota = frota
        self.frota_afundada = []

    def verificar_derrota(self):
        cont_PA, cont_E, cont_R, cont_S = 0, 0, 0, 0

        if len(self.frota) == 0:
            return True
        
        for e in self.frota:
            if e.tipo == "Porta-Aviões":
                cont_PA += 1
            elif e.tipo == "Encouraçados":
                count_E += 1
            elif e.tipo == "Rebocadores":
                count_R += 1
            elif e.tipo == "Submarinos":
                count_S += 1

        print(f"O jogador {self.id_jogador} ainda possui:")
        print(f"- {cont_PA} Porta-Aviões")
        print(f"- {count_E} Encouraçados")
        print(f"- {count_R} Rebocadores")
        print(f"- {count_S} Submarinos")
        return False

class Player(Jogador):
    def __init__(self, id_player, frota = []):
        super().__init__(frota)
        self.id_player = id_player

    def ataque_player(self, tab_inimigo):
        while True:
            ataque = input("Digite as coordenadas de ataque: ").upper()

            if len(ataque) == 0:
                print("A coordenada não pode ser vazia!")
                continue
            elif len(ataque) > 3:
                print("A coordenada não pode ter mais de 3 caracteres!")
                continue
            elif not ataque[0].isalpha():
                print("O primeiro caractere deve ser uma letra!")
                continue
            elif not ataque[1:].isdigit():
                print("Depois da letra devem existir apenas números!")
                continue

            resposta, tiro_valido = tab_inimigo.receber_tiro(ataque)

            if not tiro_valido:
                print(resposta)
                continue

            for embarc in self.frota:
                if ataque in embarc.partes_inteiras:
                    embarc.recebe_dano(ataque)

            tab_inimigo.mostrar_tabM()
            print(f"\n{resposta}\n")

            # Guarda o resultado do tiro válido e sai do while
            resultado = {ataque: resposta}
            self.ataques.appende(resultado)
            break
                    

class Cpu(Jogador):
    def __init__(self, id_cpu, frota = []):
        super().__init__(frota)
        self.id_cpu = id_cpu

    def ataque_cpu(self, tab_inimigo):
        while True:
            letras = 'ABCDEFGHIJ'
            letra_sorteada = random.choice(letras)
            numero_sorteado = random.randint(1, 10)
            ataque = letra_sorteada + str(numero_sorteado)

            resposta, tiro_valido = tab_inimigo.receber_tiro(ataque)

            if not tiro_valido:
                continue

            for embarc in self.frota:
                if ataque in embarc.partes_inteiras:
                    embarc.recebe_dano(ataque)

            tab_inimigo.mostrar_tabM()

            # Guarda o resultado do tiro válido e sai do while
            resultado = {ataque: resposta}
            self.ataques.appende(resultado)
            break


if __name__ == "__main__":
    '''coordenada = input("Digite a coordenada: ").upper()
    print(coordenada)'''
