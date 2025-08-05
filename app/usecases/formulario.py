from sqlalchemy.orm import Session
from app.repositories.formulario import FormularioRepository
from app.repositories.pergunta import PerguntaRepository
from app.domain.models.formulario import Formulario
from app.domain.models.pergunta import Pergunta

class FormularioUseCase:
    def __init__(self, db: Session):
        self.repo = FormularioRepository(db)
        self.repo_pergunta = PerguntaRepository(db)
    def listar_formularios(self):
        return self.repo.get_all()


    def criar_formulario(self, data: dict):
        perguntas_data = data.pop("perguntas", [])
        formulario = Formulario(**data)
        self.repo.create(formulario)

        for pergunta_data in perguntas_data:
            pergunta = Pergunta(**pergunta_data, id_formulario=formulario.id)
            self.repo.create(pergunta)

        return formulario

    def deletar_formulario(self, formulario_id: int):
        return self.repo.delete(formulario_id)
