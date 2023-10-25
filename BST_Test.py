import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BST_Tester(unittest.TestCase):
    
    def setUp(self):
        self.__BST = Binary_Search_Tree()

    def test_empty_str(self):
        self.assertEqual('[ ]', str(self.__BST))

    def test_empty_traverse(self):
        self.assertEqual('[ ][ ][ ]', str(self.__BST.in_order()) + str(self.__BST.pre_order()) + str(self.__BST.post_order()))

    def test_empty_height(self):
        self.assertEqual(0, self.__BST.get_height())

    def test_ins_one_str(self):
        self.__BST.insert_element(50)
        self.assertEqual('[ 50 ]', str(self.__BST))

    def test_ins_one_traverse(self):
        self.__BST.insert_element(50)
        self.assertEqual('[ 50 ][ 50 ][ 50 ]', str(self.__BST.in_order()) + str(self.__BST.pre_order()) + str(self.__BST.post_order()))

    def test_ins_one_height(self):
        self.__BST.insert_element(50)
        self.assertEqual(1, self.__BST.get_height())

    def test_ins_greater_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.assertEqual('[ 50, 60 ]', str(self.__BST))

    def test_ins_greater_traverse(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.assertEqual('[ 50, 60 ][ 50, 60 ][ 60, 50 ]', str(self.__BST.in_order()) + str(self.__BST.pre_order()) + str(self.__BST.post_order()))

    def test_ins_greater_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.assertEqual(2, self.__BST.get_height())

    def test_ins_less_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(40)
        self.assertEqual('[ 40, 50 ]', str(self.__BST))

    def test_ins_less_traverse(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(40)
        self.assertEqual('[ 40, 50 ][ 50, 40 ][ 40, 50 ]', str(self.__BST.in_order()) + str(self.__BST.pre_order()) + str(self.__BST.post_order()))

    def test_ins_less_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(40)
        self.assertEqual(2, self.__BST.get_height())

    def test_ins_greater_less_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.__BST.insert_element(40)
        self.assertEqual('[ 40, 50, 60 ]', str(self.__BST))

    def test_ins_greater_less_traverse(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.__BST.insert_element(40)
        self.assertEqual('[ 40, 50, 60 ][ 50, 40, 60 ][ 40, 60, 50 ]', str(self.__BST.in_order()) + str(self.__BST.pre_order()) + str(self.__BST.post_order()))

    def test_ins_greater_less_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.__BST.insert_element(40)
        self.assertEqual(2, self.__BST.get_height())

    def test_ins_rotate_left_str(self): 
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.__BST.insert_element(70)
        self.assertEqual('[ 50, 60, 70 ]', str(self.__BST))

    def test_ins_rotate_left_traverse(self): 
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.__BST.insert_element(70)
        self.assertEqual('[ 50, 60, 70 ][ 60, 50, 70 ][ 50, 70, 60 ]', str(self.__BST.in_order()) + str(self.__BST.pre_order()) + str(self.__BST.post_order()))

    def test_ins_rotate_left_height(self): 
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.__BST.insert_element(70)
        self.assertEqual(2, self.__BST.get_height())

    def test_ins_rotate_right_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(40)
        self.__BST.insert_element(30)
        self.assertEqual('[ 30, 40, 50 ]', str(self.__BST))

    def test_ins_rotate_right_traverse(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(40)
        self.__BST.insert_element(30)
        self.assertEqual('[ 30, 40, 50 ][ 40, 30, 50 ][ 30, 50, 40 ]', str(self.__BST.in_order()) + str(self.__BST.pre_order()) + str(self.__BST.post_order()))

    def test_ins_rotate_right_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(40)
        self.__BST.insert_element(30)
        self.assertEqual(2, self.__BST.get_height())

    def test_ins_rotate_left_right_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(40)
        self.assertEqual('[ 30, 40, 50 ]', str(self.__BST))

    def test_ins_rotate_left_right_traverse(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(40)
        self.assertEqual('[ 30, 40, 50 ][ 40, 30, 50 ][ 30, 50, 40 ]', str(self.__BST.in_order()) + str(self.__BST.pre_order()) + str(self.__BST.post_order()))

    def test_ins_rotate_left_right_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(40)
        self.assertEqual(2, self.__BST.get_height())

    def test_ins_rotate_right_left_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(60)
        self.assertEqual('[ 50, 60, 70 ]', str(self.__BST))

    def test_ins_rotate_right_left_traverse(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(60)
        self.assertEqual('[ 50, 60, 70 ][ 60, 50, 70 ][ 50, 70, 60 ]', str(self.__BST.in_order()) + str(self.__BST.pre_order()) + str(self.__BST.post_order()))

    def test_ins_rotate_right_left_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(60)
        self.assertEqual(2, self.__BST.get_height())

    def test_remove_one_root_str(self):
        self.__BST.insert_element(50)
        self.__BST.remove_element(50)
        self.assertEqual('[ ]', str(self.__BST))

    def test_remove_one_root_traverse(self):
        self.__BST.insert_element(50)
        self.__BST.remove_element(50)
        self.assertEqual('[ ][ ][ ]', str(self.__BST.in_order()) + str(self.__BST.pre_order()) + str(self.__BST.post_order()))

    def test_remove_one_root_height(self):
        self.__BST.insert_element(50)
        self.__BST.remove_element(50)
        self.assertEqual(0, self.__BST.get_height())

    def test_remove_one_leaf_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.remove_element(30)
        self.assertEqual('[ 50 ]', str(self.__BST))

    def test_remove_one_leaf_traverse(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.remove_element(30)
        self.assertEqual('[ 50 ][ 50 ][ 50 ]', str(self.__BST.in_order()) + str(self.__BST.pre_order()) + str(self.__BST.post_order()))

    def test_remove_one_leaf_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.remove_element(30)
        self.assertEqual(1, self.__BST.get_height())

    def test_remove_one_root_large_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(40)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(80)
        self.__BST.remove_element(50)
        self.assertEqual('[ 20, 30, 40, 60, 70, 80 ]', str(self.__BST))
        
    def test_remove_one_root_large_traverse(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(40)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(80)
        self.__BST.remove_element(50)
        self.assertEqual('[ 20, 30, 40, 60, 70, 80 ][ 60, 30, 20, 40, 70, 80 ][ 20, 40, 30, 80, 70, 60 ]', str(self.__BST.in_order()) + str(self.__BST.pre_order()) + str(self.__BST.post_order()))

    def test_remove_one_root_large_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(40)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(80)
        self.__BST.remove_element(50)
        self.assertEqual(3, self.__BST.get_height())

    def test_remove_rotate_left_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(80)
        self.__BST.remove_element(30)
        self.assertEqual('[ 50, 70, 80 ]', str(self.__BST))

    def test_remove_rotate_left_traverse(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(80)
        self.__BST.remove_element(30)
        self.assertEqual('[ 50, 70, 80 ][ 70, 50, 80 ][ 50, 80, 70 ]', str(self.__BST.in_order()) + str(self.__BST.pre_order()) + str(self.__BST.post_order()))

    def test_remove_rotate_left_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(80)
        self.__BST.remove_element(30)
        self.assertEqual(2, self.__BST.get_height())

    def test_remove_rotate_right_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(20)
        self.__BST.remove_element(70)
        self.assertEqual('[ 20, 30, 50 ]', str(self.__BST))

    def test_remove_rotate_right_traverse(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(20)
        self.__BST.remove_element(70)
        self.assertEqual('[ 20, 30, 50 ][ 30, 20, 50 ][ 20, 50, 30 ]', str(self.__BST.in_order()) + str(self.__BST.pre_order()) + str(self.__BST.post_order()))

    def test_remove_rotate_right_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(20)
        self.__BST.remove_element(70)
        self.assertEqual(2, self.__BST.get_height())

    def test_remove_rotate_right_left_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(60)
        self.__BST.remove_element(30)
        self.assertEqual('[ 50, 60, 70 ]', str(self.__BST))

    def test_remove_rotate_right_left_traverse(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(60)
        self.__BST.remove_element(30)
        self.assertEqual('[ 50, 60, 70 ][ 60, 50, 70 ][ 50, 70, 60 ]', str(self.__BST.in_order()) + str(self.__BST.pre_order()) + str(self.__BST.post_order()))

    def test_remove_rotate_right_left_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(60)
        self.__BST.remove_element(30)
        self.assertEqual(2, self.__BST.get_height())

    def test_remove_rotate_left_right_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(40)
        self.__BST.remove_element(70)
        self.assertEqual('[ 30, 40, 50 ]', str(self.__BST))

    def test_remove_rotate_left_right_traverse(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(40)
        self.__BST.remove_element(70)
        self.assertEqual('[ 30, 40, 50 ][ 40, 30, 50 ][ 30, 50, 40 ]', str(self.__BST.in_order()) + str(self.__BST.pre_order()) + str(self.__BST.post_order()))

    def test_remove_rotate_left_right_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(40)
        self.__BST.remove_element(70)
        self.assertEqual(2, self.__BST.get_height())


if __name__ == '__main__':
  unittest.main()