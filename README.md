# Py-Grader
## Introduction
This is a project for grading python projects based on test cases. It is very basic right now, and a lot of features have been left out, but it works to some extent currently.

## Making tests
Currently, the only way to make a test is "nerd mode", which has a special way to make it. First import test_root like so at the top of your test script:
```
from . import test_root
```

 Make a variable with the type of test you would like:
```
always_pass = test_root.AlwaysPassTest()
```
The variable name currently does not affect anything, but it may in the future; give it an appropriate name like above.

Another example test:
```
message_correct = test_root.IsEqualTest("message", "Hello World!")
```
Replace `message` with the variable name to test and `Hello World!` with the value to test against.

Make an info block in the program like so:
```
INFO = {
    "name": "Test Name",
    "for": "Assignment"
}
```
The name will be displayed in the list, and the assignment is what will be graded with the test cases.

## Running tests