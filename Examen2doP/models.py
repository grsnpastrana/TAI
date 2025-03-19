from pydantic import BaseModel, Field, EmailStr


class Licencia(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100, description="Nombre completo")
    tipo_licencia: str = Field(..., pattern="^(A|B|C|D)$", description="Tipo de licencia debe ser A, B, C o D")
    numero_licencia: str = Field(..., min_length=12, max_length=12, pattern="^[A-Z0-9]{12}$", description="Número de licencia debe ser alfanumérico de 12 caracteres")


class modeloUsuario(BaseModel):
    id: int = Field(..., gt=0, description="ID único y solo números positivos")
    nombre: str = Field(..., min_length=3, max_length=85, description="Solo caracteres, mínimo 3 y máximo 85")
    edad: int = Field(..., gt=0, lt=99, description="Edad debe ser un número positivo menor de 99")
    email: EmailStr = Field(..., description="Correo electrónico válido")

class modeloAuth(BaseModel):
    email: EmailStr = Field(..., description="Correo Electrónico válido", example="correo@example.com")
    passw: str = Field(..., min_length=8, strip_whitespace=True, description="Contraseña mínimo 8 caracteres")
