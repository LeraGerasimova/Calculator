import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

#позитивные тесты
    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 6, 2) == 3

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 11, 5) == 6

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 100, 1) == 101

#негативные тесты

    def test_multiply_cslculation_failed(self):
        assert self.calc.multiply(self, -6, 2) == 5

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 100, 100587) == 100789