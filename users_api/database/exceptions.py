class GeneralError(Exception):
    def __init__(self, message, metadata=None):
        super(GeneralError, self).__init__(message)
        self._metadata = metadata

    @property
    def metadata(self):
        return self._metadata


class DataBaseError(GeneralError):
    def __init__(self, message, metadata=None):
        super(DataBaseError, self).__init__(message, metadata)


class NotFoundException(GeneralError):
    def __init__(self, message, metadata=None):
        super(NotFoundException, self).__init__(message, metadata)


class DuplicatedException(GeneralError):
    def __init__(self, message, metadata=None):
        super(DuplicatedException, self).__init__(message, metadata)


class InsertError(GeneralError):
    def __init__(self, message, metadata=None):
        super(InsertError, self).__init__(message, metadata)


class UpdateError(GeneralError):
    def __init__(self, message, metadata=None):
        super(UpdateError, self).__init__(message, metadata)


class DeleteError(GeneralError):
    def __init__(self, message, metadata=None):
        super(DeleteError, self).__init__(message, metadata)
