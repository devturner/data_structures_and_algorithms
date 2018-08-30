from .bracket_validation import multi_braket_validation
import pytest


def test_multi_braket_validation_returns_true_happy_path():
    assert multi_braket_validation('this ( is ) good') == True


def test_multi_braket_validation_returns_false_happy_path():
    assert multi_braket_validation('this ( is bad') == False


def test_multi_braket_validation_returns_false_hard1_path():
    assert multi_braket_validation(')t{h[is ( i]s bad') == False


def test_multi_braket_validation_returns_true_hard2_path():
    assert multi_braket_validation('this is also good') == True


def test_multi_braket_validation_returns_false_hard3_path():
    assert multi_braket_validation('this i]s bad') == False


def test_multi_braket_validation_returns_false_hard4_path():
    assert multi_braket_validation('this is bad {{{{{((({{[[[') == False    


def test_example1():
    assert multi_braket_validation('{}') == True


def test_example2():
    assert multi_braket_validation('{}(){}') == True


def test_example3():
    assert multi_braket_validation('()[[Extra Characters]]') == True


def test_example4():
    assert multi_braket_validation('(){}[[]]') == True


def test_example5():
    assert multi_braket_validation('{}{Code}[Times](())') == True


def test_example6():
    assert multi_braket_validation('[({}]') == False


def test_example7():
    assert multi_braket_validation('(](') == False


def test_example8():
    assert multi_braket_validation('{(})') == False


