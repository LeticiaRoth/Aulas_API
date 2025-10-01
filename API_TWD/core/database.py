#Setamos o banco que usaremos

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import  create_async_engine, AsyncEngine, AsyncSession
#De configs que está dentro de core importa a variável Settings
from core.configs import settings


#Esse código vai abrir e fechar a conexão com o nosso banco de dados

#Váriavel que recebe o AsyncEngine
engine : AsyncEngine = create_async_engine(settings.DB_URL)

#sessionmaker retorna uma classe para nós
Session : AsyncEngine = sessionmaker(
    #Vai evitar que commit automaticamente
    autocommit = False,

    #Evita uma descarga de dados sem sina
    autoflush= False,

    #Só vai expirar quando eu der o sinla
    expire_on_commit= False,
    class_=AsyncSession,

    #Pega as informações do engine
    bind=engine
)