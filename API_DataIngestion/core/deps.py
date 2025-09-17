from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session


#Método GET - preciso da função
async def get_session() -> Generator:
    sesssion : AsyncSession = Session()

    try:
        #Tenta retornar o generator, sem ter o finale mantem ele, mantem viva enquanto eu precisar dela
        yield sesssion
    finally:
        await sesssion.close()