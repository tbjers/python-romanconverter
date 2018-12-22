# -*- coding: utf-8 -*-

from . import helpers

def convert(value, **options):
    if options.get("direction") == "roman":
        return helpers.to_roman(value)
