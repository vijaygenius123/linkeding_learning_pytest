
def setup_module(module):
    print("Setup Module")

def teardown_module(module):
    print("Teardown Module")

def setup_function(func):
    print("Running Setup")


def teardown_function(func):
    print("Running Teardown")


# will run as a test
def test_basic():
    print("Running Test")
    assert True

# will run as a test
def test_func():
    print("Running Test Func")
    assert True