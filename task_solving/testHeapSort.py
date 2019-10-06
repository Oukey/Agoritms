import unittest
import Heap_Sort as H


class HeapSortTest(unittest.TestCase):

    def test_01(self):
        hs = H.HeapSort([5, 4, 6, 3, 7, 2, 8, 9, 1])
        self.assertEqual(9, len(hs.HeapObject.HeapArray))
        self.assertEqual(9, hs.GetNextMax())
        self.assertEqual(8, len(hs.HeapObject.HeapArray))
        self.assertEqual(8, hs.GetNextMax())
        self.assertEqual(7, hs.GetNextMax())
        self.assertEqual(6, hs.GetNextMax())
        self.assertEqual(5, hs.GetNextMax())
        self.assertEqual(4, hs.GetNextMax())
        self.assertEqual(3, hs.GetNextMax())
        self.assertEqual(2, hs.GetNextMax())
        self.assertEqual(1, hs.GetNextMax())
        self.assertEqual(0, len(hs.HeapObject.HeapArray))
        self.assertEqual(-1, hs.GetNextMax())
        self.assertEqual([], hs.HeapObject.HeapArray)

    if __name__ == '__main__':
        unittest.main()
