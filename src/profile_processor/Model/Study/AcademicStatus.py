from enum import Enum


class AcademicStatus(Enum):
    NO_ACADEMIC_STATUS = 0
    COMPLETED = 1
    STUDYING = 2
    WITHDRAW = 3

    @staticmethod
    def all() -> list:
        return [
            AcademicStatus.NO_ACADEMIC_STATUS.value,
            AcademicStatus.COMPLETED.value,
            AcademicStatus.STUDYING.value,
            AcademicStatus.WITHDRAW.value
        ]
