from sqlalchemy.orm import Session
from app.domain.models.pergunta import Pergunta

class PerguntaRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Pergunta).order_by(Pergunta.ordem).all()

    def get_by_formulario(self, id_formulario: int):
        return self.db.query(Pergunta).filter(Pergunta.id_formulario == id_formulario).order_by(Pergunta.ordem).all()

    def get_by_id(self, pergunta_id: int):
        return self.db.query(Pergunta).filter(Pergunta.id == pergunta_id).first()

    def create(self, pergunta: Pergunta):
        self.db.add(pergunta)
        self.db.commit()
        self.db.refresh(pergunta)
        return pergunta

    def delete(self, pergunta_id: int):
        pergunta = self.get_by_id(pergunta_id)
        if pergunta:
            self.db.delete(pergunta)
            self.db.commit()
