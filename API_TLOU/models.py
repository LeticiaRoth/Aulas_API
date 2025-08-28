from typing import Optional
from pydantic import BaseModel

#Criação da classe PersonagensTLOU, com BaseModel

class PersonagensTLOU(BaseModel):
    id: Optional[int] = None
    nome: str
    faccao:str
    frase: str
    idade: int
    foto: str
