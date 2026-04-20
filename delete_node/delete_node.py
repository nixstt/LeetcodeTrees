'''delete node'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key == root.val:
            if not root.right and not root.left:
                return None
            if root.right and not root.left:
                return root.right
            elif root.right and root.left:
                minimum = root.right
                while minimum.left:
                    minimum = minimum.left
                root.val = minimum.val
                root.right = self.deleteNode(root.right, minimum.val)
                return root
            else:
                return root.left
        return root
