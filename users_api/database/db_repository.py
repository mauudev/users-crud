from users_api.api.utils import parse_db_response
from .connection import MongodbConnection
from .exceptions import (
    DataBaseError,
    NotFoundException,
    InsertError,
    UpdateError,
    DeleteError,
)
from bson.objectid import ObjectId
from dotenv import load_dotenv
import logging
import os


load_dotenv()

logger = logging.getLogger(__name__)

MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = os.getenv('MONGO_PORT')
MONGO_DATABASE = os.getenv('MONGO_DATABASE')


class DatabaseRepository:

    """
    Abastraccion para todas las operaciones comunes a la base de datos de mongo.
    Las clases hijas especifican a que coleccion ejecutar las operaciones y algunas custom operaciones.
    """

    def __init__(self):
        self._connection = MongodbConnection(MONGO_HOST, MONGO_PORT)
        self._client = self._connection.client
        self._db = self._client[MONGO_DATABASE]
        self._collection = None
    
    @property
    def collection(self):
        return self._collection
    
    @collection.setter
    def collection(self, collection: str):
        self._collection = self._db[collection]

    async def insert(self, body: dict) -> dict:
        try:
            async with await self._client.start_session() as s:
                data = {"_id": ObjectId(), **body}
                document = await self._collection.insert_one(data, session=s)
                result = await self._collection.find_one({"_id": document.inserted_id})
                return parse_db_response(result)
        except Exception as e:
            raise InsertError(f"Error al insertar el documento: {e}")

    async def get(self, id: str) -> dict:
        try:
            async with await self._client.start_session() as s:
                document = await self._collection.find_one(
                    {"_id": ObjectId(id)}, session=s
                )
                if not document:
                    raise NotFoundException(
                        f"No se encontro el documento con id: '{id}'"
                    )
                return parse_db_response(document)
        except Exception as e:
            raise DataBaseError(f"Error al obtener el documento: {e}")

    async def upsert(self, filters: dict, body: dict) -> dict:
        try:
            async with await self._client.start_session() as s:
                await self._collection.update_one(
                    filters,
                    {"$set": body},
                    upsert=True,
                    session=s,
                )
                document = await self._collection.find_one(filters, session=s)
                return parse_db_response(document)
        except Exception as e:
            raise UpdateError(f"Error al crear/actualizar el documento: {e}")

    async def get_with_filters(self, filters: list, limit=None) -> dict:
        try:
            results = []
            async with await self._client.start_session() as s:
                documents = self._collection.find({"$and": [*filters]}, session=s)
                for document in await documents.to_list(length=limit):
                    results.append(document)
            return parse_db_response(results)
        except Exception as e:
            raise DataBaseError(f"Error al obtener los documentos: {e}")

    async def get_all(self, limit=None) -> list:
        try:
            async with await self._client.start_session() as s:
                documents = await self._collection.find(session=s).to_list(length=limit)
                return parse_db_response(documents)
        except Exception as e:
            raise DataBaseError(f"Error al obtener los documentos: {e}")

    async def update(self, id: str, body: dict) -> dict:
        try:
            async with await self._client.start_session() as s:
                await self._collection.update_one(
                    {"_id": ObjectId(id)}, {"$set": body}, session=s
                )
                document = await self._collection.find_one(
                    {"_id": ObjectId(id)}, session=s
                )
                return parse_db_response(document)
        except Exception as e:
            raise UpdateError(f"Error al actualizar el documento: {e}")

    async def update_partials(self, id: str, body: dict) -> dict:
        try:
            async with await self._client.start_session() as s:
                await self._collection.update_one(
                    {"_id": ObjectId(id)}, {"$set": {**body}}, session=s
                )
                document = await self._collection.find_one(
                    {"_id": ObjectId(id)}, session=s
                )
                return parse_db_response(document)
        except Exception as e:
            raise UpdateError(f"Error al actualizar el documento: {e}")

    async def delete(self, id: str) -> dict:
        try:
            async with await self._client.start_session() as s:
                document = await self._collection.find_one(
                    {"_id": ObjectId(id)}, session=s
                )
                await self._collection.delete_one({"_id": ObjectId(id)}, session=s)
                return parse_db_response(document)
        except Exception as e:
            raise DeleteError(f"Error al eliminar el documento: {e}")
