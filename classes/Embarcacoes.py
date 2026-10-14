class Embarcacoes:
    def __init__(self, vida, tipo, coordenadas = []):
        self.vida = vida
        self.tipo = tipo
        self.coordenadas = coordenadas

    def esta_afundado(self):
        ...