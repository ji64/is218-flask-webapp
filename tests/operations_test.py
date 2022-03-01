from calculator.operations import Addition, Subtraction, Multiplication


def test_calculator_operations_add():
    assert Addition.add(1, 1) == 2

def test_calculator_operations_subtract():
    assert Subtraction.subtract(2, 1) == 1

def test_calculator_operations_multiply():
    assert Multiplication.multiply(2, 3) == 6



