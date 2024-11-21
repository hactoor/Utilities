import unittest
from calculator import convert_kilos_to_pounds  # Import the function

class TestConvertKilosToPounds(unittest.TestCase):
    def test_convert_valid_input(self):
        #Test with a valid float inout
        result = convert_kilos_to_pounds(220.5)
        self.assertAlmostEqual(result,100.0, places=2)  
        
if __name__ == "__main__":
    unittest.main()