from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.usecases.resposta  import RespostaUseCase
from app.api.v1.schemas.opcoes_respostas import  OpcoesRespostaCreate
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

 
@router.post("/"  )
def criar_respotas(respostas: list[OpcoesRespostaCreate], db: Session = Depends(get_db)):
    return  RespostaUseCase(db).criar_respostas(respostas.dict())
 