class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

heightNodeDict = {}
def getNodeHeight(node):
    if node:
        if node in heightNodeDict:
            height = heightNodeDict[node]
            return heightNodeDict[node]
        else:
            heightLeft, heightRight = getNodeHeight(node.left), getNodeHeight(node.right)
            if node.left:
                heightLeft += 1
            if node.right:
                heightRight += 1
            heightNodeDict[node] = max(heightLeft, heightRight)
            return heightNodeDict[node]
    else:
        return 0

def diameterOfBinaryTree(root):
    if root:
        leftHeight, rightHeight = 0, 0
        if root.left:
            leftHeight = getNodeHeight(root.left)
            leftHeight += 1
        if root.right:
            rightHeight = getNodeHeight(root.right)
            rightHeight += 1
        diameter = leftHeight + rightHeight
        return max(diameter, diameterOfBinaryTree(root.left), diameterOfBinaryTree(root.right))
    else:
        return 0
        
a = Node(1)
a.left = Node(2)
a.left.left = Node(4)
a.left.right = Node(5)
a.right = Node(3)
print(diameterOfBinaryTree(a))