
from sqlalchemy.orm import Session
from app.domain.models.opcoes_resposta import OpcaoResposta

class OpcoesRespostaRepository:
    def __init__(self, db: Session):
     self.db = db
   
    def create(self, opcao_reposta: OpcaoResposta):
        self.db.add(opcao_reposta)
        self.db.commit()
        self.db.refresh(opcao_reposta)
        return opcao_reposta

    def get_all(self):
        return self.db.query(OpcaoResposta).order_by(OpcaoResposta.ordem).all()

    def get_by_formulario(self, id_pergunta: int):
        return self.db.query(OpcaoResposta).filter(OpcaoResposta.id_pergunta == id_pergunta).order_by(OpcaoResposta.ordem).all()

    def get_by_id(self, pergunta_id: int):
        return self.db.query(OpcaoResposta).OpcaoResposta(OpcaoResposta.id == pergunta_id).first()

