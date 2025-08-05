from pydantic import BaseModel
from typing import  List

class OpcoesRespostaCreate(BaseModel):
    id: int
    id_pergunta: int
    resposta: str = None
    ordem: int
    resposta_abert: bool



class OpcoesRespostaInput(BaseModel):
    respostas: List[OpcoesRespostaCreate]