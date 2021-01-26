import pytest as pytest
import allure
from test_pytest.pytest_shizhan1.core.calc import Calc
import yaml


def load_data(path='./data.yaml'):
    with open(path,encoding='UTF-8') as f:
        data = yaml.safe_load(f)
        keys = ','.join(data[0].keys())
        values = [list(d.values()) for d in data]
        data1 = {"keys": keys, "values": values}
        print(f'load_data:{load_data}')
        print(f'keys {keys}')
        print(f'values {values}')
        return data1

class TestCalc:

    data = load_data()

    # 优先执行，会override实例方法 setup()
    @classmethod
    def setup_class(self):
        print("setup_class classmethod")
        self.calc = Calc()


    # 正常值例子
    @pytest.mark.parametrize(
        data['keys'],
        data['values']
    )
    def test_div_success(self, a, b, c):
        assert self.calc.div(a, b) == c
