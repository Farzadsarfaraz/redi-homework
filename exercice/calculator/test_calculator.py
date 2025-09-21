import pytest
from exercice.calculator.calculator import Calculator
calculator_fixture_scope = "function"

@pytest.fixture(scope=calculator_fixture_scope)
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(2, 3) == 5


def test_subtract(calculator):
    assert calculator.subtract(5, 3) == 2


def test_multiply(calculator):
    assert calculator.multiply(4, 3) == 12


def test_divide(calculator):
    assert calculator.divide(10, 2) == 5


def test_divide_by_zero(calculator):
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.divide(10, 0)

@pytest.mark.parametrize(
    "a, b, op, expected",
    [
        (2, 3, "add", 5),     
        (5, 3, "subtract", 2),    
        (4, 3, "multiply", 12),  
        (10, 2, "divide", 5),   
    ]
)
def test_evaluate(calculator, a, b, op, expected):
    assert calculator.evaluate(a, b, op) == expected
