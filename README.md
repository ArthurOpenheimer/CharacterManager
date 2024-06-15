<h1>CharacterManager</h1>
<h3>Repositório do projeto final da disciplina de Banco de Dados 2</h3>

<body>
    <h1>Exemplos de JSONs</h1>
    <h2>JSON para Arma</h2>
    <pre>
        {
        "_id": int,
        "Dano": int,
        "Descrição": String
        }
    </pre>
    <h2>JSON para Personagem com Arma</h2>
    <pre>
        {
        "Nome": String,
        "Classe": String,
        "Idade": int,
        "Arma": {
            "$ref": "Armas",
            "$id": int
        },
        "Habilidades": [
            {
            "Descrição": String
            },
            {
            "Descrição": String
            }
        ]
        }
    </pre>
    <h2>JSON para Personagem sem Arma</h2>
    <pre>
        {
        "Nome": String,
        "Classe": String,
        "Idade": int,
        "Arma": null,
        "Habilidades": [
            {
            "Descrição": String
            },
            {
            "Descrição": String
            }
        ]
        }
    </pre>
</body>
