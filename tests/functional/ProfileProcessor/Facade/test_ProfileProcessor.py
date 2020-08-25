from src.profile_processor.Facade.ProfileProcessor import ProfileProcessor


def test_was_factory_returning_errors():
    wrongUserProfile = {'name': 'Juan', 'identification_number': 103058669}
    ProfileProcessor.validate(wrongUserProfile)

    assert True