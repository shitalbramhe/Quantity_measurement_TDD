from InvalidTypeException import InvalidTypeException
import unittest

from Quantity_measurement import Quantitymeasurement

class TestQuantitymeasurement(unittest.TestCase):

    def test_zero_feet_inch(self):
        self.assertEqual(Quantitymeasurement.feet_to_inch_value(0), 0)
    
    def test_Null_feet_inch(self):
        self.assertEqual(Quantitymeasurement.feet_to_inch_Null(None),None)

    def test_Reference_feet_inch(self):
        self.assertEqual(Quantitymeasurement.feet_to_inch_Reference(7),id(7))

    def test_Type_feet_inch(self):
        self.assertEqual(Quantitymeasurement.feet_to_inch_type(2), type(3))
    
    def test_equality_feet_inch(self):
        self.assertEqual(Quantitymeasurement.feet_to_inch_value(4),4)

        self.assertGreater(Quantitymeasurement.feet_to_inch_value(9),2)
        
        self.assertLess(Quantitymeasurement.feet_to_inch_value(3),8)
