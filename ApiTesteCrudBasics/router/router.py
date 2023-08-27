from fastapi import APIRouter
router = APIRouter()

@router.get("/registro/{id}")
def get_registro(id):
    return f"registro {id}"