from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.usecases.pergunta import PerguntaUseCase
from app.api.v1.schemas.pergunta import PerguntaCreateToDb, PerguntaOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/formulario/{formulario_id}", response_model=list[PerguntaOut])
def listar_perguntas(formulario_id: int, db: Session = Depends(get_db)):
    return PerguntaUseCase(db).listar_por_formulario(formulario_id)

@router.post("/", response_model=PerguntaOut)
def criar_pergunta(pergunta: PerguntaCreateToDb, db: Session = Depends(get_db)):
    return PerguntaUseCase(db).criar_pergunta(pergunta.dict())

@router.delete("/{pergunta_id}")
def deletar_pergunta(pergunta_id: int, db: Session = Depends(get_db)):
    PerguntaUseCase(db).deletar_pergunta(pergunta_id)
    return {"message": "Pergunta deletada com sucesso"}
