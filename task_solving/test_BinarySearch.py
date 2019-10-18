import unittest
import Binary_Search as BS


class MyTestCase(unittest.TestCase):

    @staticmethod
    def creat_array(n, f, s):
        return [i for i in range(n, f, s)]

    def test_norm_0(self):
        array = self.creat_array(0, 20, 2)
        search = BS.BinarySearch(array)
        while search.result == 0:
            search.Step(0)
        self.assertEqual(search.result, 1)
        while search.result == 0:
            search.Step(2)
        self.assertEqual(search.result, 1)


if __name__ == '__main__':
    unittest.main()
