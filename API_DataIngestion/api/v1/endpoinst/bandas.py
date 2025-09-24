from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

# SQLAlchemy Async
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# Schemas e Models
from models.bandas_models import BandasModel
from schemas.bandas_schemas import BandasSchema
from core.deps import get_session

router = APIRouter()

# POST COM O BANCO DE DADOS
# Post não tem ID (pois é criado pelo banco)
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BandasSchema)
async def post_banda(banda: BandasSchema, db: AsyncSession = Depends(get_session)):
    # Cria uma nova banda com dados recebidos via body (BandasSchema)
    nova_banda = BandasModel(
        nome=banda.nome,
        qtd_integrante=banda.qtd_integrante,
        tipo_musical=banda.tipo_musical
    )
    async with db as session:
        session.add(nova_banda)
        await session.commit()# Salva no banco
        await session.refresh(nova_banda) # Atualiza a instância com dados do DB (ex: id)
    return nova_banda


# GET COM CONEXÃO COM O BANCO
@router.get("/", response_model=List[BandasSchema])
async def get_bandas(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(BandasModel)
        result = await session.execute(query)
        bandas: List[BandasModel] = result.scalars().all() # Pega todas as bandas
    return bandas


# GET POR ID
@router.get("/{banda_id}", response_model=BandasSchema, status_code=status.HTTP_200_OK)
async def get_banda(banda_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        # Consulta banda pelo ID
        query = select(BandasModel).filter(BandasModel.id == banda_id)
        result = await session.execute(query)
        banda = result.scalar_one_or_none()  

        if banda:
            return banda
        else:
            raise HTTPException(
                detail="Banda não encontrada",
                status_code=status.HTTP_404_NOT_FOUND
            )


# PUT COM CONEXÃO
@router.put("/{banda_id}", response_model=BandasSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_banda(banda_id: int, banda: BandasSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(BandasModel).filter(BandasModel.id == banda_id)
        result = await session.execute(query)
        banda_up = result.scalar_one_or_none()

        if banda_up:
            # Atualiza os dados da banda encontrada
            banda_up.nome = banda.nome
            banda_up.qtd_integrante = banda.qtd_integrante
            banda_up.tipo_musical = banda.tipo_musical

            await session.commit()        # Salva alteração
            await session.refresh(banda_up) # Atualiza a instância
            return banda_up
        else:
            raise HTTPException(
                detail="Banda não encontrada",
                status_code=status.HTTP_404_NOT_FOUND
            )


# DELETE COM CONEXÃO
@router.delete("/{banda_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_banda(banda_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(BandasModel).filter(BandasModel.id == banda_id)
        result = await session.execute(query)
        banda_del = result.scalar_one_or_none()

        if banda_del:
            await session.delete(banda_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(
                detail="Banda não deletada ou encontrada",
                status_code=status.HTTP_404_NOT_FOUND
            )
