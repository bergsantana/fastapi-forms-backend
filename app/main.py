from fastapi import FastAPI
from app.api.v1.controller import formulario
from app.api.v1.controller import pergunta
from app.core.database import Base, engine
import os

 
app = FastAPI(title="API de Formulários")

# Cria as tabelas
Base.metadata.create_all(bind=engine)

# Rotas
app.include_router(formulario.router, prefix="/api/v1/formularios", tags=["Formulários"])
app.include_router(pergunta.router, prefix="/api/v1/perguntas", tags=["Perguntas"])


@app.on_event("startup")
def log_routes():
    port = os.getenv("PORT", 8000)
    host = os.getenv("HOST", "localhost")
    
    print(f"\n🚀 Aplicação disponível em: http://{host}:{port}\n")
    print("📚 Rotas disponíveis:")
    for route in app.routes:
        if hasattr(route, "methods"):
            methods = ','.join(route.methods)
            print(f"{methods:10} {route.path}")