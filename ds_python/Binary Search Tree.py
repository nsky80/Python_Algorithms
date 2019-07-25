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
                cur = self.insert(root.left,data)
                root.left = cur
            else:
                cur = self.insert(root.right,data)
                root.right = cur
        return root

    def printInorder(self, root):

        if root:
            # First recur on left child
            Solution.printInorder(self, root.left)

            # then print the data of node
            print(root.data, end=" ")

            # now recur on right child
            Solution.printInorder(self, root.right)


    def getHeight(self, root):
        # Write your code here
        if root is None:
            return -1
        else:
            ldepth = Solution.getHeight(self, root.left)
            rdepth = Solution.getHeight(self, root.right)

            if ldepth > rdepth:
                return ldepth + 1
            else:
                return rdepth + 1


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.printInorder(root)
height = myTree.getHeight(root)
print("\n", height)
