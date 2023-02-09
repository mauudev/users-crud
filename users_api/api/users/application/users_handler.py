from users_api.api.users.domain.users_repository import UsersRepository


class UsersHandler:
    def __init__(self, logger):
        self._repository = UsersRepository()
        self._logger = logger
    
    async def create_user(self, user_data):
        self._logger.info(f"Creando nuevo usuario: {user_data}")
        new_user = await self._repository.insert(user_data)
        self._logger.info("Usuario creado con exito.")
        return new_user

    async def all_users(self):
        self._logger.info("Obteniendo todos los usuarios ..")
        return await self._repository.get_all()

    async def get_user(self, user_id):
        self._logger.info(f"Obteniendo usuario con el id: '{user_id}'")
        return await self._repository.get(user_id)
    
    async def update_user(self, user_id, data):
        self._logger.info(f"Actualizando datos de usuario con el id: '{user_id}'")
        return await self._repository.update(user_id, data)
