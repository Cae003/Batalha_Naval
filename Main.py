import os, random
from classes.Jogador import Player, Cpu
from classes.Tabuleiro import Tabuleiro
from classes.Embarcacoes import Embarcacoes

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

def valida_captura(coordenada):
    if len(coordenada) == 0:
        print("A coordenada não pode ser vazia!")
        return False
    elif len(coordenada) > 3:
        print("A coordenada não pode ter mais de 3 caracteres!")
        return False
    elif not coordenada[0].isalpha():
        print("O primeiro caractere deve ser uma letra!")
        return False
    elif not coordenada[1:].isdigit():
        print("Depois da letra devem existir apenas números!")
        return False
    else:
        return True

def valida_coordenadas(coordenadas):
    linhas = [c[0] for c in coordenadas]
    colunas = [int(c[1:]) for c in coordenadas]

    mesma_linha = len(set(linhas)) == 1
    mesma_coluna = len(set(colunas)) == 1

    if mesma_linha:
        colunas.sort()

        if colunas == list(range(colunas[0], colunas[0] + len(colunas))):
            return True
        else:
            return False
    elif mesma_coluna:
        linhas.sort()

        valores_linhas = [ord(linha) for linha in linhas]

        if valores_linhas == list(range(valores_linhas[0], valores_linhas[0] + len(valores_linhas))):
            return True
        else:
            return False
    else:
        return False

def gerar_coordenadas(tamanho):
    linhas = "ABCDEFGHIJ"
    colunas = list(range(1, 11))
    coordenadas = []
    direcao = random.choice(["horizontal", "vertical"])

    if direcao == "horizontal":
        linha = random.choice(linhas)
        coluna_inicial = random.randint(1, 11 - tamanho)

        for coluna in range(coluna_inicial, coluna_inicial + tamanho):
            coordenada = f"{linha}{coluna}"
            coordenadas.append(coordenada)
    elif direcao == "vertical":
        coluna = random.choice(colunas)
        linha_inicial = random.randint(0, 10 - tamanho)

        for linha in range(linha_inicial, linha_inicial + tamanho):
            coordenada = f"{linhas[linha]}{coluna}"
            coordenadas.append(coordenada)
    return coordenadas

def criar_frota_manual(tabuleiro):
    frota_cods = []
    tabuleiro.mostrar_tabJ()
    for caso in range(1,10):
        if caso <= 2:
            while True:
                c1 =  input(f"Escolha a coordenada 1 do Porta-Aviões {caso}: ").upper()
                if not valida_captura(c1):
                    continue
                c2 =  input(f"Escolha a coordenada 2 do Porta-Aviões {caso}: ").upper()
                if not valida_captura(c2):
                    continue
                c3 =  input(f"Escolha a coordenada 3 do Porta-Aviões {caso}: ").upper()
                if not valida_captura(c3):
                    continue
                c4 =  input(f"Escolha a coordenada 4 do Porta-Aviões {caso}: ").upper()
                if not valida_captura(c4):
                    continue
                coordenadas = [c1, c2, c3, c4]

                if not valida_coordenadas(coordenadas):
                    print("A embarcação não esta posicionada em sequência horizontal nem vertical!")
                    continue

                resposta, is_valido = tabuleiro.posicionar_navio(coordenadas)
                if not is_valido:
                    print(resposta)
                    continue
                print(resposta)
                tabuleiro.mostrar_tabJ()
                break
            frota_cods.append(coordenadas)
        elif caso > 2 and caso <= 4:
            while True:
                c1 =  input(f"Escolha a coordenada 1 do Encouraçado {caso-2}: ").upper()
                if not valida_captura(c1):
                    continue
                c2 =  input(f"Escolha a coordenada 2 do Encouraçado {caso-2}: ").upper()
                if not valida_captura(c2):
                    continue
                c3 =  input(f"Escolha a coordenada 3 do Encouraçado {caso-2}: ").upper()
                if not valida_captura(c3):
                    continue
                coordenadas = [c1, c2, c3]

                if not valida_coordenadas(coordenadas):
                    print("A embarcação não esta posicionada em sequência horizontal nem vertical!")
                    continue

                resposta, is_valido = tabuleiro.posicionar_navio(coordenadas)
                if not is_valido:
                    print(resposta)
                    continue
                print(resposta)
                tabuleiro.mostrar_tabJ()
                break
            frota_cods.append(coordenadas)
        elif caso > 4 and caso <= 6:
            while True:
                c1 =  input(f"Escolha a coordenada 1 do Rebocador {caso-4}: ").upper()
                if not valida_captura(c1):
                    continue
                c2 =  input(f"Escolha a coordenada 2 do Rebocador {caso-4}: ").upper()
                if not valida_captura(c2):
                    continue
                coordenadas = [c1, c2]

                if not valida_coordenadas(coordenadas):
                    print("A embarcação não esta posicionada em sequência horizontal nem vertical!")
                    continue

                resposta, is_valido = tabuleiro.posicionar_navio(coordenadas)
                if not is_valido:
                    print(resposta)
                    continue
                print(resposta)
                tabuleiro.mostrar_tabJ()
                break
            frota_cods.append(coordenadas)
        elif caso > 6 and caso <= 9:
            while True:
                c1 =  input(f"Escolha as coordenadas do Submarino {caso-6}: ").upper()
                if not valida_captura(c1):
                    continue
                coordenada = [c1]

                resposta, is_valido = tabuleiro.posicionar_navio(coordenada)
                if not is_valido:
                    print(resposta)
                    continue
                print(resposta)
                tabuleiro.mostrar_tabJ()
                break
            frota_cods.append(coordenadas)
    return frota_cods

