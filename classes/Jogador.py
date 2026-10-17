import random

class Jogador:
    def __init__(self, id_jogador, meu_tab, frota = []):
        self.id_jogador = id_jogador
        self.meu_tab = meu_tab
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
            elif e.tipo == "Encouraçado":
                cont_E += 1
            elif e.tipo == "Rebocador":
                cont_R += 1
            elif e.tipo == "Submarino":
                cont_S += 1

        print(f"O jogador {self.id_jogador} ainda possui:")
        print(f"- {cont_PA} Porta-Aviões - 4 casas")
        print(f"- {cont_E} Encouraçado's - 3 casas")
        print(f"- {cont_R} Rebocador'es - 2 casas")
        print(f"- {cont_S} Submarino's - 1 casa")
        return False

class Player(Jogador):
    def __init__(self, id_jogador, meu_tab, frota = []):
        super().__init__(id_jogador, meu_tab, frota)

    def ataque_player(self, j_inimigo):
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

            resposta, tiro_valido = j_inimigo.meu_tab.receber_tiro(ataque)

            if not tiro_valido:
                print(resposta)
                continue

            for embarc in j_inimigo.frota:
                if ataque in embarc.partes_inteiras:
                    embarc.recebe_dano(ataque)
                if embarc.esta_afundado():
                    j_inimigo.frota.remove(embarc)
                    j_inimigo.frota_afundada.append(embarc)

            # tab_inimigo.mostrar_tabM()
            print(f"\n{resposta}\n")

            # Guarda o resultado do tiro válido e sai do while
            resultado = {ataque: resposta}
            self.ataques.append(resultado)
            break
                    

class Cpu(Jogador):
    def __init__(self, id_jogador, meu_tab, frota = []):
        super().__init__(id_jogador, meu_tab, frota)

    def ataque_cpu(self, j_inimigo):
        while True:
            letras = 'ABCDEFGHIJ'
            letra_sorteada = random.choice(letras)
            numero_sorteado = random.randint(1, 10)
            ataque = letra_sorteada + str(numero_sorteado)

            resposta, tiro_valido = j_inimigo.meu_tab.receber_tiro(ataque)

            if not tiro_valido:
                continue
            print(f"CPU atacou a {ataque}")

            for embarc in j_inimigo.frota:
                if ataque in embarc.partes_inteiras:
                    embarc.recebe_dano(ataque)
                if embarc.esta_afundado():
                    j_inimigo.frota.remove(embarc)
                    j_inimigo.frota_afundada.append(embarc)

            j_inimigo.meu_tab.mostrar_tabM()
            print(f"\n{resposta}\n")

            # Guarda o resultado do tiro válido e sai do while
            resultado = {ataque: resposta}
            self.ataques.append(resultado)
            break


if __name__ == "__main__":
    '''coordenada = input("Digite a coordenada: ").upper()
    print(coordenada)'''
    t1 = Cpu(1, "tabela")
    t2 = Cpu(1, "tabela")
    t3 = Cpu(1, "tabela")
    t4 = Cpu(1, "tabela")
    teste = []
    teste.append(t1)
    teste.append(t2)
    teste.append(t3)
    teste.append(t4)
    j1 = Cpu(1, "tabela", teste)

    j1.frota.remove(t1)
    print(j1.frota)
