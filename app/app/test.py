"""
Sample test
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc Module"""

    def tes_add_numbers(self):
        """Test adding numbers to"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)
