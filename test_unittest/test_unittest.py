import unittest

class TestStringMethods(unittest.TestCase):

    # setupclass 和 teardownclass 在每个类前后执行一次
    # setupclass 和 teardown 是类方法，需要加装饰器
    @classmethod
    def setUpClass(cls)->None:
        print("setupclass")

    # setup和teardown 是在每个方法前后执行一次
    def setUp(self)->None:
        print("setup")

    def tearDown(self)->None:
        print("teardown")

    @classmethod
    def tearDownClass(cls)->None:
        print("teardownclass")

    def test_abc(self):
        print('test abc!')

    def test_upper(self):
        print("test_upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("test_isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("test_split")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
