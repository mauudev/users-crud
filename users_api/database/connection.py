from motor.motor_asyncio import AsyncIOMotorClient


class MongodbConnection:
    def __init__(self, host, port, user=None, password=None):
        if user and password:
            self._db_client = AsyncIOMotorClient(
                f"mongodb://{user}:{password}@{host}:{port}"
            )
        else:
            self._db_client = AsyncIOMotorClient(f"mongodb://{host}:{port}")

    @property
    def client(self):
        return self._db_client
