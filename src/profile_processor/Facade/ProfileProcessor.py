from cerberus import Validator
from src.profile_processor.Schema.User import user


class ProfileProcessor:

    @staticmethod
    def validate(user_schema: dict) -> dict:
        v = Validator()
        v.validate(user_schema, user())
        return v.errors

    @staticmethod
    def sanitize() -> dict:
        return True

    @staticmethod
    def save() -> dict:
        return True

    @staticmethod
    def process() -> dict:
        return True
