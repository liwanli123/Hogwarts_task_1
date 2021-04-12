from typing import List
import pytest
from pytestdemo.get_data import get_calculatorTestData as data
from pytestdemo.Calculator import Calculator


@pytest.fixture(scope="class")
def get_calc():
    print("【计算开始】")
    calc = Calculator()
    yield calc
    print("【计算结束】")


@pytest.fixture(params=data("add")[0], ids=data("add")[1])
def addData(request):
    return request.param


@pytest.fixture(params=data("sub")[0], ids=data("sub")[1])
def subData(request):
    return request.param


@pytest.fixture(params=data("div")[0], ids=data("div")[1])
def divData(request):
    return request.param


@pytest.fixture(params=data("mul")[0], ids=data("mul")[1])
def mulData(request):
    return request.param


def pytest_collection_modifyitems(session, config, items: List):
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


