from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class UserModel(BaseModel):
    username: str = Field(..., description="Nombre del usuario")
    email: str = Field(..., description="Correo electronico del usuario")
    password: str = Field(..., description="Contrasena del usuario")
    logged_in: Optional[bool] = Field(False, description="Si el usuario ha iniciado sesion or not")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Fecha de creacion del usuario")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Fecha de actualizacion del usuario")

class UserResponseModel(UserModel):
    id: str = Field(..., description="Id del usuario")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Fecha de creacion del usuario")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Fecha de actualizacion del usuario")
