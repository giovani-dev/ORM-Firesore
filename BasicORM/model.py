from typing import NamedTuple, Any, List
from BasicORM.connection import DataBaseConnection
from BasicORM.validate import BaseModelValidations


class FilterConditional(NamedTuple):
    field: str
    conditional: str
    value: Any


# class DefineBaseModel(object):

class PostOperations(DataBaseConnection):

    def __init__(self):
        super().__init__()
        self.instance: object = self.db.collection(self.__class__.__name__)

    def create(self) -> dict:
        if not self.id:
            self.instance: object = self.instance.document()
        else:
            self.instance: object = self.instance.document(self.id)
        self.instance.set(self.fields)
        return self.fields

    def update(self, doc) -> dict:
        self.instance: object = self.instance.document(doc)
        self.instance.set(self.fields)
        return self.fields


class GetOperations(DataBaseConnection):

    def __init__(self):
        super().__init__()
        self.instance: object = self.db.collection(self.__class__.__name__)

    def get(self, doc) -> dict:
        self.instance: object = self.instance.document(doc)
        return self.instance.get().to_dict()

    def all(self) -> object:
        # self.instance = self.db.collection(self.__class__.__name__)
        return self.__dict__()

    def filter(self, conditionals: List[FilterConditional]) -> object:
        for filter_cond in conditionals:
            self.instance: object = self.instance.where(filter_cond.field, filter_cond.conditional, filter_cond.value)
        return self

    def exists(self):
        ...


class BaseModel(PostOperations, GetOperations):
    id: str = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validate: object = BaseModelValidations
        self.validate.is_custom_fields(sended=kwargs.keys(), class_fields=self.__class__.__annotations__.keys())
        self.fields: dict = self.__class__.__dict__.items()
        self.fields.update(kwargs)
        self.data: dict = None

    def __iter__(self):
        self.data = self.instance
        return iter(self.data)

    def __dict__(self):
        self.data = self.instance
        return self.data

    @property
    def data(self) -> object:
        return self._data

    @data.setter
    def data(self, value: object) -> None:
        if value:
            to_data = dict()
            for doc in value.stream():
                to_data.update({doc.id: doc.to_dict()})
            self._data = to_data
        else:
            self._data = value

    @property
    def fields(self) -> dict:
        return self._fields

    @fields.setter
    def fields(self, class_variables: dict) -> None:
        self._fields: dict = {key: value for key, value in class_variables if
                              self.validate.is_key(key) and self.validate.is_value(value) and not key == "id"}
