
from pydantic.v1 import BaseSettings
from sqlalchemy.orm import declarative_base

#Coloca as configurações do projeto, passa por herança para ter todas as configurações
class Settings(BaseSettings):

    #Variavel de versionamento em casos necessários
    API_V1_STR : str = '/api/v1'

    #Pedende do banco, trocar a porta se necessário
    DB_URL : str = '/mysql+asyncmy://root@127.0.0.1:3306/bandas'

    #Todos os models herdem os recursos do sqlachemy, padronizado
    DBBaseModel = declarative_base()


class Config:
    #Não ficar dando erro em arquivos sensiveis, ignora
    case_sensitive = False
    env_file = "env"


#Importa a variavel que herda a classe
settings = Settings()

