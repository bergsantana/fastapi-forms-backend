from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class TipoPerguntaEnum(enum.Enum):
    Sim_Nao = "Sim_Nao"
    Multipla_escolha = "Multipla_escolha"
    Unica_escolha = "Unica_escolha"
    Texto_livre = "Texto_livre"
    Inteiro = "Inteiro"
    Numero_decimal = "Numero_decimal"

class Pergunta(Base):
    __tablename__ = "perguntas"
    id = Column(Integer, primary_key=True, index=True)
    id_formulario = Column(Integer, ForeignKey("formularios.id"), nullable=False)
    titulo = Column(Text)
    codigo = Column(Text)
    orientacao_resposta = Column(Text)
    obrigatoria = Column(Boolean, default=False)
    ordem = Column(Integer)
    sub_pergunta = Column(Boolean, default=False)
    tipo_pergunta = Column(Enum(TipoPerguntaEnum), nullable=False)
