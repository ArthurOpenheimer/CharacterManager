class Personagem:
    def __init__(self, nome, classe, idade, habilidades, armas):
        self.nome = nome
        self.classe = classe
        self.idade = idade
        self.habilidades = habilidades
        self.armas = armas

    def to_dict(self):
        return {
            "nome": self.nome,
            "classe": self.classe,
            "idade": self.idade,
            "habilidades": [habilidade.to_dict() for habilidade in self.habilidades],
            "armas": [arma.to_dict() for arma in self.armas],
        }

    def print(self):
        print("--------------------------------------------------")
        print(f"Nome: {self.nome}")
        print(f"Classe: {self.classe}")
        print(f"Idade: {self.idade}")
        print("Habilidades:")
        for habilidade in self.habilidades:
            print(f"  - {habilidade.descricao}")
        print("Armas:")
        for arma in self.armas:
            print(f"  - {arma.descricao}, Dano: {arma.dano}")
        print("--------------------------------------------------")
