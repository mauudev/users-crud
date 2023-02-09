from users_crud.api.users.application.users_handler import UsersHandler
from users_crud.api.users.domain.schema import UserModel, UserResponseModel
from users_crud.api.shared import Logger
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List, Union


logger = Logger()

users_handler = UsersHandler(logger)

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={},
)

@router.post("/create", response_model=UserResponseModel, operation_id="create_user")
async def create_user(body: UserModel) -> UserResponseModel:
    try:
        new_user = await users_handler.create_user(jsonable_encoder(body))
        return UserResponseModel(**new_user)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.get("/", operation_id="get_all_users")
async def get_all_users() -> List[Union[UserResponseModel, None]]:
    try:
        users = await users_handler.all_users()
        return users
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
 
@router.get("/login/{id}", response_model=UserResponseModel, operation_id="login_user")
async def login_user(id: str) -> UserResponseModel:
    try:
        user_data = await users_handler.get_user(id)
        user_data['logged_in'] = True
        user_data = await users_handler.update_user(id, jsonable_encoder(user_data))
        return UserResponseModel(**user_data)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.get("/logout/{id}", response_model=UserResponseModel, operation_id="logout_user")
async def login_user(id: str) -> UserResponseModel:
    try:
        user_data = await users_handler.get_user(id)
        user_data['logged_in'] = False
        user_data = await users_handler.update_user(id, jsonable_encoder(user_data))
        return UserResponseModel(**user_data)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
