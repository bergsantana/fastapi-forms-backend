from typing import List
from pydantic import BaseModel
from app.api.v1.schemas.pergunta import PerguntaCreateDto

class FormularioCreate(BaseModel):
    titulo: str
    descricao: str
    ordem: int
    perguntas: List[PerguntaCreateDto] = []

class FormularioOut(BaseModel):
    id: int
    titulo: str
    descricao: str
    ordem: int

    class Config:
        orm_mode = True