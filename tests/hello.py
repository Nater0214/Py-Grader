from . import test_root

INFO = {
    "name": "Hello World Test",
    "for": "Hello-World-Test"
}

message_hello = test_root.IsEqualTest("message", "Hello World!")
printed_message = test_root.OutputEqualTest("Hello World!", 1)