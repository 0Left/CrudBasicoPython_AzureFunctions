#ParteDoAzure
import logging
import azure.functions as func

#para lidar com arquivos e infos de ambiente
import os
import sys

#buscar o aquivo .env
from dotenv import load_dotenv

#oq eu vou usar de importante
import pymongo
import fastapi
from pydantic import BaseModel

#Importar os "router's" para deixar mais organizado
from ApiTesteCrudBasics.router.router import router

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
app.include_router(router)