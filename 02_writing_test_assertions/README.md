# Test Fixtures

* establish a initial state for every test case
* ensure reproduceability
* test fixtures operates at three levels of specificity:
    * Module
    * Test Case
    * Test

1. test fixtures in PyUnit

```python
def setUpModule() : # runs once before any test ( when loading the script first execute this function)

def tearDownModule(): # runs once after all the tests

class MyTestCases(TestCase):

    @classmethod
    def setUpClass(cls):    # runs once before test cases inside class

    @classmethod
    def tearDownClass(cls):     # runs once after test cases inside the class

    def setUp(self):            # runs before each test

    def tearDown(self):         # runs after each test

```

## lets define a structure for test folder

tests
|- test_models.py
|- test_routes.py
|- fixtures
    |- account_data.json