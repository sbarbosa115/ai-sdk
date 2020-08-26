from src.profile_processor.Model.Study.AcademicLevel import AcademicLevel
from src.profile_processor.Model.Study.AcademicStatus import AcademicStatus
from src.profile_processor.Utils import Coerce
from src.profile_processor.Utils.Coerce import parse_date


def user():
    return {
        'name': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
        'identification_number': {'type': 'string', 'minlength': 0, 'maxlength': 20},
        'email': {'required': True, 'type': 'string', 'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'},
        # Pending to add Email Validation
        'phone': {
            'type': 'dict', 'schema': {
                'area_code': {'required': True, 'type': 'integer', 'min': 1, 'max': 999},
                'number': {'required': True, 'type': 'string', 'minlength': 7, 'maxlength': 11},
            }
        },
        'location': {
            # same that current if not present.
            'type': 'dict', 'required': True, 'schema': {
                'birth': {
                    'type': 'dict', 'schema': {
                        'country_name': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                        'country_iso_code': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 3},
                        'city': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                        'state': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                    }
                },
                'current': {
                    'type': 'dict', 'schema': {
                        'country_name': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                        'country_iso_code': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 3},
                        'city': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                        'state': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                    }
                },
            }
        },
        'age': {
            'type': 'dict', 'required': True, 'schema': {
                'birth_date': {'type': 'date', 'coerce': parse_date},
                'number': {'type': 'integer', 'min': 18, 'max': 100}
            }
        },
        'work_experience': {
            'type': 'dict', 'required': True, 'schema': {
                'position': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                'company': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                'start_date': {'required': True, 'type': 'date', 'coerce': parse_date},
                'end_date': {'type': 'date', 'coerce': parse_date, 'nullable': True},
                'description': {'type': 'string'},
                'sector': {'type': 'string', 'minlength': 3, 'maxlength': 255},
                'area': {'type': 'string', 'minlength': 3, 'maxlength': 255},
            }
        },
        'studies': {
            'type': 'dict', 'required': True, 'schema': {
                'career': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                'institution': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                'level': {'required': True, 'type': 'integer', 'allowed': AcademicLevel.all()},
                'status': {'required': True, 'type': 'integer', 'allowed': AcademicStatus.all()},
                'start_date': {'required': True, 'type': 'date', 'coerce': parse_date},
                'end_date': {'type': 'date', 'coerce': parse_date, 'nullable': True},
            }
        },
        'languages': {
            'type': 'dict', 'required': True, 'schema': {
                # Language List [->HERE<-]
                'language': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                # ReadingLevel List [->HERE<-]
                'reading_level': {'required': True, 'contains': ['item']},
                # ReadingLevel List [->HERE<-]
                'writing_level': {'required': True, 'contains': ['item']},
                # ListingLevel List [->HERE<-]
                'listing_level': {'required': True, 'contains': ['item']},
                # TalkingLevel List [->HERE<-]
                # TalkingLevel List [->HERE<-]
                'talking_level': {'required': True, 'contains': ['item']},
            }
        },
        'skills': {
            'type': 'list', 'required': True, 'schema': {
                'type': 'dict', 'schema': {
                    'skill': {'type': 'string'},
                    'level': {'type': 'integer', 'min': 1, 'max': 10},
                }
            }
        },
    }
