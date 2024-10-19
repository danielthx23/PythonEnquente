import banco

def cadastra_enquente(enq: dict):
    banco.insere_enquente(enq)
    id = enq['id']
    print("ID: ", id)
    lista_perguntas = enq['perguntas']
    for perg in lista_perguntas:
        perg['id_enquente'] = id
        if perg['tipo'] == 2 or perg['tipo'] == 3:
            lista_opcoes = perg.pop('opcoes')
        banco.insere_pergunta(perg)
        if perg['tipo'] != 1:
            for opcao in lista_opcoes:
                opcao['id_pergunta'] = perg['id']
                banco.insere_opcao(opcao)

if __name__ == "__main__":
    info = {
            "nome": "Pesquisa de intenção de voto",
            "categoria": "Politica",
            "perguntas": [
                    {
                        "texto": "Em quem você votou no primeiro turno?",
                        "tipo": 1,
                        "numero": 1
                    },
                    {
                        "texto": "Em quem você vai votar no 2 turno?",
                        "tipo": 2,
                        "numero": 2,
                        "opcoes": [
                            {
                                "alternativa": "Boulos",
                                "rotulo": 1
                            },
                            {
                                "alternativa": "Nunes",
                                "rotulo": 2
                            }
                        ]
                    }
                ]
            }
    cadastra_enquente(info)
