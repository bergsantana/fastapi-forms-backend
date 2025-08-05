from app.domain.models.opcoes_resposta_pergunta  import OpcaoRespostaPergunta
from sqlalchemy.orm import Session


class OpcoesRespostaPerguntaRepository:
    def __init__(self, db: Session):
        self.db = db
    def create(self, entity: OpcaoRespostaPergunta) -> OpcaoRespostaPergunta:
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity