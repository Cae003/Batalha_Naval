class Jogador:
    def __init__(self, frota = []):
        self.ataques = []
        self.frota = frota

    def verificar_derrota(self):
        ...

class Player(Jogador):
    def __init__(self, id_player, frota = []):
        super().__init__(frota)
        self.id_player = id_player

    def ataque_player(self):
        ...

class Cpu(Jogador):
    def __init__(self, id_cpu, frota = []):
        super().__init__(frota)
        self.id_cpu = id_cpu

    def ataque_cpu(self):
        ...