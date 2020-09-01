from enum import Enum


class AcademicLevel(Enum):
    NO_ACADEMIC_LEVEL = 0
    PRIMARY = 1
    HIGH_SCHOOL = 2
    TECHNICAL = 3
    TECHNOLOGIST = 4
    PROFESSIONAL_TECHNICIAN = 5
    PROFESSIONAL = 6
    SPECIALIZATION = 7
    MASTERS_DEGREE = 8
    DOCTORATE = 9

    @staticmethod
    def all() -> list:
        return [
            AcademicLevel.NO_ACADEMIC_LEVEL.value,
            AcademicLevel.PRIMARY.value,
            AcademicLevel.HIGH_SCHOOL.value,
            AcademicLevel.TECHNICAL.value,
            AcademicLevel.TECHNOLOGIST.value,
            AcademicLevel.PROFESSIONAL_TECHNICIAN.value,
            AcademicLevel.PROFESSIONAL.value,
            AcademicLevel.SPECIALIZATION.value,
            AcademicLevel.MASTERS_DEGREE.value,
            AcademicLevel.DOCTORATE.value
        ]
