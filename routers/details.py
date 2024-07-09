from fastapi import APIRouter


router = APIRouter()

@router.get("/")
def index():
    return "Index Details Route"


@router.get("/{name}")
def get_id(name):
    return {
        "data" : name
    }