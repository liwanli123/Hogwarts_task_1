"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/8 8:47 下午'
"""
import pytest
import yaml
from Calculator import Calculator


class TestCal:

    def setup_class(self):
        print("setup Test")

    def teardown_class(self):
        print("Teardown Test")

    @pytest.fixture(scope='function')
    def add(self):
        print("Add Setup")
        yield
        print("Add Teardown ")

    @pytest.fixture(scope='function')
    def div(self):
        print("Div Setup")
        yield
        print("Div Teardown ")

    @pytest.fixture(scope='function')
    def mul(self):
        print("Mul Setup")
        yield
        print("Mul Teardown ")

    @pytest.fixture(scope='function')
    def sub(self):
        print("Sub Setup")
        yield
        print("Sub Teardown ")

    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open("add.yaml", encoding='utf-8')))
    @pytest.mark.usefixtures("add")
    def test_add(self, a, b, expect):
        assert expect == Calculator().add(a, b)

    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open("div.yaml", encoding='utf-8')))
    @pytest.mark.usefixtures("div")
    def test_div(self, a, b, expect):
        assert expect == Calculator().div(a, b)

    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open("mul.yaml", encoding='utf-8')))
    @pytest.mark.usefixtures("mul")
    def test_mul(self, a, b, expect):
        assert expect == Calculator().mul(a, b)

    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open("sub.yaml", encoding='utf-8')))
    @pytest.mark.usefixtures("sub")
    def test_sub(self, a, b, expect):
        assert expect == Calculator().sub(a, b)
