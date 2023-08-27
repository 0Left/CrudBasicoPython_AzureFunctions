#ParteDoAzure
import logging
import azure.functions as func

#para lidar com arquivos e infos de ambiente
import os
import sys

#buscar o aquivo .env
from dotenv import load_dotenv

import fastapi

#Importar os "router's" para deixar mais organizado
from ApiTesteCrudBasics.router.get import get_router
from ApiTesteCrudBasics.router.put import put_router
from ApiTesteCrudBasics.router.delete import delete_router

#Cria o brabo
app = fastapi.FastAPI()

#Importante para o AzureFunctions
async def main(req: func.HttpRequest,context: func.Context) -> func.HttpResponse:
    return await func.AsgiMiddleware(app).handle_async(req,context)
#adicionando uma rota
@app.get("/teste")
async def teste():
    return "opa"
#Adicionando um roteador
app.include_router(get_router)
app.include_router(put_router)
app.include_router(delete_router)