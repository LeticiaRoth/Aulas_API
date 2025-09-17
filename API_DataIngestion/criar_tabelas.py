from core.configs import settings
from core.database import engine
from models import all_models

async def create_table() -> None:
    print("Criando tabelas no banco")


    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop.all)

        await conn.run_sync(settings.DBBaseModel.metadata.create.all)

    print("Tabelas criadas com sucesso")



if __name__ == "__main__":
    import asyncio

    asyncio.run(create_table())
