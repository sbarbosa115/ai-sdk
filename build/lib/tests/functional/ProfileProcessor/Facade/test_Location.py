from src.profile_processor.Facade.ProfileProcessor import ProfileProcessor
from tests.Factory import UserProfile


def test_was_city_name_and_state_lowercase_and_sanitized():
    profile = UserProfile.profile()

    city = '   Bogotá   '
    state = '   Bogotá D.C   '
    profile['location']['city'] = city
    profile['location']['state'] = state
    document = ProfileProcessor.process(profile)

    assert document['location']['city'] == 'bogotá'
    assert document['location']['state'] == 'bogotá d.c'



