class Habilidade:
    def __init__(self, descricao):
        self.descricao = descricao

    def to_dict(self):
        return {"descricao": self.descricao}
