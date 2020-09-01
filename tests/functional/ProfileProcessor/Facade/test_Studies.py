from src.profile_processor.Facade.ProfileProcessor import ProfileProcessor
from tests.Factory import UserProfile


def test_when_date_is_present_must_be_grater_than_from_date():
    profile = UserProfile.profile()

    start_date = '2020-01-03'
    end_date = '2020-01-02'
    profile['studies'][0]['start_date'] = start_date
    profile['studies'][0]['end_date'] = end_date
    errors = ProfileProcessor.validate(profile)

    assert len(errors) > 0
