import unittest
import MergeSort as MS


class MergeSortTest(unittest.TestCase):

    def NormTest(self):
        heap = MS.Heap()
        self.assertEqual(heap.HeapSize, 0)
        self.assertEqual(heap.HeapArray, [])
        heap.Add(1, 101)
        self.assertEqual(heap.HeapSize, 1)
        self.assertEqual(heap.HeapArray, [101])




    if __name__ == '__main__':
        unittest.main()
