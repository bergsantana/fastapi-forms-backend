from sqlalchemy.orm import Session
from app.domain.models.formulario import Formulario

class FormularioRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Formulario).order_by(Formulario.ordem).all()

    def get_by_id(self, formulario_id: int):
        return self.db.query(Formulario).filter(Formulario.id == formulario_id).first()

    def create(self, formulario: Formulario):
        self.db.add(formulario)
        self.db.commit()
        self.db.refresh(formulario)
        return formulario

    def delete(self, formulario_id: int):
        formulario = self.get_by_id(formulario_id)
        if formulario:
            self.db.delete(formulario)
            self.db.commit()
