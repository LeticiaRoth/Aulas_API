from typing import Optional
from pydantic import BaseModel

#Criação da classe PersonagensTLOU, com BaseModel
class PersonagensTLOU(BaseModel):
    nome: Optional[str] = None
    faccao: Optional[str] = None
    frase: Optional[str] = None
    idade: Optional[int] = None
    foto: Optional[str] = None

#Ele precisa que todos os campos ou a maioria sejam opcionais para não dar problema com o POST
class PersonagensTLOUUpdate(BaseModel):
    nome: Optional[str] = None
    faccao: Optional[str] = None
    frase: Optional[str] = None
    idade: Optional[int] = None
    foto: Optional[str] = None