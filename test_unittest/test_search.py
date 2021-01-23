import unittest

class Search:

    def search_fun(self):
        print("search")
        return True

class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupclass")
        cls.search = Search()

    @classmethod
    def tearDownClass(cls):
        print("teardownclass")

    def setUp(self):
        print("setup -->方法级别")

    def tearDown(self):
        print("teardown -->方法级别")

    def test_search1(self):
        print("test_search1")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search2(self):
        print("test_search2")
        # search = Search()
        assert True == self.search.search_fun()

    def test_equal(self):
        print("断言相等")
        self.assertEqual(1,1, "判断 1 ==1")

    def test_notequal(self):
        print("断言不相等")
        self.assertNotEqual(1,1, "判断 1 =！1")

if __name__=='__main__':
    # 方法一：执行当前文件所有的unittest测试用例
    # unittest.main()
    # 方法二：执行指定的测试用例，添加用例到测试套件
    # 创建一个测试套件，批量执行测试方法
    suite = unittest.TestSuite()
    suite.addTest(TestSearch("test_search2"))
    unittest.TextTestRunner().run(suite)

    # 方法三：执行某个测试类,将测试类添加到测试套件里面，批量执行测试类
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
    # # suite2 = unittest.TestLoader().loadTestsFromTestCase()
    # suite = unittest.TestSuite([suite1])
    # unittest.TextTestRunner(verbosity=2).run(suite)