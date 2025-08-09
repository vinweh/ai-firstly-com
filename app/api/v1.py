from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Echo(BaseModel):
    msg: str

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/echo")
def echo(body: Echo):
    return {"you_said": body.msg}
