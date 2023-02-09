from users_crud.database.db_repository import DatabaseRepository


class UsersRepository(DatabaseRepository):
    def __init__(self):
        super(UsersRepository, self).__init__()
        self._collection = self._db.users
