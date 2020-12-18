from day_18.solution import (
    process,
    process_operation,
)

s1 = '1 * (2+3)'
s2 = '1 * (2+3) + (3+5)'
s3 = '1 + (4 * (5 + 6))'


def test_simple_process_operation():
    expected = '9'
    expression = '1 + 2 * 3'
    result = process_operation(expression)

    assert result == expected


def test_process_operation():
    expected = '71'
    expression = '1 + 2 * 3 + 4 * 5 + 6'
    result = process_operation(expression)

    assert result == expected


def test_simple_parenthesis():
    expected = '5'
    expression = '1 * (2 + 3)'
    result = process(expression)

    assert result == expected


def test_double_parenthesis():
    expected = '13'
    expression = '1 * (2+3) + (3+5)'
    result = process(expression)

    assert result == expected


def test_nested_parenthesis():
    expected = '45'
    expression = '1 + (4 * (5 + 6))'
    result = process(expression)

    assert result == expected


def test_nested_parenthesis_final():
    expected = '51'
    expression = '1 + (2 * 3) + (4 * (5 + 6))'
    result = process(expression)

    assert result == expected
