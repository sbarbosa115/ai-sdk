import pycountry

from src.profile_processor.Model.Study.AcademicLevel import AcademicLevel
from src.profile_processor.Model.Study.AcademicStatus import AcademicStatus


def profile() -> dict:
    return {
        'name': 'Lionel Messi',
        'identification_number': '1030589045',
        'email': 'leo@example.com',
        'phone': {
            'area_code': 57,
            'number': '300 2823178',
        },
        'location': {
            'birth': {
                'country_name': pycountry.countries.get(alpha_2='CO').name,
                'country_iso_code': pycountry.countries.get(alpha_2='CO').alpha_3,
                'city': 'Bogota',
                'state': 'Bogota D.C',
            },
            'current': {
                'country_name': pycountry.countries.get(alpha_2='CO').name,
                'country_iso_code': pycountry.countries.get(alpha_2='CO').alpha_3,
                'city': 'Medellin',
                'state': 'Antioquia',
            },
        },
        'age': {
            'birth_date': '1990-09-20',
            'number': 29
        },
        'work_experience': {
            'position': 'Conductor',
            'company': 'Transmilenio S.A',
            'start_date': '2019-01-01',
            'end_date': '',
            'description': 'Conducir Buses en Diferentes Rutas',
            'sector': 'Transportes',
            'area': 'Transportes',
        },
        'studies': {
            'career': 'Ingeniero Mecanico',
            'institution': 'Universidad de Michigan',
            'level': AcademicLevel.BACHELOR,
            'status': AcademicStatus.COMPLETED,
            'start_date': '2015-01-01',
            'end_date': '2019-01-01',
        },
        'languages': {
            'language': pycountry.languages.get(alpha_3='spa').name,
            'reading_level': 10,
            'writing_level': 10,
            'listing_level': 10,
            'talking_level': 10,
        },
        'skills': [
            {
                'skill': 'Mecanizado',
                'level': 10,
            }
        ],
    }
