import ast
import unittest

class SyntaxTest(unittest.TestCase):
    def test_valid_code(self):
        code = """
        def my_function():
            return "Hello, world!"
        """
        try:
            ast.parse(code)
        except SyntaxError:
            self.fail("Unexpected SyntaxError for valid code")

    def test_valid_code(self):
        code = """
        def my_function():
            return "Hello, world!"
        """
        try:
            ast.parse(code)
        except SyntaxError:
            self.fail("Unexpected SyntaxError for valid code")

if __name__ == "__main__":
    unittest.main()