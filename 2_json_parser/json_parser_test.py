import pytest
import json_parser

def parse(filename):
    try:
        print(filename)
        with open(f"./test/{filename}","r") as file:
            contents = file.read()            
            return json_parser.parse(contents,[])
    except Exception as e:         
        raise(e)


def test_full_payload_valid():
    print('Testing')
    result = parse("pass1.json")
    assert result == True, "pass1.json - Full valid payload"

def test_not_too_deep_payload_valid():
    result = parse("pass2.json")
    assert result == True, "pass2.json - Not too deep valid payload"
    
def test_object_or_array_payload_valid():
    result = parse("pass3.json")
    assert result == True, "pass3.json - Object or array valid payload"

def test_string_payload_invalid():
    result = parse("fail1.json")
    assert result == False, "fail1.json - A JSON payload should be an object or array, not a string."
    
def test_unclose_array_invalid():
    result = parse("fail2.json")
    assert result == False, "fail2.json - Unclosed array"

def test_unquoted_key_invalid():
    result = parse("fail3.json")
    assert result == False, "fail3.json - Unquoted key"

def test_array_extra_comma_invalid():
    result = parse("fail4.json")
    assert result == False, "fail4.json - Extra comma"

def test_double_extra_comma_invalid():
    result = parse("fail5.json")
    assert result == False, "fail5.json - double extra comma"

def test_missing_value_invalid():
    result = parse("fail6.json")
    assert result == False, "fail6.json - missing value"

def test_comma_after_close_invalid():
    result = parse("fail7.json")
    assert result == False, "fail7.json - Comma after the close"

def test_extra_close_invalid():
    result = parse("fail8.json")
    assert result == False, "fail8.json - Extra close"

def test_object_extra_comma_invalid():
    result = parse("fail9.json")
    assert result == False, "fail19.json - Extra comma"

def test_misplaced_quote_value_invalid():
    result = parse("fail10.json")
    assert result == False, "fail10.json - misplaced quoted value"

def test_illegal_expression_invalid():
    result = parse("fail11.json")
    assert result == False, "fail11.json - Illegal expression"

def test_illegal_invocation_invalid():
    result = parse("fail12.json")
    assert result == False, "fail12.json - Illegal invocation"

def test_numbers_with_leading_zeros_invalid():
    result = parse("fail13.json")
    assert result == False, "fail13.json - Numbers cannot have leading zeroes"

def test_hex_numbers_invalid():
    result = parse("fail14.json")
    assert result == False, "fail14.json - Numbers cannot be hex"

def test_illegal_backslash_escape_x_invalid():
    result = parse("fail15.json")
    assert result == False, "fail15.json - Illegal backslash escape (x)"

def test_array_unquoted_value_invalid():
    result = parse("fail16.json")
    assert result == False, "fail16.json - Unquoted array value"

def test_illegal_backslash_escape_0_invalid():
    result = parse("fail17.json")
    assert result == False, "fail17.json - Illegal backslash escape (0)"

def test_too_deep_invalid():
    result = parse("fail18.json")
    assert result == False, "fail18.json - Too deep"

def test_missing_colon_invalid():
    result = parse("fail19.json")
    assert result == False, "fail19.json - Missing colon"

def test_double_colon_invalid():
    result = parse("fail20.json")
    assert result == False, "fail20.json - Double colon"

def test_comma_instead_of_colon_invalid():
    result = parse("fail21.json")
    assert result == False, "fail21.json - Comma instead of colon"

def test_colon_instead_of_comma_invalid():
    result = parse("fail22.json")
    assert result == False, "fail22.json - Colon instead of comma"

def test_bad_value_invalid():
    result = parse("fail23.json")
    assert result == False, "fail23.json - Bad value"

def test_single_quote_invalid():
    result = parse("fail24.json")
    assert result == False, "fail24.json - single quote"

def test_tab_character_in_string_invalid():
    result = parse("fail25.json")
    assert result == False, "fail25.json - Tab character in string"

def test_illegal_backslash_escape_whitespace_invalid():
    result = parse("fail26.json")
    assert result == False, "fail26.json - Illegal backslash escape ( )"

def test_line_break_invalid():
    result = parse("fail27.json")
    assert result == False, "fail27.json - Line break in string"

def test_line_break_and_illegal_escape_character_in_string_invalid():
    result = parse("fail28.json")
    assert result == False, "fail28.json - Line break in string and illegal escape character"

def test_unexpected_end_of_number_e_invalid():
    result = parse("fail29.json")
    assert result == False, "fail29.json - Unexpected end of number (e)"

def test_unexpected_end_of_number_e_plus_invalid():
    result = parse("fail30.json")
    assert result == False, "fail30.json - Unexpected end of number (e+)"

def test_unexpected_end_of_number_e_plus_minus_1_invalid():
    result = parse("fail31.json")
    assert result == False, "fail31.json - Unexpected end of number (0e+-1)"

def test_comma_instead_of_closing_brace_invalid():
    result = parse("fail32.json")
    assert result == False, "fail32.json - Comma instead if closing brace"

def test_brace_mismatch_invalid():
    result = parse("fail33.json")
    assert result == False, "fail33.json - Brace mismatch"
