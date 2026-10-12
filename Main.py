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
                print(opcao)
                break
            elif opcao == '2':
                print(texto_regras)
            elif opcao == '3':
                print("Obrigado por Jogar!! ;)\n")
                exit()
            else:
                print("Opção Inexistente! Tente Novamente!\n")
                continue