def criar_frota_auto(tabuleiro):
    frota_cods = []
    for caso in range(1,10):
        if caso <= 2:
            tamanho = 4
        elif caso > 2 and caso <= 4:
            tamanho = 3
        elif caso > 4 and caso <= 6:
            tamanho = 2
        elif caso > 6 and caso <= 9:
            tamanho = 1
        while True:
            coordenadas = gerar_coordenadas(tamanho)
            resposta, is_valido = tabuleiro.posicionar_navio(coordenadas)
            if not is_valido:
                continue
            break
        frota_cods.append(coordenadas)
    return frota_cods

def cria_embarcacoes(num_jogador, frota_cods):
    match num_jogador:
        case 1:
            pa1 = Embarcacoes(4, "Porta-Aviões", frota_cods[0])
            pa2 = Embarcacoes(4, "Porta-Aviões", frota_cods[1])
            e1 = Embarcacoes(3, "Encouraçado", frota_cods[2])
            e2 = Embarcacoes(3, "Encouraçado", frota_cods[3])
            r1 = Embarcacoes(2, "Rebocador", frota_cods[4])
            r2 = Embarcacoes(2, "Rebocador", frota_cods[5])
            s1 = Embarcacoes(1, "Submarino", frota_cods[6])
            s2 = Embarcacoes(1, "Submarino", frota_cods[7])
            s3 = Embarcacoes(1, "Submarino", frota_cods[8])
            return [pa1, pa2, e1, e2, r1, r2, s1, s2, s3]
        case 2:
            pa3 = Embarcacoes(4, "Porta-Aviões", frota_cods[0])
            pa4 = Embarcacoes(4, "Porta-Aviões", frota_cods[1])
            e3 = Embarcacoes(3, "Encouraçado", frota_cods[2])
            e4 = Embarcacoes(3, "Encouraçado", frota_cods[3])
            r3 = Embarcacoes(2, "Rebocador", frota_cods[4])
            r4 = Embarcacoes(2, "Rebocador", frota_cods[5])
            s4 = Embarcacoes(1, "Submarino", frota_cods[6])
            s5 = Embarcacoes(1, "Submarino", frota_cods[7])
            s6 = Embarcacoes(1, "Submarino", frota_cods[8])
            return [pa3, pa4, e3, e4, r3, r4, s4, s5, s6]

def partida(j1, j2, is_cpu):
    if is_cpu:
        while True:
            #Turno Jogador
            print("\nJogador 🕹️\n")
            tab2.mostrar_tabM()
            j1.ataque_player(j2)
            if j1.verificar_derrota():
                print("\nVitória da CPU!! 🤖🎉\n")
                print(f"Ataques Jogador 1: {j1.ataques}")
                print(f"\nAtaques Jogador 2: {j2.ataques}")
                break

            print("="*50)
            
            #Turno CPU
            print("\nCPU 🤖🕹️\n")
            #tab2.mostrar_tabJ()
            j2.ataque_cpu(j1)
            if j2.verificar_derrota():
                print("\nVitória do Jogador!! 😎🎉\n")
                print(f"Ataques Jogador 1: {j1.ataques}")
                print(f"\nAtaques Jogador 2: {j2.ataques}")
                break
            print("="*50)
    else:
        while True:
            #Turno Jogador 1
            print("\nJogador 1 🕹️\n")
            tab2.mostrar_tabM()
            j1.ataque_player(j2)
            if j1.verificar_derrota():
                print("\nVitória do Jogador 2!! 😎🎉\n")
                print(f"Ataques Jogador 1: {j1.ataques}")
                print(f"\nAtaques Jogador 2: {j2.ataques}")
                break

            print("="*50)

            #Turno Jogador 2
            print("\nJogador 2 🕹️\n")
            tab1.mostrar_tabM()
            j2.ataque_player(j1)
            if j2.verificar_derrota():
                print("\nVitória do Jogador 1!! 😎🎉\n")
                print(f"Ataques Jogador 1: {j1.ataques}")
                print(f"\nAtaques Jogador 2: {j2.ataques}")
                break
            print("="*50)


