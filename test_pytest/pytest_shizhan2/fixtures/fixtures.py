from test_pytest.pytest_shizhan1.core.calc import Calc
import pytest

@pytest.fixture(scope="module")
# @pytest.fixture
def calc_init():
    print("setup_class")
    return Calc()