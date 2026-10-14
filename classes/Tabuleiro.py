class Tabuleiro:
    def __init__(self):
        self.tab_mostrado = {
            "A": {"1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-", "8": "-", "9": "-", "10": "-"},
            "B": {"1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-", "8": "-", "9": "-", "10": "-"},
            "C": {"1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-", "8": "-", "9": "-", "10": "-"},
            "D": {"1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-", "8": "-", "9": "-", "10": "-"},
            "E": {"1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-", "8": "-", "9": "-", "10": "-"},
            "F": {"1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-", "8": "-", "9": "-", "10": "-"},
            "G": {"1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-", "8": "-", "9": "-", "10": "-"},
            "H": {"1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-", "8": "-", "9": "-", "10": "-"},
            "I": {"1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-", "8": "-", "9": "-", "10": "-"},
            "J": {"1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-", "8": "-", "9": "-", "10": "-"}
        }
        self.tab_jogador = {
            "A": {"1": "~", "2": "~", "3": "~", "4": "~", "5": "~", "6": "~", "7": "~", "8": "~", "9": "~", "10": "~"},
            "B": {"1": "~", "2": "~", "3": "~", "4": "~", "5": "~", "6": "~", "7": "~", "8": "~", "9": "~", "10": "~"},
            "C": {"1": "~", "2": "~", "3": "~", "4": "~", "5": "~", "6": "~", "7": "~", "8": "~", "9": "~", "10": "~"},
            "D": {"1": "~", "2": "~", "3": "~", "4": "~", "5": "~", "6": "~", "7": "~", "8": "~", "9": "~", "10": "~"},
            "E": {"1": "~", "2": "~", "3": "~", "4": "~", "5": "~", "6": "~", "7": "~", "8": "~", "9": "~", "10": "~"},
            "F": {"1": "~", "2": "~", "3": "~", "4": "~", "5": "~", "6": "~", "7": "~", "8": "~", "9": "~", "10": "~"},
            "G": {"1": "~", "2": "~", "3": "~", "4": "~", "5": "~", "6": "~", "7": "~", "8": "~", "9": "~", "10": "~"},
            "H": {"1": "~", "2": "~", "3": "~", "4": "~", "5": "~", "6": "~", "7": "~", "8": "~", "9": "~", "10": "~"},
            "I": {"1": "~", "2": "~", "3": "~", "4": "~", "5": "~", "6": "~", "7": "~", "8": "~", "9": "~", "10": "~"},
            "J": {"1": "~", "2": "~", "3": "~", "4": "~", "5": "~", "6": "~", "7": "~", "8": "~", "9": "~", "10": "~"}
        }

    def mostrar_tabM(self):
        print("\n    1   2   3   4   5   6   7   8   9  10")
        print("  +" + "---+" * 10)

        for linha, colunas in self.tab_mostrado.items():
            print(f" {linha} ", end="")

            for coluna in colunas:
                print(f" {colunas[coluna]} |", end="")

            print()
            print("  +" + "---+" * 10)
        print()

    def mostrar_tabJ(self):
        print("\n    1   2   3   4   5   6   7   8   9  10")
        print("  +" + "---+" * 10)

        for linha, colunas in self.tab_jogador.items():
            print(f" {linha} ", end="")

            for coluna in colunas:
                print(f" {colunas[coluna]} |", end="")

            print()
            print("  +" + "---+" * 10)
        print()

    def posicionar_navio(self, coordenadas):
        # Verifica se são aceitas nas regras de limites
        linhas_validas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        colunas_validas = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        for c in coordenadas:
            linha = c[0].upper()
            if linha not in linhas_validas:
                print(linha)
                return f"A linha '{linha}' é inexistente! Tente novamente!"
            coluna = c[1:]
            if coluna not in colunas_validas:
                return f"A coluna '{coluna}' é inexistente! Tente novamente!"
            
        # Verifica se são aceitas nas regras de sobreposição
        for c in coordenadas:
            linha = c[0].upper()
            coluna = c[1:]
            if self.tab_jogador[linha][coluna] != "~":
                return f"A posição que escolheu já possuí outra embarcação em '{c}'! Escolha outra posição!"
            
        # Após atender as 2 regras coloca a embarcação no tab_jogador
        tipo_embarcacao = "~"
        if len(coordenadas) == 4:
            tipo_embarcacao = "A"
        elif len(coordenadas) == 3:
            tipo_embarcacao = "E"
        elif len(coordenadas) == 2:
            tipo_embarcacao = "R"
        elif len(coordenadas) == 1:
            tipo_embarcacao = "S"

        for c in coordenadas:
            linha = c[0].upper()
            coluna = c[1:]
            self.tab_jogador[linha][coluna] = tipo_embarcacao
        return f"Embarcação colocada com sucesso!"

    def receber_tiro(self, ataque):
        linha = ataque[0].upper()
        coluna = ataque[1:]
        if self.tab_mostrado[linha][coluna] != "-":
            return "Posição já alvejada! Escolha outra!"
        elif self.tab_jogador[linha][coluna] == "~":
            self.tab_mostrado[linha][coluna] = "~"
            return "Água!"
        else:
            self.tab_mostrado[linha][coluna] = "X"
            self.tab_jogador[linha][coluna] = "F"
            if self.tab_jogador[linha][coluna] == "A":
                return "Fogo! Porta-Aviões!"
            elif self.tab_jogador[linha][coluna] == "E":
                return "Fogo! Encouraçado!"
            elif self.tab_jogador[linha][coluna] == "R":
                return "Fogo! Rebocador!"
            elif self.tab_jogador[linha][coluna] == "S":
                return "Fogo! Submarino!"


if __name__ == "__main__":
    tab1 = Tabuleiro()
    tab1.mostrar_tabJ()
    resposta = tab1.posicionar_navio(["C3", "D3", "e3", "F3"])
    print(resposta)
    tab1.mostrar_tabJ()
    tab1.tab_mostrado["C"]["3"] = "X"
    tab1.tab_mostrado["C"]["4"] = "~"
    tab1.mostrar_tabM()