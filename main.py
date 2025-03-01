from test_module import TestCalculateFunction
import unittest

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculateFunction)
    unittest.TextTestRunner().run(suite)