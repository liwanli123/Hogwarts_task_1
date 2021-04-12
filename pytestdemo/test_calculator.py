"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/8 8:47 下午'
"""
from pytestdemo.Calculator import Calculator

class TestCal:

    def test_add(self, addData, get_calc):
        try:
            assert addData[2] == Calculator().add(addData[0], addData[1])
        except TypeError:
            print("请输入数字")
        except IndexError:
            print("不能输入空字符")

    def test_div(self, divData, get_calc):
        try:
            assert divData[2] == Calculator().div(divData[0], divData[1])
        except TypeError:
            print("请输入数字")
        except IndexError:
            print("不能输入空字符")
        except ZeroDivisionError:
            print("除数不能为0")

    def test_mul(self, mulData, get_calc):
        try:
            assert mulData[2] == Calculator().mul(mulData[0], mulData[1])
        except TypeError:
            print("请输入数字")
        except IndexError:
            print("不能输入空字符")

    def test_sub(self, subData, get_calc):
        try:
            assert subData[2] == Calculator().sub(subData[0], subData[1])
        except TypeError:
            print("请输入数字")
        except IndexError:
            print("不能输入空字符")
