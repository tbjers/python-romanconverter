# -*- coding: utf-8 -*-

from .core import convert

class TestClass(object):
    def test_convert_without_direction(self):
        assert convert(1) == None

    def test_convert(self):
        assert convert(1, direction = "roman") == "I"

    def test_string_input(self):
        assert convert("lizard", direction = "roman") == "nihil"
