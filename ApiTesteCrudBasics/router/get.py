from fastapi import APIRouter
import pymongo
get_router = APIRouter(prefix="/buscar",tags=["Puxar Infos"])

@get_router.get("/registro")
def get_registro(id):
    return f"buscando registros... {id}"

@get_router.get("/registro/{id}")
def get_registro(id):
    return f"segue retorno do registro: {id}"