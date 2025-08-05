from sqlalchemy  import Column, Integer, Text
from app.core.database import Base

class Formulario(Base):
    __tablename__ = "formularios"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(Text, nullable=False)
    descricao = Column(Text)
    ordem = Column(Integer)