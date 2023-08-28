#ParteDoAzure
import logging
import azure.functions as func

from fastapi import FastAPI,Request

#Importar os "router's" para deixar mais organizado
from ApiTesteCrudBasics.router.get import get_router
from ApiTesteCrudBasics.router.put import put_router
from ApiTesteCrudBasics.router.delete import delete_router

#Cria o brabo
app = FastAPI()


#Importante para o AzureFunctions
async def main(req: func.HttpRequest,context: func.Context) -> func.HttpResponse:
    return await func.AsgiMiddleware(app).handle_async(req,context)

#Adicionando roteadores
app.include_router(get_router)
app.include_router(put_router)
app.include_router(delete_router)