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

    def test_feet_inch(self):
        self.assertEqual(Quantitymeasurement.feet_to_inch(0,'Feet'),0,'Inch')
        self.assertNotEqual(Quantitymeasurement.feet_to_inch(1,'Feet'),1,'Inch')
        self.assertEqual(Quantitymeasurement.feet_to_inch(1,'Feet'),12,'Inch')

    def test_inch_feet(self):
        self.assertNotEqual(Quantitymeasurement.inch_to_feet(1,'Inch'),1,'Feet')
        self.assertEqual(Quantitymeasurement.inch_to_feet(12,'Inch'),1,'Feet')

    def tes_feet_yard(self):
        self.assertEqual(Quantitymeasurement.feet_yard(3,'Feet'),1,'yard')
        self.assertNotEqual(Quantitymeasurement.feet_yard(1,'Feet'),1,'yard')

    def test_inch_yard(self):
        self.assertNotEqual(Quantitymeasurement.inch_yard(1,'Inch'),1,'yard')
        self.assertEqual(Quantitymeasurement.inch_yard(36,'Inch'),1,'yard')

    def test_yard_inch(self):
        self.assertEqual(Quantitymeasurement.yard_inch(1,'yard'),36,'Inch')

    def test_yard_feet(self):
        self.assertEqual(Quantitymeasurement.yard_feet(1,'yard'),3,'Feet')
