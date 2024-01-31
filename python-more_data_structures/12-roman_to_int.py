def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    first_value = 0
    for char in reversed(roman_string):
        last_value = roman_numerals.get(char, 0)
        if last_value < first_value:
            result -= last_value
        else:
            result += last_value
        first_value = last_value
    return result
