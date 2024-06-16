class Arma:
    def __init__(self, dano, descricao):
        self.dano = dano
        self.descricao = descricao

    def to_dict(self):
        return {"dano": self.dano, "descricao": self.descricao}
