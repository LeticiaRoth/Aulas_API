from core.configs import settings
from sqlalchemy import Column, Integer, String, Float, Boolean


class BandasModel(settings.DBBaseModel):
    __tablename__ = "bandas"

    #Campos da minha tabela
    id : int = Column(Integer(), primary_key=True, autoincrement =True)
    nome : str = Column(String(230))
    qtd_integrante : int = Column(Integer())
    tipo_musical : int = Column(String(250))
