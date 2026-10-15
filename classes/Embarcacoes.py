class Embarcacoes:
    def __init__(self, vida, tipo, coordenadas = []):
        self.vida = vida
        self.tipo = tipo
        self.coordenadas = coordenadas
        self.partes_inteiras = coordenadas
        self.partes_atingidas = []

    def esta_afundado(self):
        if self.vida <= 0:
            return True
        return False

    def recebe_dano(self, ataque):
        self.vida -= 1
        ataque = ataque.upper()
        self.partes_inteiras.remove(ataque)
        self.partes_atingidas.append(ataque)


if __name__ == "__main__":
    pa1 = Embarcacoes(4, "Porta-Aviões", ["C3", "D3", "E3", "F3"])

    for i in range(4):
        print(pa1.partes_inteiras)
        print(pa1.partes_atingidas)
        ataque = input("\nDigite as coordenadas de ataque: ")
        pa1.recebe_dano(ataque)
        is_afundado = pa1.esta_afundado()

        if is_afundado:
            print("\nPorta-Aviões Afundado!")
        else:
            print("\nPorta-Aviões ainda na batalha!")

        print(f"\nVida Porta-Aviões: {pa1.vida}\n")