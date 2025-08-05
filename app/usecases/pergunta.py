from sqlalchemy.orm import Session
from app.repositories.pergunta import PerguntaRepository
from app.domain.models.pergunta import Pergunta, TipoPerguntaEnum

class PerguntaUseCase:
    def __init__(self, db: Session):
        self.repo = PerguntaRepository(db)

    def listar_por_formulario(self, id_formulario: int):
        return self.repo.get_by_formulario(id_formulario)

    def criar_pergunta(self, data: dict):
        nova = Pergunta(**data)
        return self.repo.create(nova)

    def deletar_pergunta(self, pergunta_id: int):
        return self.repo.delete(pergunta_id)
