from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import List
from models import Licencia, modeloUsuario, modeloAuth
import re

app = FastAPI(
    title="Gestión de Licencias",
    description="API para gestionar licencias de conducción",
    version="1.0.0"
)


fake_db = [
    {"numero_licencia": "ABC123456789", "nombre": "Gerson Pastrana", "tipo_licencia": "A"},
    {"numero_licencia": "XYZ987654321", "nombre": "Sergio perez", "tipo_licencia": "B"}
]

@app.get("/")
def home():
    return {"mensaje": "HOLA MUNDO"}


@app.get("/buscar/{numero_licencia}", tags=["Operaciones CRUD"])
def buscar_licencia(numero_licencia: str):
    for licencia in fake_db:
        if licencia["numero_licencia"] == numero_licencia:
            return licencia
    raise HTTPException(status_code=404, detail="Licencia no encontrada")


@app.post("/agregar", response_model=Licencia, tags=["Operaciones CRUD"])
def agregar_licencia(licencia: Licencia):
    for lic in fake_db:
        if lic["numero_licencia"] == licencia.numero_licencia:
            raise HTTPException(status_code=400, detail="La licencia ya existe")
    fake_db.append(licencia.dict())
    return licencia


@app.delete("/eliminar/{numero_licencia}", tags=["Operaciones CRUD"])
def eliminar_licencia(numero_licencia: str):
    for licencia in fake_db:
        if licencia["numero_licencia"] == numero_licencia:
            fake_db.remove(licencia)
            return {"message": "Licencia eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="Licencia no encontrada")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)










