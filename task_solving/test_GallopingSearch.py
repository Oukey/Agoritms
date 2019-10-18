import unittest
import GallopingSearch as GS


class MyTestCase(unittest.TestCase):

    def test_norm_0(self):
        array = [num for num in range(0, 11)]
        self.assertFalse(GS.GallopingSearch(array, -1))
        self.assertTrue(GS.GallopingSearch(array, 0))
        self.assertTrue(GS.GallopingSearch(array, 1))
        self.assertTrue(GS.GallopingSearch(array, 2))
        self.assertTrue(GS.GallopingSearch(array, 3))
        self.assertTrue(GS.GallopingSearch(array, 4))
        self.assertTrue(GS.GallopingSearch(array, 5))
        self.assertTrue(GS.GallopingSearch(array, 6))
        self.assertTrue(GS.GallopingSearch(array, 7))
        self.assertTrue(GS.GallopingSearch(array, 8))
        self.assertTrue(GS.GallopingSearch(array, 9))
        self.assertTrue(GS.GallopingSearch(array, 10))
        self.assertFalse(GS.GallopingSearch(array, 11))

    def test_norm_1(self):
        array = [num for num in range(0, 11, 2)]
        self.assertFalse(GS.GallopingSearch(array, -1))
        self.assertTrue(GS.GallopingSearch(array, 0))
        self.assertFalse(GS.GallopingSearch(array, 1))
        self.assertTrue(GS.GallopingSearch(array, 2))
        self.assertFalse(GS.GallopingSearch(array, 3))
        self.assertTrue(GS.GallopingSearch(array, 4))
        self.assertFalse(GS.GallopingSearch(array, 5))
        self.assertTrue(GS.GallopingSearch(array, 6))
        self.assertFalse(GS.GallopingSearch(array, 7))
        self.assertTrue(GS.GallopingSearch(array, 8))
        self.assertFalse(GS.GallopingSearch(array, 9))
        self.assertTrue(GS.GallopingSearch(array, 10))
        self.assertFalse(GS.GallopingSearch(array, 11))


if __name__ == '__main__':
    unittest.main()
