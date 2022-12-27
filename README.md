# Py-Grader
This is a project for grading python projects based on test cases. It is very basic right now, and a lot of features have been left out, but it works to some extent currently.

## Making tests
Currently, the only way to make a test is "nerd mode", which has a special way to make it. Write a function like so:
```
def test_case(program):
    if program.message == "Hello World!:
        assert True
    else:
        assert False
```
Program is the students program. The test case name does not currently affect anything, but it may with future updates, so I would suggest giving it a good name.  

Make an info block in the program like so:
```
INFO = {
    "name": "Test Name",
    "for": "Assignment"
}
```
The name will be displayed in the list, and the assignment is what will be graded with the test cases.