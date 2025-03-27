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
from fastapi import APIRouter

routerAuth = APIRouter()

# Endpoint autenticación
@routerAuth.post('/auth',  tags=['Autentificación'])
def login(autorizacion: modeloAuth):
    if autorizacion.email == "mario@gmail.com" and autorizacion.passw == "123456789":
        token:str = createToken(autorizacion.model_dump())
        print(token)
        return JSONResponse(content=token)
    else:
        return {"Aviso": "Credenciales incorrectas"}
