from unittest import TestCase
import pytest
from CalculateAverageOfList import CalculateAverageOfList
from main import comparison


def test_calculate_average_of_list():
    assert CalculateAverageOfList([1, 5, 8, 9, 10]).average == 6.6


def test_if_divizion_by_zero():
    assert CalculateAverageOfList([]).average == 0


def test_not_list():
    with pytest.raises(TypeError):
        CalculateAverageOfList("1, 5, 8, 9, 10")


def test_comparison():
    list1 = CalculateAverageOfList([1, 5, 8, 9, 10])
    list2 = CalculateAverageOfList([5, 5, 7, 10, 6])
    assert comparison(list1, list2) == "Средние значения равны"
