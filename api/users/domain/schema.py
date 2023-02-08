from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List, Union, Dict

class UserModel(BaseModel):
    username: str = Field(..., description="Nombre del usuario")
    email: str = Field(..., description="Correo electronico del usuario")
    password: str = Field(..., description="Contrasena del usuario")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Fecha de creacion del usuario")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Fecha de actualizacion del usuario")

class UserResponseModel(BaseModel):
    id: str = Field(..., description="Id del usuario")
    username: str = Field(..., description="Nombre del usuario")
    email: str = Field(..., description="Correo electronico del usuario")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Fecha de creacion del usuario")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Fecha de actualizacion del usuario")
