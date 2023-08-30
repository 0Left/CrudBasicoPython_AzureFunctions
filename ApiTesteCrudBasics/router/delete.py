from fastapi import APIRouter
from pydantic import BaseModel
from ApiTesteCrudBasics.modules.connectDB import basicCollection,chave_acesso

from dotenv import load_dotenv
import os

delete_router = APIRouter(prefix="/deletar",tags=["Deletar Infos"])
class DeleteModel(BaseModel):
    chaveAcesso: str
    email: str

@delete_router.delete("/registro")
def get_registro(delete_model : DeleteModel):
    if(delete_model.chaveAcesso == chave_acesso):
        deletado = basicCollection.find_one_and_delete({"idKey":delete_model.email},projection={"_id":False})
        if(deletado):
            return f"Registro deletado: {deletado}"
        else:
            return f"Registro não encontrado"
    else:
        return f"Não possui acesso ao recurso."