if __name__ == "__main__":
    titulo = "⚓ BATALHA NAVAL"
    # Pegar texto das regras que está no txt
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
                print("\nEmbarcações Posicionadas Automaticamente! 👌\n")

                #Criando PLayer 1
                tab1 = Tabuleiro()
                frota1 = cria_embarcacoes(1, criar_frota_auto(tab1))
                jogador1 = Player(1, tab1, frota1)

                #Criando PLayer 2
                tab2 = Tabuleiro()
                frota2 = cria_embarcacoes(2, criar_frota_auto(tab2))
                jogador2 = Player(2, tab2, frota2)

                #Começa o Jogo
                print()
                print("="*50)
                print("\nCOMEÇO DA PARTIDA:\n")
                partida(jogador1, jogador2, False)
                break
            elif modo_selecionado == 1 and modo_posicionamento == 2:
                #Caso em que abre menu de posicionamento para os 2 players
                print()
                print("="*50)
                print("\nPOSICIONAMENTO DAS EMBARCAÇÕES:\n")

                #Criando PLayer 1
                print("\nJogador 1 🕹️\n")
                tab1 = Tabuleiro()
                frota1 = cria_embarcacoes(1, criar_frota_manual(tab1))
                jogador1 = Player(1, tab1, frota1)

                #Criando PLayer 2
                print("\nJogador 2 🕹️\n")
                tab2 = Tabuleiro()
                frota2 = cria_embarcacoes(2, criar_frota_manual(tab2))
                jogador2 = Player(2, tab2, frota2)

                #Começa o Jogo
                print()
                print("="*50)
                print("\nCOMEÇO DA PARTIDA:\n")
                partida(jogador1, jogador2, False)
                break
            elif modo_selecionado == 2 and modo_posicionamento == 1:
                #Caso em que vai direto pro jogo de player x CPU
                print("\nEmbarcações Posicionadas Automaticamente! 👌\n")

                #Criando PLayer 1
                tab1 = Tabuleiro()
                frota1 = cria_embarcacoes(1, criar_frota_auto(tab1))
                jogador1 = Player(1, tab1, frota1)

                #Criando PLayer 2
                tab2 = Tabuleiro()
                frota2 = cria_embarcacoes(2, criar_frota_auto(tab2))
                jogador2 = Cpu(2, tab2, frota2)

                #Começa o Jogo
                print()
                print("="*50)
                print("\nCOMEÇO DA PARTIDA:\n")
                partida(jogador1, jogador2, True)
                break
            elif modo_selecionado == 2 and modo_posicionamento == 2:
                #Caso em que abre menu de posicionamento para o player e automatico pra CPU
                print()
                print("="*50)
                print("\nPOSICIONAMENTO DAS EMBARCAÇÕES:\n")
                
                #Criando PLayer 1
                print("\nJogador 🕹️\n")
                tab1 = Tabuleiro()
                frota1 = cria_embarcacoes(1, criar_frota_manual(tab1))
                jogador1 = Player(1, tab1, frota1)

                #Criando PLayer 2
                print("\nCPU 🤖🕹️\n")
                tab2 = Tabuleiro()
                frota2 = cria_embarcacoes(2, criar_frota_auto(tab2))
                jogador2 = Cpu(2, tab2, frota2)

                #Começa o Jogo
                print()
                print("="*50)
                print("\nCOMEÇO DA PARTIDA:\n")
                partida(jogador1, jogador2, True)
                print("\nObrigado por Jogar!! 😊\n")
                break
            else:
                print("Erro! Opção não prevista selecionada!")
        elif opcao == '2':
            print(f"\n{texto_regras}\n")
        elif opcao == '3':
            print("Obrigado por Jogar!! 😊\n")
            exit()
        else:
            print("Opção Inexistente! Tente Novamente!\n")
            continue
