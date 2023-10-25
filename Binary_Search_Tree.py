class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.height = 1
      # TODO complete Node initialization

  def __init__(self):
    self.__root = None
    # TODO complete initialization
    
  def __get_sub_height(self, subroot):
    if subroot.left and subroot.right:
      return max(subroot.left.height, subroot.right.height) + 1
    elif subroot.left or subroot.right:
      return (subroot.right.height if subroot.right else subroot.left.height) + 1
    else:
      return 1

  def __get_bal(self, subroot):
    if subroot.left and subroot.right:
      return subroot.right.height - subroot.left.height
    elif subroot.right:
      return subroot.right.height
    elif subroot.left:
      return 0 - subroot.left.height
    else:
      return 0

  def __balance(self, subroot):
    if self.__get_bal(subroot) not in [-1,0,1]:
      if self.__get_bal(subroot) < -1 and self.__get_bal(subroot.left) <= 0:
        subroot = self.__rotate_right(subroot)
        subroot.right.height = self.__get_sub_height(subroot.right)
        subroot.height = self.__get_sub_height(subroot)
      elif self.__get_bal(subroot) < -1 and self.__get_bal(subroot.left) > 0:
        subroot.left = self.__rotate_left(subroot.left)
        subroot.left.left.height = self.__get_sub_height(subroot.left.left)
        subroot.left.height = self.__get_sub_height(subroot.left)
        subroot = self.__rotate_right(subroot)
        subroot.right.height = self.__get_sub_height(subroot.right)
        subroot.height = self.__get_sub_height(subroot)
      elif self.__get_bal(subroot) > 1 and self.__get_bal(subroot.right) >= 0:
        subroot = self.__rotate_left(subroot)
        subroot.left.height = self.__get_sub_height(subroot.left)
        subroot.height = self.__get_sub_height(subroot)
      elif self.__get_bal(subroot) > 1 and self.__get_bal(subroot.right) < 0:
        subroot.right = self.__rotate_right(subroot.right)
        subroot.right.right.height = self.__get_sub_height(subroot.right.right)
        subroot.right.height = self.__get_sub_height(subroot.right)
        subroot = self.__rotate_left(subroot)
        subroot.left.height = self.__get_sub_height(subroot.left)
        subroot.height = self.__get_sub_height(subroot)
    subroot.height = self.__get_sub_height(subroot)
    return subroot

  def __rotate_left(self, subroot):
    floater = subroot.right.left
    subroot.right.left = subroot
    new = subroot.right
    subroot.right = floater
    return new

  def __rotate_right(self, subroot):
    floater = subroot.left.right
    subroot.left.right = subroot
    new = subroot.left
    subroot.left = floater
    return new

  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # TODO replace pass with your implementation
    self.__root = self.__rins(value, self.__root)

  def __rins(self, value, subroot):
    if not subroot:
      return self.__BST_Node(value)
    elif value < subroot.value:
      subroot.left = self.__rins(value, subroot.left)
    elif value > subroot.value:
      subroot.right = self.__rins(value, subroot.right)
    else:
      raise ValueError
    return self.__balance(subroot)

  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # TODO replace pass with your implementation
    self.__root = self.__rrem(value, self.__root)

  def __rrem(self, value, subroot):
    if not subroot:
      raise ValueError
    elif value < subroot.value:
      subroot.left = self.__rrem(value, subroot.left)
    elif value > subroot.value:
      subroot.right = self.__rrem(value, subroot.right)
    else:
      if subroot.left and subroot.right:
        self.__min_child(subroot.right)
        subroot.value = self.min.value
        subroot.right = self.__rrem(subroot.value, subroot.right)
      elif (not subroot.right) and (not subroot.left):
        return
      else:
        return subroot.right if subroot.right else subroot.left
    return self.__balance(subroot)

  def __min_child(self, subroot):
    if subroot.left:
      self.__min_child(subroot.left)
    else:
      self.min = subroot
    return

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
    if self.__root:
      self.__string = ''
      self.__rin_order(self.__root)
      return '[ ' + self.__string[2:len(self.__string)] + ' ]'
    return '[ ]'

  def __rin_order(self, subroot):
    if subroot.left:
      subroot.left = self.__rin_order(subroot.left)
    self.__string = self.__string + ', ' + str(subroot.value)
    if subroot.right:
      subroot.right = self.__rin_order(subroot.right)
    return subroot

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
    if self.__root:
      self.__string = ''
      self.__rpre_order(self.__root)
      return '[ ' + self.__string[2:len(self.__string)] + ' ]'
    return '[ ]'

  def __rpre_order(self, subroot):
    self.__string = self.__string + ', ' + str(subroot.value)
    if subroot.left:
      subroot.left = self.__rpre_order(subroot.left)
    if subroot.right:
      subroot.right = self.__rpre_order(subroot.right)
    return subroot

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
    if self.__root:
      self.__string = ''
      self.__rpost_order(self.__root)
      return '[ ' + self.__string[2:len(self.__string)] + ' ]'
    return '[ ]'

  def __rpost_order(self, subroot):
    if subroot.left:
      subroot.left = self.__rpost_order(subroot.left)
    if subroot.right:
      subroot.right = self.__rpost_order(subroot.right)
    self.__string = self.__string + ', ' + str(subroot.value)
    return subroot

  def to_list(self):
    self.__list = []
    if self.__root:
      self.__rto_list(self.__root)
    return self.__list

  def __rto_list(self, subroot):
    if subroot.left:
      subroot.left = self.__rto_list(subroot.left)
    self.__list.append(subroot.value)
    if subroot.right:
      subroot.right = self.__rto_list(subroot.right)
    return subroot

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    # TODO replace pass with your implementation
    if not self.__root:
      return 0
    return self.__root.height

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  pass #unit tests make the main section unnecessary.

