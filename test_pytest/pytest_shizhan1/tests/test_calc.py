import pytest as pytest
from pytest import raises

from test_pytest.pytest_shizhan.core.calc import Calc


class TestCalc:

    def setup_class(self):
        self.calc = Calc()

    # 正常值例子
    @pytest.mark.parametrize('a, b, c',[
        # 正数 *  正数
        # 正数 * 负数
        # 负数 * 负数
        # 整数 * 整数
        # 整数 * 小数
        # 小数 * 小数
        # 小数 * 0
        # 负数 * 0
        [2, 3, 6],
        [26, -1, -26],
        [-10, -5, 50],
        [20, 10, 200],
        [2, 1.5, 3],
        [2.5, 2.5, 6.25],
        [5.45, 0, 0],
        [-20, 0, 0]
    ])
    def test_mul_success(self, a, b, c):
        assert self.calc.mul(a, b) == c

    # 异常值例子
    @pytest.mark.parametrize('a, b, c',[
        # 整数 * 字母
        # 负数 * 字母
        [10, "a", 10],
        ["b", 1, 2]
    ])
    def test_mul_failed(self, a, b, c):
        assert self.calc.mul(a, b) == c


    #正常值例子
    @pytest.mark.parametrize('a,b,c',[
        # 整数 / 整数
        # 整数 / 小数
        # 小数 / 小数
        # 负数 / 负数
        # 负数 / 正数
        # 0 / 正数
        [10, 2, 5],
        [10, 2.5, 4],
        [2.5, 1.25, 2],
        [-20, -10, 2],
        [-100, 10, -10],
        [0, 10, 0]
    ])
    def test_div(self, a, b, c):
        assert self.calc.div(a,b) == c

    # 除数为0
    @pytest.mark.parametrize('a,b',[
        # 整数 / 0
        # 小数 / 0
        [10, 0],
        [4.6, 0]
    ])
    def test_div_failed(self, a, b):
        with pytest.raises(ZeroDivisionError):
            assert self.calc.div(a,b)

    # 除数和被除数为字母
    @pytest.mark.parametrize('a,b',[
        # 字母 / 数字
        # 数字 / 字母
        ["a", 2],
        [4.6, "a"]
    ])
    def test_div_failed1(self,a,b):
        with pytest.raises(TypeError):
            assert self.calc.div(a,b)


    # 流程示例
    def test_process(self):
        r1 = self.calc.mul(1,2)
        r2 = self.calc.div(2,1)
        assert r1 == 2
        assert r2 == 2