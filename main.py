from arma import Arma
from habilidades import Habilidade
from personagem import Personagem
from personagem_dao import PersonagemDAO


def create_personagem(dao):
    nome = input("Nome do personagem: ")
    classe = input("Classe do personagem: ")
    idade = int(input("Idade do personagem: "))

    num_habilidades = int(input("Número de habilidades: "))
    habilidades = []
    for _ in range(num_habilidades):
        descricao = input(f"Descrição da habilidade {_ + 1}: ")
        habilidades.append(Habilidade(descricao=descricao))

    num_armas = int(input("Número de armas: "))
    armas = []
    for _ in range(num_armas):
        descricao = input(f"Descrição da arma {_ + 1}: ")
        dano = int(input(f"Dano da arma {_ + 1}: "))
        armas.append(Arma(dano=dano, descricao=descricao))

    personagem = Personagem(
        nome=nome, classe=classe, idade=idade, habilidades=habilidades, armas=armas
    )
    dao.create(personagem)
    print("Personagem inserido com sucesso!")


def read_personagem(dao):
    nome = input("Nome do personagem: ")
    personagem = dao.read(nome)
    if personagem:
        print(f"Nome: {personagem.nome}")
        print(f"Classe: {personagem.classe}")
        print(f"Idade: {personagem.idade}")
        print("Habilidades:")
        for habilidade in personagem.habilidades:
            print(f"- {habilidade.descricao}")
        print("Armas:")
        for arma in personagem.armas:
            print(f"- {arma.descricao}, Dano: {arma.dano}")
    else:
        print("Personagem não encontrado.")


def update_personagem(dao):
    nome = input("Nome do personagem a ser atualizado: ")
    campo = input("Campo a ser atualizado (nome, classe, idade, habilidades, armas): ")

    if campo in ["nome", "classe", "idade"]:
        valor = input(f"Novo valor para {campo}: ")
        if campo == "idade":
            valor = int(valor)
        update_fields = {campo: valor}
    elif campo == "habilidades":
        num_habilidades = int(input("Número de habilidades: "))
        habilidades = []
        for _ in range(num_habilidades):
            descricao = input(f"Descrição da habilidade {_ + 1}: ")
            habilidades.append(Habilidade(descricao=descricao))
        update_fields = {
            "habilidades": [habilidade.to_dict() for habilidade in habilidades]
        }
    elif campo == "armas":
        num_armas = int(input("Número de armas: "))
        armas = []
        for _ in range(num_armas):
            descricao = input(f"Descrição da arma {_ + 1}: ")
            dano = int(input(f"Dano da arma {_ + 1}: "))
            armas.append(Arma(dano=dano, descricao=descricao))
        update_fields = {"armas": [arma.to_dict() for arma in armas]}
    else:
        print("Campo inválido.")
        return

    updated_count = dao.update(nome, update_fields)
    if updated_count > 0:
        print("Personagem atualizado com sucesso!")
    else:
        print("Personagem não encontrado.")


def delete_personagem(dao):
    nome = input("Nome do personagem a ser deletado: ")
    deleted_count = dao.delete(nome)
    if deleted_count > 0:
        print("Personagem deletado com sucesso!")
    else:
        print("Personagem não encontrado.")


def read_all_personagens(dao):
    personagens = dao.read_all()
    if personagens:
        for personagem in personagens:
            personagem.print()
    else:
        print("Nenhum personagem encontrado.")


def find_personagens_by_habilidade(dao):
    descricao = input("Descrição da habilidade: ")
    personagens = dao.find_by_habilidade(descricao)
    if personagens:
        for personagem in personagens:
            personagem.print()
    else:
        print("Nenhum personagem encontrado com essa habilidade.")


def find_personagens_by_age(dao):
    comparison = input(
        "Você quer personagens com idade maior ou menor? (maior/menor): "
    )
    if comparison not in ["maior", "menor"]:
        print("Opção inválida.")
        return
    idade = int(input("Digite a idade: "))
    personagens = dao.find_by_age(comparison, idade)
    if personagens:
        for personagem in personagens:
            personagem.print()
    else:
        print("Nenhum personagem encontrado.")


def main():
    dao = PersonagemDAO()

    while True:
        print("\nMenu:")
        print("1. Criar personagem")
        print("2. Ler personagem")
        print("3. Atualizar personagem")
        print("4. Deletar personagem")
        print("5. Listar todos os personagens")
        print("6. Buscar personagens por habilidade")
        print("7. Buscar personagens por idade")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            create_personagem(dao)
        elif escolha == "2":
            read_personagem(dao)
        elif escolha == "3":
            update_personagem(dao)
        elif escolha == "4":
            delete_personagem(dao)
        elif escolha == "5":
            read_all_personagens(dao)
        elif escolha == "6":
            find_personagens_by_habilidade(dao)
        elif escolha == "7":
            find_personagens_by_age(dao)
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
