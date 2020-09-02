import json
import logging
import os
import uuid
import boto3
from cerberus import Validator
from dotenv import load_dotenv, find_dotenv
from src.profile_processor.Schema.User import user

load_dotenv(find_dotenv())
logging.basicConfig(filename='../../var/logs/transaction.log')


class ProfileProcessor:

    @staticmethod
    def validate(user_schema: dict) -> dict:
        v = Validator()
        v.validate(user_schema, user())
        return v.errors

    @staticmethod
    def save(user_schema: dict) -> bool:
        AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
        AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")
        AWS_BUCKET_NAME = os.environ.get("AWS_BUCKET_NAME")

        session = boto3.Session(
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
        )

        s3 = session.resource('s3')
        s3object = s3.Object(AWS_BUCKET_NAME, '{}.{}'.format(str(uuid.uuid4()), 'json'))
        s3object.put(Body=json.dumps(user_schema).encode('UTF-8'))

        return True

    @staticmethod
    def process(user_schema: dict) -> dict:
        logging.log('Loading User {} '.format(json.dumps(user_schema).encode('UTF-8')))

        v = Validator()
        v.validate(user_schema, user())
        if len(v.errors) == 0:
            ProfileProcessor.save(user_schema)
            return v.document

        return v.errors
