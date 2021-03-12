# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
 
  def print_tree(self, root, traversal=[]):
    h = self.height(root)
    for i in range(1, h+1):
      self.printLevel(root, i, traversal)
    
    return traversal

  def printLevel(self, root, level, traversal):
    if root is None:
      return
    if level == 1:
      traversal.append(root.val)
    elif level > 1:
      self.printLevel(root.left, level-1, traversal)
      self.printLevel(root.right, level-1, traversal)

  def height(self, root):
    if root is None:
      return 0
    else:
      lheight = self.height(root.left)
      rheight = self.height(root.right)

      if lheight > rheight:
        return lheight+1
      else:
        return rheight+1

class Solution(object):
  def mergeTrees(self, root1, root2):
    """
    :type root1: TreeNode
    :type root2: TreeNode
    :rtype: TreeNode
    """
    if root1 and root2:
      root = TreeNode(root1.val + root2.val)
      root.left = self.mergeTrees(root1.left, root2.left)
      root.right = self.mergeTrees(root1.right, root2.right)
      return root
    else:
      return root1 or root2

obj = Solution()

# [1,3,2,5]
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.left.left = TreeNode(5)
root1.right = TreeNode(2)

# [2,1,3,null,4,null,7]
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.left.right = TreeNode(4)
root2.right = TreeNode(3)
root2.right.right = TreeNode(7)

merged = obj.mergeTrees(root1, root2)

print(merged.print_tree(merged))
