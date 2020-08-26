from enum import Enum


class AcademicStatus(Enum):
    COMPLETED = 1
    STUDYING = 2
    WITHDRAW = 3

    @staticmethod
    def all() -> list:
        return [
            AcademicStatus.COMPLETED.value,
            AcademicStatus.STUDYING.value,
            AcademicStatus.WITHDRAW.value
        ]
