#ParteDoAzure
import logging
import azure.functions as func

#para lidar com arquivos e infos de ambiente
import os
import sys

#buscar o aquivo .env
from dotenv import load_dotenv

import pymongo
import fastapi
from pydantic import BaseModel

app = fastapi.FastAPI()

async def main(req: func.HttpRequest,context: func.Context) -> func.HttpResponse:
    return await func.AsgiMiddleware(app).handle_async(req,context)

@app.get("/teste")
async def teste():
    return "opa"