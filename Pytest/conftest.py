import pytest


@pytest.fixture
def presetupWork(scope="session"):
    print("this is pre setup")
    return "pass"