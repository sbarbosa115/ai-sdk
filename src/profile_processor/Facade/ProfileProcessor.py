from cerberus import Validator
from src.profile_processor.Schema.User import user


class ProfileProcessor:

    @staticmethod
    def validate(user_schema: dict) -> dict:
        v = Validator()
        v.validate(user_schema, user())
        return v.errors

    @staticmethod
    def save() -> dict:
        return True

    @staticmethod
    def process(user_schema: dict) -> dict:
        v = Validator()
        v.validate(user_schema, user())
        if len(v.errors) == 0:
            return v.document

        return v.errors
