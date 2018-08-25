"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, l, r):

        # Both childs must exist
        if l is None and r is None:
            return True
        
        # Only one exists - not symmetric
        elif l is None or r is None:
            return False

        # Symmetric. Continue exploring
        elif l.val == r.val:
            out = self.isMirror(l.left, r.right)
            inn = self.isMirror(l.right, r.left)
            return out and inn

        # Not symmetric
        else:
            return False