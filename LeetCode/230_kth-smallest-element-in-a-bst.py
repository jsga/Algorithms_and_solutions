"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# This solution posted here is accepted. However it is inefficient and works for any kind of binary tree.
# Read again carefully that the given tree is a binary search tree. We only need to visit k nodes.

class Solution:
    def kthSmallest(self, root, k):

        # Gather all the elements in a list
        l = [root.val] + self.treeList(root.left) + self.treeList(root.right)

        # Sort the list
        l.sort()

        # Return the kth element
        return l[k - 1]

    def treeList(self, root):

        # Empty tree
        if root is None:
            return []

        # End of tree
        if root.left is None and root.right is None:
            return [root.val]

        # Move both ways
        else:
            return [root.val] + self.treeList(root.left) + self.treeList(root.right)