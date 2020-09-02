from src.profile_processor.Facade.ProfileProcessor import ProfileProcessor
from tests.Factory import UserProfile


def test_was_phone_number_sanitized():
    profile = UserProfile.profile()

    phone = '(305)-78 0 99 88'
    profile['phone']['number'] = phone
    document = ProfileProcessor.process(profile)

    assert document['phone']['number'] == '3057809988'



