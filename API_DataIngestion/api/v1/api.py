from fastapi import APIRouter
from api.v1.endpoinst import bandas

api_router = APIRouter()
api_router.include_router(bandas.router, prefix='/bandas', tags=['Bandas'])