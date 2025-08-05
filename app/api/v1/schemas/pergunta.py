from pydantic import BaseModel
from enum import Enum

class TipoPerguntaEnum(str, Enum):
    Sim_Nao = "Sim_Nao"
    Multipla_escolha = "Multipla_escolha"
    Unica_escolha = "Unica_escolha"
    Texto_livre = "Texto_livre"
    Inteiro = "Inteiro"
    Numero_decimal = "Numero_decimal"

class PerguntaCreateDto(BaseModel):
    titulo: str
    codigo: str
    orientacao_resposta: str
    obrigatoria: bool
    ordem: int
    sub_pergunta: bool
    tipo_pergunta: TipoPerguntaEnum

class PerguntaCreateToDb(BaseModel):
    id_formulario: int
    titulo: str
    codigo: str
    orientacao_resposta: str
    obrigatoria: bool
    ordem: int
    sub_pergunta: bool
    tipo_pergunta: TipoPerguntaEnum

class PerguntaOut(BaseModel):
    id: int
    id_formulario: int
    titulo: str
    codigo: str
    orientacao_resposta: str
    obrigatoria: bool
    ordem: int
    sub_pergunta: bool
    tipo_pergunta: TipoPerguntaEnum

    class Config:
        orm_mode = True
