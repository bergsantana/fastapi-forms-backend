from sqlalchemy.orm import Session
from app.domain.models.opcoes_resposta import OpcaoResposta
from app.repositories.opcoes_resposta import  OpcaoResposta
 
class RespostaUseCase:
    def __init__(self, db: Session):
        self.db = db
        self.repo = OpcaoResposta(db)

    def criar_respostas(self, respostas_data: list):
        for data in respostas_data:
            # Cria a resposta (valores livres)
            # resposta = Resposta(
            #     id_pergunta=data['id_pergunta'],
            #     resposta_texto=data.get('resposta_texto'),
            #     resposta_inteiro=data.get('resposta_inteiro'),
            #     resposta_decimal=data.get('resposta_decimal')
            # )
            resposta = OpcaoResposta(
                id_pergunta = data['id_pergunta'],
                resposta = data['id_pergunta'],
                ordem = data['id_pergunta'],
                resposta_aberta = data['id_pergunta']
            )

            print('repostas')
            print(resposta)
            # self.resposta_repo.create(resposta)

        

        return {"message": "Respostas salvas com sucesso"}
