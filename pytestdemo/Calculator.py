"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/8 8:50 下午'
"""


# 计算器
class Calculator:
    # 加法
    def add(self, a, b):
        return round(a + b, 3)

    # 除法
    def div(self, a, b):
        return round(a / b, 3)

    # 乘法
    def mul(self, a, b):
        return round(a * b, 3)

    # 减法
    def sub(self, a, b):
        return round(a - b, 3)
