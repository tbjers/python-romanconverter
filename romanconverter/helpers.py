# -*- coding: utf-8 -*-

numerals = {
    # Apostrophus system
    100000: "ↈ",
    50000:  "ↇ",
    10000:  "ↂ",
    5000:   "ↁ",
    # Conventional letter symbols
    1000:   "M",
    900:    "CM",
    500:    "D",
    400:    "CD",
    100:    "C",
    90:     "XC",
    50:     "L",
    40:     "XL",
    10:     "X",
    9:      "IX",
    5:      "V",
    4:      "IV",
    1:      "I",
}

def validate_input(value):
    try:
        return int(value)
    except ValueError:
        return False

def to_roman(value):
    """Convert a decimal to a Roman numeral string."""

    num = validate_input(value)
    result = ""

    if num == 0:
        return "nihil"

    for dec, roman in sorted(numerals.iteritems(), reverse = True):
        while num % dec < num:
            result += roman
            num -= dec

    return result
