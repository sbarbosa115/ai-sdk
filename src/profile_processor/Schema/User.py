def user():
    return {
        'name': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
        'identification_number': {'type': 'integer', 'minlength': 0, 'maxlength': 20},
        'email': {'type': 'string', 'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'},
        # Pending to add Email Validation
        'phone': {
            'area_code': {'required': True, 'type': 'integer', 'min': 1, 'max': 999},
            'number': {'required': True, 'type': 'integer', 'minlength': 7, 'maxlength': 11},
        },
        'location': {
            # same that current if not present.
            'birth': {
                'country_name': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                'country_iso_code': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 3},
                'city': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                'state': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
            },
            'current': {
                'country_name': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                'country_iso_code': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 3},
                'city': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
                'state': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
            },
        },
        'age': {
            'birth_date': {'type': 'datetime'},
            'number': {'type': 'integer', 'min': 18, 'max': 100}
        },
        'work_experience': {
            'position': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
            'company': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
            'start_date': {'required': True, 'type': 'datetime'},
            'end_date': {'type': 'datetime'},
            'description': {'type': 'string'},
            'sector': {'type': 'string', 'minlength': 3, 'maxlength': 255},
            'area': {'type': 'string', 'minlength': 3, 'maxlength': 255},
        },
        'studies': {
            'career': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
            'institution': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
            # Level List [->HERE<-]
            'level': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
            # Status List [->HERE<-]
            'status': {'required': True, 'type': 'string', 'minlength': 3, 'maxlength': 255},
            'start_date': {'required': True, 'type': 'datetime'},
            'end_date': {'type': 'datetime'},
        },
        'languages': {
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
        },
        'skills': {
            'rows': {
                'type': 'list', 'schema': {
                    'type': 'dict', 'schema': {
                        'skill': {'type': 'string'},
                        'level': {'type': 'integer', 'min': 1, 'max': 10},
                    }
                }
            }
        },
    }
