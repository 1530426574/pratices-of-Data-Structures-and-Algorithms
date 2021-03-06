import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left, self.right = None, None


class Solution:  # 48ms
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        关键在哪呢？？先翻转，再遍历每个节点。
        """
        # 001 terminator
        if root is None:
            return None
        # 002 handle current level
        root.left, root.right = root.right, root.left
        # 003 dril down
        self.invertTree(root.left)
        self.invertTree(root.right)
        # 004 restore current level status
        return root


class Solution1:  # 44ms
    def invertTree(self, root: TreeNode) -> TreeNode:
        # node= root
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.right)
                stack.append(node.left)
        return root

    # recursively
    def invertTree1(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

    # BFS
    def invertTree2(self, root):
        queue = collections.deque([(root)])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left  # 变量引用对象，本质上是对象的调换。
                queue.append(node.left)
                queue.append(node.right)
        return root

    # DFS
    def invertTree3(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left  # 做选择
                stack.extend([node.right, node.left])  # 可以更换添加顺序。不一定非要左右，右左遍历一样可以。
        return root
