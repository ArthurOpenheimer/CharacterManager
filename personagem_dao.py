from arma import Arma
from habilidades import Habilidade
from personagem import Personagem
from pymongo import MongoClient


class PersonagemDAO:
    def __init__(
        self,
        db_name="character_manager",
        collection_name="characters",
        uri="mongodb://localhost:27017",
    ):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create(self, personagem):
        return self.collection.insert_one(personagem.to_dict())

    def read(self, personagem_name):
        result = self.collection.find_one({"nome": personagem_name})
        if result:
            habilidades = [
                Habilidade(**habilidade) for habilidade in result["habilidades"]
            ]
            armas = [Arma(**arma) for arma in result["armas"]]
            return Personagem(
                nome=result["nome"],
                classe=result["classe"],
                idade=result["idade"],
                habilidades=habilidades,
                armas=armas,
            )
        return None

    def update(self, personagem_name, update_fields):
        update_result = self.collection.update_one(
            {"nome": personagem_name}, {"$set": update_fields}
        )
        return update_result.modified_count

    def delete(self, personagem_name):
        delete_result = self.collection.delete_one({"nome": personagem_name})
        return delete_result.deleted_count

    def read_all(self):
        result = self.collection.find()
        personagens = []
        for personagem in result:
            habilidades = [
                Habilidade(**habilidade) for habilidade in personagem["habilidades"]
            ]
            armas = [Arma(**arma) for arma in personagem["armas"]]
            personagens.append(
                Personagem(
                    nome=personagem["nome"],
                    classe=personagem["classe"],
                    idade=personagem["idade"],
                    habilidades=habilidades,
                    armas=armas,
                )
            )
        return personagens

    def find_by_habilidade(self, descricao):
        results = self.collection.find({"habilidades.descricao": descricao})
        personagens = []
        for result in results:
            habilidades = [
                Habilidade(**habilidade) for habilidade in result["habilidades"]
            ]
            armas = [Arma(**arma) for arma in result["armas"]]
            personagens.append(
                Personagem(
                    nome=result["nome"],
                    classe=result["classe"],
                    idade=result["idade"],
                    habilidades=habilidades,
                    armas=armas,
                )
            )
        return personagens

    def find_by_age(self, comparison, idade):
        if comparison == "maior":
            query = {"idade": {"$gt": idade}}
        elif comparison == "menor":
            query = {"idade": {"$lt": idade}}
        else:
            return []

        results = self.collection.find(query)
        personagens = []
        for result in results:
            habilidades = [
                Habilidade(**habilidade) for habilidade in result["habilidades"]
            ]
            armas = [Arma(**arma) for arma in result["armas"]]
            personagens.append(
                Personagem(
                    nome=result["nome"],
                    classe=result["classe"],
                    idade=result["idade"],
                    habilidades=habilidades,
                    armas=armas,
                )
            )
        return personagens
