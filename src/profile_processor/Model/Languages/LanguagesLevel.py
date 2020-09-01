from enum import Enum


class LanguageLevel(Enum):
    NO_LANGUAGE_LEVEL = 0
    LEARNING = 1
    BASIC = 2
    INTERMEDIATE = 3
    UPPER_INTERMEDIATE = 4
    ADVANCED = 5
    NATIVE = 6

    @staticmethod
    def all() -> list:
        return [
            LanguageLevel.NO_LANGUAGE_LEVEL.value,
            LanguageLevel.LEARNING.value,
            LanguageLevel.BASIC.value,
            LanguageLevel.INTERMEDIATE.value,
            LanguageLevel.UPPER_INTERMEDIATE.value,
            LanguageLevel.ADVANCED.value,
            LanguageLevel.NATIVE.value
        ]
