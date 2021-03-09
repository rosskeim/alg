# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  
  def print_tree():
    if self.left:
      self.left.print_tree()
    elif self.right:
      self.right.print_tree()

    return self.val

class Solution(object):
  def mergeTrees(self, root1, root2):
    """
    :type root1: TreeNode
    :type root2: TreeNode
    :rtype: TreeNode
    """

    if root1.left:
      if root2.left:
        root1.left = mergeTrees(root1.left, root2.left)
      else:
        root1.left = mergeTrees(root1.left, TreeNode())
    elif root1.right:
      if root2.right:
        root1.right = mergeTrees(root1.right, root2.right)
      else:
        root1.right = mergeTrees(root1.right, TreeNode())
      
    return TreeNode(root1.val+root2.val)
