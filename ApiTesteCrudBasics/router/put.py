from fastapi import APIRouter
from pydantic import BaseModel

import pymongo

put_router = APIRouter(prefix="/inserir",tags=["Inserir/Atualizar Infos"])

class Item(BaseModel):
    name: str
    email: str
    description: str | None = None

@put_router.put("/registro")
def inserir_registro(registro : Item):
    return f"registro Inserido: {registro}"