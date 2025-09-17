from typing import Optional
from pydantic import BaseModel as SCBaseModel


class BandasSchema(SCBaseModel):
    
    id : Optional[int] = None
    nome : str
    qtd_integrantes : int
    tipo_musical : str


    class Config:
        #Esse schemas vai ser JSON, mas fara a comunicação com o Banco de Dados
        orm_mode = True

        