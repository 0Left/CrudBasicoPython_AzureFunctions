from fastapi import APIRouter
from ApiTesteCrudBasics.modules.connectDB import basicCollection
get_router = APIRouter(prefix="/buscar",tags=["Puxar Infos"])

@get_router.get("/registro")
def get_registro():
    registros = list(basicCollection.find(projection={"_id":False}))
    return f"Seguem 10 primeiros registros: {registros[0:10]}"

@get_router.get("/registro/{id}")
def get_registro(id):
    registro = basicCollection.find_one({"idKey":id},projection={"_id":False})
    if (registro):
        return f"Segue retorno do registro: {registro}"
    else:
        return f"Registro não encontrado"