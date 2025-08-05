from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from app.core.database import Base

class OpcaoResposta(Base):
    __tablename__ = "opcoes_resposta"
    id = Column(Integer, primary_key=True, index=True)
    id_pergunta = Column(Integer, ForeignKey("perguntas.id"), nullable=False)
    resposta = Column(Text)
    ordem = Column(Integer)
    resposta_aberta = Column(Boolean, default=False)
