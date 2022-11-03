import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(2),pi*4)

    def test_value(self):
        self.assertRaises(ValueError,circle_area,-2)

    def test_type(self):
        self.assertRaises(TypeError,circle_area,3+2j)
        self.assertRaises(TypeError,circle_area,True)
        self.assertRaises(TypeError,circle_area,"Chennai")

    def test_zero(self):
        self.assertRaises(ValueError,circle_area,0)