from fastapi import APIRouter
from pydantic import BaseModel
from ApiTesteCrudBasics.modules.connectDB import basicCollection,chave_acesso
import json

put_router = APIRouter(prefix="/inserir",tags=["Inserir/Atualizar Infos"])

class InsertModel(BaseModel):
    name: str
    email: str
    description: str | None = None
    chaveAcesso: str

@put_router.put("/registro")
def inserir_registro(registro : InsertModel):
    if(registro.chaveAcesso == chave_acesso):
        create_dict = {
            "idKey" : registro.email,
            "email" : registro.email,
            "name" : registro.name,
            "description" : registro.description
        }
        update_dict = {"$set":create_dict}
        update_return = basicCollection.find_one_and_update({"idKey":registro.email},update_dict,{"_id":False},return_document=True)
        if (not update_return):
            new_doc = basicCollection.insert_one(create_dict)
            return f"Registro Criado com a chave: {registro.email}"
        else :
            return f"Registro Inserido na chave: {registro.email}"
    else:
        return f"Não possui acesso ao recurso."