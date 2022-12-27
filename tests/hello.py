INFO = {
    "name": "Hello World Test",
    "for": "Hello-World-Test"
}

def message_hello(program):
    try:
        if program.message == "Hello World!":
            assert True
        else:
            assert False
    except AttributeError:
        assert False