from pydantic import BaseModel, Field, EmailStr

email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

#Modelo de validaciones
class modeloUsuario(BaseModel):
    id: int = Field(...,gt=0, description="ID unico y solo numeros positivos")
    nombre: str = Field(..., min_length=3, max_length=85, description="solo caracteres minimo 3 y maximo 85")
    edad: int = Field(...,gt=0, lt=99, description="ID unico y solo numeros positivos")
    email: EmailStr = Field(..., description="Correo electrónico válido")

class modeloAuth(BaseModel):
    email:EmailStr = Field(..., description="Correo Electronico valido", example="correo@example.com")
    passw: str = Field(..., min_length=8, strip_withespace=True, description="Contraseña  minimo 8 caracteres")