from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from  app.usecases.formulario import FormularioUseCase
from  app.api.v1.schemas.formulario import FormularioCreate, FormularioOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[FormularioOut])
def listar_formularios(db: Session = Depends(get_db)):
    return FormularioUseCase(db).listar_formularios()

@router.post("/", response_model=FormularioOut)
def criar_formulario(formulario: FormularioCreate, db: Session = Depends(get_db)):
    return FormularioUseCase(db).criar_formulario(formulario.dict())

@router.delete("/{formulario_id}")
def deletar_formulario(formulario_id: int, db: Session = Depends(get_db)):
    FormularioUseCase(db).deletar_formulario(formulario_id)
    return {"message": "Formulário deletado com sucesso"}