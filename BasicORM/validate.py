from BasicORM.errors import FieldDoesNotExist


class BaseModelValidations(object):

    @staticmethod
    def is_value(value: object) -> bool:
        return isinstance(value, (float, int, str, list, dict, tuple))

    @staticmethod
    def is_key(key: str) -> bool:
        return not "__" in key

    @staticmethod
    def is_custom_fields(sended: list, class_fields: list) -> bool:
        for field in sended:
            if not field in class_fields:
                raise FieldDoesNotExist(field)
        return True
