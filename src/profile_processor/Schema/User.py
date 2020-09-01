from src.profile_processor.Model.Study.AcademicLevel import AcademicLevel
from src.profile_processor.Model.Study.AcademicStatus import AcademicStatus
from src.profile_processor.Utils.Coerce import parse_date, sanitize_numeric, sanitize_names


def user():
    return {
        'name': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
        'identification_number': {'type': 'string', 'minlength': 0, 'maxlength': 20},
        'email': {'required': True, 'type': 'string', 'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'},
        'phone': {
            'type': 'dict', 'schema': {
                'area_code': {'required': True, 'type': 'integer', 'min': 1, 'max': 999},
                'number': {'required': True, 'type': 'string', 'minlength': 7, 'maxlength': 11, 'coerce': sanitize_numeric},
            }
        },
        'location': {
            'type': 'dict', 'required': True, 'schema': {
                'country_name': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                'country_iso_code': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 3},
                'city': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255, 'coerce': sanitize_names},
                'state': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255, 'coerce': sanitize_names},
            }
        },
        'birth_date': {'type': 'date', 'coerce': parse_date},
        'work_experience': {
            'type': 'list', 'required': True, 'schema': {
                'type': 'dict', 'schema': {
                    'position': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                    'company': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                    'start_date': {'required': True, 'type': 'date', 'coerce': parse_date},
                    'end_date': {'type': 'date', 'coerce': parse_date, 'nullable': True},
                    'description': {'type': 'string'},
                    'sector': {'type': 'string', 'minlength': 3, 'maxlength': 255},
                    'area': {'type': 'string', 'minlength': 3, 'maxlength': 255},
                }
            }
        },
        'studies': {
            'type': 'list', 'required': True, 'schema': {
                'type': 'dict', 'schema': {
                    'career': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                    'institution': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                    'level': {'required': True, 'type': 'integer', 'allowed': AcademicLevel.all()},
                    'status': {'required': True, 'type': 'integer', 'allowed': AcademicStatus.all()},
                    'start_date': {'required': True, 'type': 'date', 'coerce': parse_date},
                    'end_date': {'type': 'date', 'coerce': parse_date, 'nullable': True},
                }
            }
        },
        'languages': {
            'type': 'list', 'required': True, 'schema': {
                'type': 'dict', 'schema': {
                    'language': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                    'reading_level': {'required': True, 'contains': ['item']},
                    'writing_level': {'required': True, 'contains': ['item']},
                    'listening_level': {'required': True, 'contains': ['item']},
                    'speaking_level': {'required': True, 'contains': ['item']},
                }
            },
        },
        'skills': {
            'type': 'list', 'schema': {
                'type': 'string'
            }
        },
    }
