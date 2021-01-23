import unittest

from util.HTMLTestRunner_PY3 import HTMLTestRunner

if __name__=='__main__':
    report_title = '用力执行报告 我的标题'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = 'result.html'

    # 方法四：匹配某个目录下所有以test开头的py文件，执行这些文件下的所有测试用例
    test_dir = 'test_unittest'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    # unittest.TextTestRunner(verbosity=2).run(discover)
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)
