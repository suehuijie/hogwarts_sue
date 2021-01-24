import yaml

import pytest as pytest


class TestData:
    @pytest.mark.parametrize("a,b",[
        (10, 20),
        (10, 5),
        (3, 9)
    ])
    def test_data_string(self, a, b):
        print(a+b)

    @pytest.mark.parametrize(['c','d'],[
        (10, 20),
        (10, 30)
    ])
    def test_data_list(self, c ,d):
        print(c+d)

    @pytest.mark.parametrize(('e','f'),[
        (1, 2),
        (3, 4)
    ])
    def test_data_tuple(self, e, f):
        print(e+f)

    @pytest.mark.parametrize(('h','i'), yaml.safe_load(open("./data.yaml")))
    def test_data_yaml(self, h, i):
        print(h + i)