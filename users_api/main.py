from users_api.api.users.infra.users_routes import router as users_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_server_app() -> FastAPI:
    app = FastAPI()

    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(users_router)

    return app

app = create_server_app()
