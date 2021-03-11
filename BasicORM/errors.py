

class ORMBaseException(Exception):
    def __init__(self):
        self.message = ""
        super().__init__()

    def __str__(self):
        return self.message


class FieldDoesNotExist(ORMBaseException):
    def __init__(self, field: str):
        self.message = f"This field '{field}' is not avaible"
