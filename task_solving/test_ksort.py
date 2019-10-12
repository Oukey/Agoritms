import unittest
import kSort as KS


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    @staticmethod
    def creat_list():
        let_ = 'abcdefgh'
        num_ = '0123456789'
        st = [a + str(m) + str(n) for a in let_ for m in num_ for n in num_]
        return st

    def test_norm(self):
        st = self.creat_list()
        ksort = KS.ksort()
        for elem in st:
            ksort.add(elem)
        self.assertEqual(st, ksort.items)

    def test_norm_01(self):
        k_sort = KS.ksort()
        s = 'zip'
        self.assertEqual(k_sort.index(s), -1)
        s = -88
        self.assertEqual(k_sort.index(s), -1)
        s = 988
        self.assertEqual(k_sort.index(s), -1)
        s = 98887
        self.assertEqual(k_sort.index(s), -1)
        s = '10a'
        self.assertEqual(k_sort.index(s), -1)
        s = 'k55'
        self.assertEqual(k_sort.index(s), -1)

    def test_norm_02(self):
        k_sort = KS.ksort()
        s_1 = 'f87'
        s_2 = 'h01'
        s_3 = 'e87'
        res_0 = k_sort.index(s_1) > k_sort.index(s_3)
        res_1 = k_sort.index(s_2) < k_sort.index(s_3)
        res_3 = k_sort.index(s_1) == k_sort.index(s_3)
        self.assertTrue(res_0)
        self.assertFalse(res_1)
        self.assertFalse(res_3)


if __name__ == '__main__':
    unittest.main()
