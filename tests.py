import unittest

from solution import RunTimeExercises


class RunTimeUnitTests(unittest.TestCase):

    def test_linear_search(self):
        subject = RunTimeExercises()
        a_list = [1, 2, 3, 4, 5, 6]
        self.assertTrue(subject.linearSearch(a_list, 4))
        another_List = [20, 10, 90, 1005, 1]
        self.assertTrue(subject.linearSearch(another_List, 1))
        #added a comment
        self.assertFalse(subject.linearSearch(another_List, 100))

    def test_swap_pos(self):
        subject = RunTimeExercises()
        list = [13, 50, 18, 95]
        result = [18, 50, 13, 95]
        pos1, pos2 = 0, 2
        self.assertEqual(subject.swap_positions(list, pos1, pos2, ),result)

    def test_search2lists(self):
        subject = RunTimeExercises()
        listA = [4, 20, 7, 5, 12, 54, 21, 64, 12, 32]
        listB = [5, 3, 3, 8, 16, 14, 54, 56, 22, 65, 72, 2]
        self.assertTrue(subject.search_two_lists(listA,listB,3))
        self.assertFalse(subject.search_two_lists(listA, listB, 100))

    def test_findMax(self):
        subject = RunTimeExercises()
        a_list = [1, 2, 3, 4, 5, 6]
        self.assertEqual(6, subject.findMax(a_list))
        another_List = [20, 10, 90, 1005, 1]
        self.assertEqual(subject.findMax(another_List), 1005)
        self.assertIsNot(subject.findMax(another_List), 2000)

    def test_prefix_average(self):
        list1 = [1, 2, 3, 4, 5, 6]
        subject = RunTimeExercises()
        result_list = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
        self.assertEqual(result_list, subject.prefix_average(list1))

        list2 = [1, 2]
        result_list2 = [1.0, 1.5]
        self.assertEqual(result_list2, subject.prefix_average(list2))

    def test_binarySearch(self):
        a_list = [5, 12, 18, 19, 26, 46, 64, 78, 90, 120]
        subject = RunTimeExercises()
        low = 0
        high = len(a_list) - 1
        self.assertTrue(subject.binarySearch(a_list, 46, low, high))
        self.assertFalse(subject.binarySearch(a_list, 10000, low, high))


if __name__ == '__main__':
    unittest.main()
