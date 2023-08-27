from fastapi import APIRouter
import pymongo
delete_router = APIRouter(prefix="/deletar",tags=["Deletar Infos"])

@delete_router.delete("/registro/{id}")
def get_registro(id):
    return f"segue status da deleção do registro: {id}"