# -*- coding: utf-8 -*-

from .helpers import to_roman

class TestClass(object):
    def test_zero(self):
        assert to_roman(0) == "nihil"

    def test_basic(self):
        assert to_roman(1) == "I"
        assert to_roman(4) == "IV"
        assert to_roman(5) == "V"
        assert to_roman(9) == "IX"
        assert to_roman(10) == "X"
        assert to_roman(40) == "XL"
        assert to_roman(50) == "L"
        assert to_roman(90) == "XC"
        assert to_roman(100) == "C"
        assert to_roman(400) == "CD"
        assert to_roman(500) == "D"
        assert to_roman(900) == "CM"
        assert to_roman(1000) == "M"

    def test_edge_cases(self):
        assert to_roman(2) == "II"
        assert to_roman(3) == "III"
        assert to_roman(6) == "VI"
        assert to_roman(8) == "VIII"
        assert to_roman(3998) == "MMMCMXCVIII"
        assert to_roman(3999) == "MMMCMXCIX"

    def test_years(self):
        assert to_roman(2018) == "MMXVIII"

    def test_large_numbers(self):
        assert to_roman(4999) == "MMMMCMXCIX"
        assert to_roman(5000) == "ↁ"
        assert to_roman(5500) == "ↁD"
        assert to_roman(10000) == "ↂ"
        assert to_roman(50000) == "ↇ"
        assert to_roman(100000) == "ↈ"
        assert to_roman(200000) == "ↈↈ"
        assert to_roman(250001) == "ↈↈↇI"
