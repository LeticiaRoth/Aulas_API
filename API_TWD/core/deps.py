#Abre e fecha o banco para fazer a injeção dentro do banco

from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

#Para dar um GET dentro do banco, precisop de uma função
async def get_session() -> Generator:
    session : AsyncSession = Session()

    #TRY
    try:
        yield session #Ele devolve a sessão, mas também a função determinada
    finally:
        await session.close() #Após utilizar a sessão so depois ele fechará o banco