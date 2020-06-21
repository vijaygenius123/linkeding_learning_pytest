
def setup_function(func):
    print("Running Setup")


def teardown_function(func):
    print("Running Teardown")


# will run as a test
def test_basic():
    print("Running Test")
    assert True