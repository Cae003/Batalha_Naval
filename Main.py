import os, random

'''def menu_principal():
    titulo = "BATALHA NAVAL"
    print("="*50)
    print(f"\n{titulo:^50}\n")

    while True:
        print("="*50)
        print("\n1 - Jogar\n2 - Regras\n3 - Sair\n")
        opcao =  input("Digite o número da opção desejada: ")

        if opcao == '1':
            return opcao
        elif opcao == '2':
            return opcao
        elif opcao == '3':
            print("Obrigado por Jogar!! ;)\n")
            exit()
        else:
            print("Opção Inexistente! Tente Novamente!\n")
            continue'''

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


if __name__ == "__main__":
    # opcao = menu_principal()
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
            print("Jogo")
            break
        elif opcao == '2':
            print(f"\n{texto_regras}\n")
        elif opcao == '3':
            print("Obrigado por Jogar!! ;)\n")
            exit()
        else:
            print("Opção Inexistente! Tente Novamente!\n")
            continue
