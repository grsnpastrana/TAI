from fastapi import FastAPI, HTTPException, Depends 
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, List
from modelsPydantic import modeloUsuario, modeloAuth
from genToken import createToken
from middlewares import BearerJWT
from DB.conexion import Session, engine, Base 
from models.modelsDB import User
from routers.usuario import routerUsuario
from routers.auth import routerAuth




app = FastAPI(
    title='Mi Primer API 192',
    description='Gerson',
    version='1.0.1'
)

app.include_router(routerUsuario)
app.include_router(routerAuth)
Base.metadata.create_all(bind=engine)




# Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello': 'world FastAPI'}

