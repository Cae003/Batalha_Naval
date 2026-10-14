import os, random

def menu_modo_jogo():
    while True:
        print()
        print("="*50)
        print("\nMODO DE JOGO:")
        print("\n1 - Jogador x Jogador\n2 - Jogador x CPU\n3 - Voltar ao Menu\n")
        opcao =  input("Digite o número da opção desejada: ")

        if opcao == '1':
            return 1
        elif opcao == '2':
            return 2
        elif opcao == '3':
            return 3
        else:
            print("Opção Inexistente! Tente Novamente!\n")
            continue

def menu_posicionar():
    while True:
        print()
        print("="*50)
        print("\nPOSICIONAMENTO DAS EMBARCAÇÕES:")
        print("\n1 - Posicionar Automaticamente\n2 - Posicionar Manualmente\n3 - Voltar ao Menu\n")
        opcao =  input("Digite o número da opção desejada: ")

        if opcao == '1':
            return 1
        elif opcao == '2':
            return 2
        elif opcao == '3':
            return 3
        else:
            print("Opção Inexistente! Tente Novamente!\n")
            continue

def monta_tabuleiros():
    ...

def partida(is_cpu):
    ...


if __name__ == "__main__":
    titulo = "BATALHA NAVAL"
    base_dir = os.path.dirname(__file__)
    texto_regras_path = os.path.join(base_dir, "Texto_Regras.txt")
    with open(texto_regras_path, "r", encoding="utf-8") as f:
        texto_regras = f.read()

    print("="*50)
    print(f"\n{titulo:^50}\n")

    while True:
        print("="*50)
        print("\n1 - Jogar\n2 - Regras\n3 - Sair\n")
        opcao =  input("Digite o número da opção desejada: ")

        if opcao == '1':
            modo_selecionado = menu_modo_jogo()
            if modo_selecionado == 3:
                continue
            modo_posicionamento = menu_posicionar()
            if modo_posicionamento == 3:
                continue

            if modo_selecionado == 1 and modo_posicionamento == 1:
                #Caso em que vai direto pro jogo de player x player
                break
            elif modo_selecionado == 1 and modo_posicionamento == 2:
                #Caso em que abre menu de posicionamento para os 2 players
                break
            elif modo_selecionado == 2 and modo_posicionamento == 1:
                #Caso em que vai direto pro jogo de player x CPU
                break
            elif modo_selecionado == 2 and modo_posicionamento == 2:
                #Caso em que abre menu de posicionamento para o player e automatico pra CPU
                break
            else:
                print("Erro! Opção não prevista selecionada!")
        elif opcao == '2':
            print(f"\n{texto_regras}\n")
        elif opcao == '3':
            print("Obrigado por Jogar!! ;)\n")
            exit()
        else:
            print("Opção Inexistente! Tente Novamente!\n")
            continue
