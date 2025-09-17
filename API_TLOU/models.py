from typing import Optional
from pydantic import BaseModel

#Criação da classe PersonagensTLOU, com BaseModel
class PersonagensTLOU(BaseModel):
    nome: str
    faccao: str
    frase: str
    idade: str
    foto_game: str
    foto_serie: str

#Ele precisa que todos os campos ou a maioria sejam opcionais para não dar problema com o POST
class PersonagensTLOUUpdate(BaseModel):
    nome: Optional[str] = None
    faccao: Optional[str] = None
    frase: Optional[str] = None
    idade: Optional[int] = None
    foto_game: Optional[str] = None
    foto_serie: Optional[str] = None
