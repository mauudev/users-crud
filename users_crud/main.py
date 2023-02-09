# from users_crud.api.users.infra.users_routes import router as users_router
from users_crud.api.users.infra.users_routes import router as users_router
from fastapi import FastAPI


def create_server_app() -> FastAPI:
    app = FastAPI()

    app.include_router(users_router)

    return app

app = create_server_app()
