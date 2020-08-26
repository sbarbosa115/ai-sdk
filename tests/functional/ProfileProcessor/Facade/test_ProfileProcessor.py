from src.profile_processor.Facade.ProfileProcessor import ProfileProcessor
from tests.Factory import UserProfile


def test_was_factory_returning_errors():
    wrongUserProfile = {'name': 'Juan', 'identification_number': 103058669}
    error = ProfileProcessor.validate(wrongUserProfile)

    assert len(error) > 0


def test_was_profile_successfully_validated():
    profile = UserProfile.profile()
    error = ProfileProcessor.validate(profile)

    assert len(error) == 0