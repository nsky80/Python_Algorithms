import sys


#
# Sample Input
#
# 6
# 3
# 5
# 4
# 7
# 2
# 1
# Sample Output
#
# 3 2 5 1 4 7


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    queue = []

    def levelOrder(self, root):
        # Write your code here
        if root is not None:
            Solution.queue.append(root)
            while Solution.queue:
                tree = Solution.queue.pop(0)
                print(tree.data, end=' ')
                if tree.left:
                    Solution.queue.append(tree.left)
                if tree.right:
                    Solution.queue.append(tree.right)


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
