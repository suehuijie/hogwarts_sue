from python_practice.python_task.tstonglao import TongLao


class XuZhu(TongLao):

    def __init__(self, power):
        super().__init__(power)

    def read(self):
        print("罪过罪过！！")


xuzhu = XuZhu(500)
xuzhu.read()