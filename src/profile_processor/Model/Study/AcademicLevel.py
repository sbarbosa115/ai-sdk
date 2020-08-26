from enum import Enum


class AcademicLevel(Enum):
    PRIMARY = 1
    ELEMENTARY = 2
    BACHELOR = 3

    @staticmethod
    def all() -> list:
        return [
            AcademicLevel.PRIMARY.value,
            AcademicLevel.ELEMENTARY.value,
            AcademicLevel.BACHELOR.value
        ]
