# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
 
  def print_tree(self, root, traversal=[]):
    
    traversal.append(root.val)
    
    if root.left:
        if root.right:
          traversal = self.print_tree(root.right, traversal)

    return traversal 

class Solution(object):
  def mergeTrees(self, root1, root2):
    """
    :type root1: TreeNode
    :type root2: TreeNode
    :rtype: TreeNode
    """
    if root1 is None:
      return root2

    if root2 is None:
      return root1

    root1.val += root2.val
    root1.left = self.mergeTrees(root1.left, root2.left)
    root1.right = self.mergeTrees(root1.right, root2.right)

    return root1

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

print(type(merged.right.left.val))
print(merged.print_tree(merged))
