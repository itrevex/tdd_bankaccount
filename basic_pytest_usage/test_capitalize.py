"""
Test Capitalize Function
"""
import pytest

def capital_case(word):
    if not isinstance(word, str):
        raise TypeError('Please provide a string argument')
    return word.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)
