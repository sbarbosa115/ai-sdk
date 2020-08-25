from cerberus import Validator
from src.profile_processor.Schema.User import user


class ProfileProcessor:

    @staticmethod
    def validate(user_schema: dict) -> bool:
        v = Validator()
        v.validate(user_schema, user())
        return v.errors

    @staticmethod
    def sanitize() -> bool:
        return True

    @staticmethod
    def save() -> bool:
        return True

    @staticmethod
    def process() -> bool:
        return True
