from fastapi import FastAPI, HTTPException, Depends 
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, List
from modelsPydantic import modeloUsuario, modeloAuth
from genToken import createToken
from middlewares import BearerJWT
from DB.conexion import Session, engine, Base 
from models.modelsDB import User
from fastapi import APIRouter

routerUsuario = APIRouter()

# Endpoint CONSULTA TODOS
@routerUsuario.get("/todoUsuarios", tags=["Operaciones CRUD"])
def leer_usuarios():
    db = Session()
    try:
        consulta = db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    except Exception as e:
        return JSONResponse(status_code=500,
                            content={"message": "Error al Consultar",
                            "Exception":str(e)})
    finally:
        db.close()


#Endpoint buscar por id
@routerUsuario.get('/usuario/{id}', tags=["Operaciones CRUD"])
def buscarUno(id: int):
    db = Session()
    try:
        consultauno = db.query(User).filter(User.id == id).first()

        if not consultauno:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})

        return JSONResponse(content=jsonable_encoder(consultauno))

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "mensaje": "Error al consultar",
                "excepcion": str(e)
            }
        )

    finally:
        db.close()

#endpoint Agregar nuevos
@routerUsuario.post('/usuario/', response_model= modeloUsuario, tags=['Operaciones CRUD'])
def agregarUsuario(usuario: modeloUsuario):
    db = Session()
    try:
        db.add(User(**usuario.model_dump()))
        db.commit()
        return JSONResponse(status_code=201,
                            content={"message": "Usuario Guardado",
                            "usuario": usuario.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"message": "Error al Guardar al Usuario",
                            "Exception":str(e)})
    finally:
        db.close()
# Endpoint Actualizar Usuarios
@routerUsuario.put('/usuario/{id}', tags=['Operaciones CRUD'])
def actualizarUsuario(id: int, usuarioActualizado: modeloUsuario):
    db = Session()
    try:
        usuario_db = db.query(User).filter(User.id == id).first()

        if not usuario_db:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})

        # Actualizamos los campos
        usuario_db.nombre = usuarioActualizado.nombre
        usuario_db.edad = usuarioActualizado.edad
        usuario_db.correo = usuarioActualizado.correo

        db.commit()
        return JSONResponse(content={"mensaje": "Usuario actualizado correctamente"})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"mensaje": "Error al actualizar", "Exception": str(e)})
    finally:
        db.close()

# Endpoint Eliminar Usuarios
@routerUsuario.delete('/usuario/{id}', tags=['Operaciones CRUD'])
def eliminarUsuario(id: int):
    db = Session()
    try:
        usuario_db = db.query(User).filter(User.id == id).first()

        if not usuario_db:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})

        db.delete(usuario_db)
        db.commit()
        return JSONResponse(content={"mensaje": "Usuario eliminado correctamente"})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"mensaje": "Error al eliminar", "Exception": str(e)})
    finally:
        db.close()
