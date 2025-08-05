from sqlalchemy import Column, Integer, ForeignKey
from app.core.database import Base

class OpcaoRespostaPergunta(Base):
    __tablename__ = "opcoes_resposta_pergunta"
    id = Column(Integer, primary_key=True, index=True)
    id_opcao_resposta = Column(Integer, ForeignKey("opcoes_resposta.id"), nullable=False)
    id_pergunta = Column(Integer, ForeignKey("perguntas.id"), nullable=False)
