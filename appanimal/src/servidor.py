from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4


app = FastAPI()

class Animal(BaseModel):
     id: Optional[str]
     nome: str
     idade: int
     cor: str
     sexo: str


banco: list[Animal] = []


@app.get('/animal')
def lista_animal():
    return banco


@app.get('/animal/{animal_id}')
def buscar_animal(animal_id: str):
    for animal in banco:
        if animal.id == animal_id:
            return animal
    

@app.post('/animal')
def cadastra_animal(animal: Animal):
    animal.id = str (uuid4())
    banco.append(animal)
    return None


@app.delete('/animal/{animal_id}')
async def delete_item(animal_id: str):
    posicao = -1
    for index, animal in enumerate(banco):
      if animal.id == animal_id:
        posicao = index
        break
    
    if posicao != -1:
        banco.pop(posicao)
        return {"mensagem": f"Item {animal_id} excluído com sucesso."}
    else:
        return {"erro": f"Item {animal_id} não encontrado."}
        
