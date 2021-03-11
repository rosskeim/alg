# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
 
  def print_tree(self, traversal):
    if self.left:
      traversal.append(self.val)
      self.print_tree(self.left, traversal)
    elif self.right:
      traversal.append(self.val)
      self.print_tree(self.right, traversal)

    return traversal 

class Solution(object):
  def mergeTrees(self, root1, root2, traversal=[]):
    """
    :type root1: TreeNode
    :type root2: TreeNode
    :rtype: TreeNode
    """
    
    if root1:
      if root2:
        traversal.append(root1.val+root2.val)
      else
        traversal.append(root1.val)
    elif root2:
      traversal.append(root2.val)

    if root1.left:
      if root2.left:
        root1.left = self.mergeTrees(root1.left, root2.left)
      else:
        root1.left = self.mergeTrees(root1.left, TreeNode())
    elif root1.right:
      if root2.right:
        root1.right = self.mergeTrees(root1.right, root2.right)
      else:
        root1.right = self.mergeTrees(root1.right, TreeNode())

    return TreeNode(root1.val+root2.val) 

obj = Solution()

root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.left.left = TreeNode(5)
root1.right = TreeNode(2)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.left.right = TreeNode(4)
root2.right = TreeNode(3)
root2.right.right = TreeNode(7)

merged = obj.mergeTrees(root1, root2)

traversal = [3]
print(root2.left.right.val)
print(merged.print_tree(traversal))
