import pytest


@pytest.fixture
def secondWork(scope="function"):
    print("this is function pre setup")
    yield
    print("tear down validation")



def test_initialCheck(presetupWork, secondWork):
    print("Initial Check")
    assert presetupWork == "pass"

@pytest.mark.skip
def test_secondCheck(presetupWork, secondWork):
    print("second Check")
    assert presetupWork == "pass"
