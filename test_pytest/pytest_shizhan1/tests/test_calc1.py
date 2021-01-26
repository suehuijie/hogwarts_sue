import pytest as pytest
import allure

from test_pytest.pytest_shizhan1.core.calc import Calc


class TestCalc:

    def setup_class(self):
        self.calc = Calc()

    @allure.step
    def simple_step(self, step_param1, step_param2=None):
        pass

    # 正常值例子
    @pytest.mark.parametrize('a, b, c',[
        [2.5, 2.5, 6.25],
        [5.45, 0, 0],
        [-20, 0, 0]
    ])
    def test_mul_success(self, a, b, c):
        # 追加截图
        allure.attach.file(".../resource/photo1.jpg",name="图片", attachment_type=allure.attachment_type.JPG)
        self.simple_step(f'{a} {b} {c}')
        assert self.calc.mul(a, b) == c


    #正常值例子
    @pytest.mark.parametrize('a,b,c',[
        [-20, -10, 2],
        [-100, 10, -10],
        [0, 10, 0]
    ])
    def test_div(self, a, b, c):
        assert self.calc.div(a,b) == c



    # 流程示例
    def test_process(self):
        r1 = self.calc.mul(1,2)
        r2 = self.calc.div(2,1)
        assert r1 == 2
        assert r2 == 2