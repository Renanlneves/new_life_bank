from ast import Num
from pydantic import BaseModel, Field
import uvicorn
from typing import Dict
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

accounts = []

class Account(BaseModel):
    id: int
    nome: str
    documento: str
    dataNacimento: str
    email: str
    telefone: str

@app.get("/")
def root() -> str:
    return "hello World"

@app.get("/health")
def alive() -> Dict[str, datetime]:
    return {"timestamp": datetime.now()}

@app.post("/accounts", response_model=bool, tags=["accounts"])
def create_account(account: Account):

    accounts.append(account)
    
    return True

#pegando os dados das contas.
@app.get("/accounts", response_model=list ,tags=["accounts"])
def get_account():

    return accounts


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True) 
