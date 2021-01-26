# from test_pytest.pytest_shizhan2.fixtures import calc_init

def test_calc_demo(calc_init):
    assert calc_init.mul(1,2) == 2


def test_calc_demo2(calc_init):
    assert calc_init.mul(1,3) == 3

