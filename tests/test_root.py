# tests/test_root.py
# The root import for tests
# All tests should import this script and use it


# Imports
from typing import Any
from collections.abc import Callable


# Definitions
class BaseTest:
    """The base test class"""
    
    def __init__(self, condition: Callable) -> None:
        """Create or inherit from BaseTest"""

        # Condition must be callable
        if not callable(condition):
            raise TypeError("Condition must be callable")
        
        self.condition = condition
    
    def run(self, program, printed_output) -> bool:
        """Run the test"""
        
        return self.condition(program, printed_output)


class CustomTest(BaseTest):
    """A decorator to create a custom test"""
    
    def __init__(self, condition: Callable) -> None:
        """Create a custom test by decorating a function"""
        
        super().__init__(condition)


class AlwaysPassTest(BaseTest):
    """A test that always passes"""
    
    def __init__(self) -> None:
        """Create a test that always passes"""
        
        # Initialize with True lambda
        super().__init__(lambda p, o: True)


class AlwaysFailTest(BaseTest):
    """A test that always fails"""
    
    def __init__(self) -> None:
        """Create a test that always fails"""
        
        # Initialize with False lambda
        super().__init__(lambda p, o: False)


class VariableExistsTest(BaseTest):
    """A test that will pass if a variable exists in the program"""
    
    def __init__(self, program_var_name: str) -> None:
        """Create a test that will pass if a variable exists in the program"""                
        
        # Set variable
        self.program_var_name = program_var_name
    
    
    def run(self, program, o) -> bool:
        """Run the test"""
        
        # Try to get the variable
        try:
            getattr(program, self.program_var_name)
        
        # Return False if AttributeError
        except AttributeError:
            return False
        
        # If no error return True
        else:
            return True


class IsEqualTest(BaseTest):
    """A test that will pass if a value is equal to another"""
    
    def __init__(self, program_var_name: str, test_value: Any):
        """Create a test that will pass is a value in the program is equal to a set value"""
        
        # Set variables
        self.program_var_name = program_var_name
        self.test_value = test_value
    
    
    def run(self, program, o) -> bool:
        """Run the test"""
        
        # Make sure variable exists first
        exists_test = VariableExistsTest(self.program_var_name)
        if not exists_test.run(program, o):
            return False

        # Check if equal
        if getattr(program, self.program_var_name) == self.test_value:
            return True
        
        else:
            return False


class OutputEqualTest(BaseTest):
    """A test that will pass is the printed output is equal to a value"""
    
    def __init__(self, test_value: str, test_line: int) -> None:
        """Create a test that will pass is the printed output is equal to a value"""
        
        # Set variables
        self.test_value = test_value
        self.test_line = test_line
    
    
    def run(self, p, printed_output: str) -> bool:
        """Run the test"""
        
        # Check if equal
        if printed_output[self.test_line - 1] == self.test_value:
            return True
        
        else:
            return False