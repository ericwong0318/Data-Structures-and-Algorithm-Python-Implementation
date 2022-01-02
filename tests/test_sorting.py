import unittest
from sorting import linear_time_sorting, merge_sort, quadratic_time_sorting, quicksort


class TestSorting(unittest.TestCase):
    def setUp(self) -> None:
        self.bubble_sort = quadratic_time_sorting.QuadraticTimeSorting().bubble_sort
        self.insertion_sort = quadratic_time_sorting.QuadraticTimeSorting().insertion_sort
        self.selection_sort = quadratic_time_sorting.QuadraticTimeSorting().selection_sort
        self.merge_sort = merge_sort.MergeSort().merge_sort
        self.quicksort = quicksort.QuickSort().quick_sort
        self.randomized_quicksort = quicksort.QuickSort().randomized_quicksort
        self.radix_sort = linear_time_sorting.LinearTimeSorting().radix_sort

    def test_normal_list(self):
        unsorted_list = [5, 0, 7, 4, 8, 6, 3, 9, 1, 2]
        sorted_list = [i for i in range(10)]

        # bubble sort
        unsorted_list_copy = unsorted_list
        self.bubble_sort(unsorted_list_copy)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # insertion sort
        unsorted_list_copy = unsorted_list
        self.insertion_sort(unsorted_list_copy)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # selection sort
        unsorted_list_copy = unsorted_list
        self.selection_sort(unsorted_list_copy)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # merge sort
        unsorted_list_copy = unsorted_list
        self.merge_sort(unsorted_list_copy)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # quicksort
        unsorted_list_copy = unsorted_list
        self.quicksort(unsorted_list_copy, 0, len(unsorted_list_copy) - 1)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # randomized quicksort
        unsorted_list_copy = unsorted_list
        self.randomized_quicksort(unsorted_list_copy, 0, len(unsorted_list_copy) - 1)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # radix sort
        unsorted_list_copy = unsorted_list
        result = self.radix_sort(unsorted_list_copy, 1, 9)
        self.assertEqual(sorted_list, result)

    def test_empty_list(self):
        unsorted_list = []
        sorted_list = []
        # bubble sort
        unsorted_list_copy = unsorted_list
        self.bubble_sort(unsorted_list_copy)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # insertion sort
        unsorted_list_copy = unsorted_list
        self.insertion_sort(unsorted_list_copy)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # selection sort
        unsorted_list_copy = unsorted_list
        self.selection_sort(unsorted_list_copy)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # merge sort
        unsorted_list_copy = unsorted_list
        self.merge_sort(unsorted_list_copy)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # quicksort
        unsorted_list_copy = unsorted_list
        self.quicksort(unsorted_list_copy, 0, len(unsorted_list_copy) - 1)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # randomized quicksort
        unsorted_list_copy = unsorted_list
        self.randomized_quicksort(unsorted_list_copy, 0, len(unsorted_list_copy) - 1)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # radix sort
        unsorted_list_copy = unsorted_list
        result = self.radix_sort(unsorted_list_copy, 1, 9)
        self.assertEqual(sorted_list, result)

    def test_negative_number_list(self):
        unsorted_list = [-5, 0, -7, -4, -8, -6, -3, -9, -1, -2]
        sorted_list = [-i for i in reversed(range(10))]

        # bubble sort
        unsorted_list_copy = unsorted_list
        self.bubble_sort(unsorted_list_copy)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # insertion sort
        unsorted_list_copy = unsorted_list
        self.insertion_sort(unsorted_list_copy)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # selection sort
        unsorted_list_copy = unsorted_list
        self.selection_sort(unsorted_list_copy)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # merge sort
        unsorted_list_copy = unsorted_list
        self.merge_sort(unsorted_list_copy)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # quicksort
        unsorted_list_copy = unsorted_list
        self.quicksort(unsorted_list_copy, 0, len(unsorted_list_copy) - 1)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # randomized quicksort
        unsorted_list_copy = unsorted_list
        self.randomized_quicksort(unsorted_list_copy, 0, len(unsorted_list_copy) - 1)
        self.assertEqual(sorted_list, unsorted_list_copy)


if __name__ == '__main__':
    unittest.main()
