import HtmlTestRunner
import unittest


class TestStringMethod(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    #
    # def testError(self):
    #     raise ValueError

    def test_fail(self):
        self.assertEqual(1, 1)

    @unittest.skip
    def tast_skip(self):
        pass


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
