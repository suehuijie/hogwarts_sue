# content of test_sample.py
import pytest

def inc(x):
    return x + 1

# 用例数据参数化
@pytest.mark.parametrize('a,b',[
    (1, 2),
    (10, 20),
    ("a1", "a2"),
    (3, 4),
    (5, 6)
])
def test_answer(a, b):
    assert inc(a) == b

def test_answer1():
    assert inc(4) == 5

# 装饰器
@pytest.fixture()
def login():
    print("登录操作")
    username = 'jerry'
    return username

class TestDemo:
    def test_a(self, login):
        print(f"a username = {login}")

    def test_b(self):
        print("b")

    def test_c(self, login):
        print(f"c username = {login}")

if __name__=='__main__':
    pytest.main(['test_a.py'])