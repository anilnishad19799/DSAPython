class AVLNode:
    def __init__(self, data, balanceFactor=0, left=None, right=None):
        self.data = data
        self.balanceFactor = balanceFactor
        self.left = left
        self.right = right

class AVLTree:
    def __init__(self):
        self.root = None

    def inOrderPrint(self):
        self.recInOrderPrint(self.root)

    def recInOrderPrint(self, root):
        if root is not None:
            self.recInOrderPrint(root.left)
            print(root.data)
            self.recInOrderPrint(root.right)

    def insert(self, data):
        newNode = AVLNode(data)
        self.root, taller = self.recInsertAVL(self.root, newNode)

    def recInsertAVL(self, root, newNode):
        print("1"*10)
        print("In rectInsertAVL")
        if root is None:
            print("1. First case root is None so define new node")
            root = newNode
            root.balanceFactor = 0
            taller = True
        elif newNode.data < root.data:
            print("2. newnodedata", newNode.data , " < root.data", root.data)
            root.left, taller = self.recInsertAVL(root.left, newNode)

            print("root value", root.data, "root.left value", root.left.data)
            if taller:
                print("2.1 Taller true ")
                if root.balanceFactor == 0:
                    print("2.2 root.balanceFactor 0 ")
                    root.balanceFactor = -1
                    taller = False
                elif root.balanceFactor == 1:
                    print("2.3 root.balanceFactor 1 ")
                    root.balanceFactor = 0
                    taller = False
                else:
                    print("2.3 Esle root.balanceFactor rightleftrotate call")
                    root = self.rightLeftRotate(root)
                    taller = False
        else:
            print("3. newnodedata", newNode.data , " > root.data", root.data)
            root.right, taller = self.recInsertAVL(root.right, newNode)
            print("root value", root.data, "root.left value", root.left.data)

            if taller:
                print("3.1 Taller true ")
                if root.balanceFactor == -1:
                    print("3.2 root.balanceFactor -1")
                    root.balanceFactor = 0
                    taller = False
                elif root.balanceFactor == 0:
                    print("3.3 root.balanceFactor 0")
                    root.balanceFactor = 1
                    taller = False
                else:
                    print("3.3 Esle root.balanceFactor leftRightRotate call")
                    root = self.leftRightRotate(root)
                    taller = False
        return root, taller

    def rightLeftRotate(self, root):
        print("R*",10)
        print("Inside rightLeftRotate")
        print("Here root value", root.data)
        X = root.left
        if X.balanceFactor == -1:
            root.balanceFactor = 0
            X.balanceFactor = 0
            root = self.singleRightRotate(root)
        else:
            Y = X.right
            if Y.balanceFactor == -1:
                root.balanceFactor = 1
                X.balanceFactor = 0
            elif Y.balanceFactor == 0:
                root.balanceFactor = 0
                X.balanceFactor = 0
            else:
                root.balanceFactor = 0
                X.balanceFactor = -1
            Y.balanceFactor = 0
            root.left = self.singleRightRotate(root.left)
            root = self.singleLeftRotate(root)
        return root

    def leftRightRotate(self, root):
        print("L*",10)
        print("Inside leftRightRotate")
        print("Here root value", root.data)
        X = root.right
        if X.balanceFactor == 1:
            root.balanceFactor = 0
            X.balanceFactor = 0
            root = self.singleLeftRotate(root)
        else:
            Y = X.left
            if Y.balanceFactor == -1:
                root.balanceFactor = 0
                X.balanceFactor = 1
            elif Y.balanceFactor == 0:
                root.balanceFactor = 0
                X.balanceFactor = 0
            else:
                root.balanceFactor = -1
                X.balanceFactor = 0
            Y.balanceFactor = 0
            root.right = self.singleLeftRotate(root.right)
            root = self.singleRightRotate(root)
        return root

    def singleRightRotate(self, root):
        X = root.right
        root.right = X.left
        X.left = root
        root.balanceFactor = max(self.getBalanceFactor(root.left), self.getBalanceFactor(root.right)) + 1
        X.balanceFactor = max(self.getBalanceFactor(X.right), root.balanceFactor) + 1
        return X

    def singleLeftRotate(self, root):
        W = root.left
        root.left = W.right
        W.right = root
        root.balanceFactor = max(self.getBalanceFactor(root.left), self.getBalanceFactor(root.right)) + 1
        W.balanceFactor = max(self.getBalanceFactor(W.left), root.balanceFactor) + 1
        return W

    def getBalanceFactor(self, node):
        if not node:
            return 0
        return node.balanceFactor

    def height(self):
        return self.recHeight(self.root)

    def recHeight(self, root):
        if root is None:
            return 0
        else:
            leftH = self.recHeight(root.left)
            rightH = self.recHeight(root.right)
            return 1 + max(leftH, rightH)

def tester():
    avl = AVLTree()
    data = [3,1]
    for i in range(len(data)):
        avl.insert(data[i])

    print("#"*10)
    print("In order print")
    avl.inOrderPrint()
    print("Height =", avl.height())

if __name__ == "__main__":
    tester()
