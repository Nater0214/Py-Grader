# Import test root
import test_root

# This is the info block, it is necessary to tell the test runner info about the test. You can follow the template to make your own.
INFO = {
    "name": "Assertion Test",
    "for": "Hello-World-Test"
}

# These are the tests you just need to create the test for the test runner to run it.
always_true = test_root.AlwaysPassTest()
always_true2 = test_root.AlwaysPassTest()
always_false = test_root.AlwaysFailTest()