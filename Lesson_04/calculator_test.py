import pytest
from calculator import Calculator

calculator = Calculator()

def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(5, 7)
    assert res == 12

def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-5, -7)
    assert res == -12

def test_sum_positive_and_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-9, 9)
    assert res == 0

def test_sum_float_nums(): #проверка сложения десятичных дробей
    calculator = Calculator()
    res = calculator.sum(4.8, 2.3)
    res = round(res, 1)
    assert res == 7.1

def test_sum_zero_nums():
    calculator = Calculator()
    res = calculator.sum(10, 0)
    assert res == 10

def test_div_positive():
    calculator = Calculator()
    res = calculator.div(25, 5)
    assert res == 5

# def test_div_by_zero():
#     calculator = Calculator()
#     res = calculator.div(10, 0)
#     assert res == None

def test_avg_positive():
    calculator = Calculator()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
    res = calculator.avg(numbers)
    print(res)
    assert res == 5

def test_avg_empty_list():
    calculator = Calculator()
    numbers = []
    res = calculator.avg(numbers)
    assert res == 0