class Queue:
    def __init__(self):
        self.array = []

    def enqueue(self, data):
        self.array.append(data)
    
    def dequeue(self):
        self.array.pop(0)

    def isEmpty(self):
        if len(self.array) == 0:
            return False
        return True

class BSTNode:
    def __init__(self, data):
        self.data = data

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def levelOrderTraversal(self):
        queue = Queue()
        queue.enqueue(self.root)

        if self.root == None:
            return

        allvalue = []
        while queue.isEmpty():
            node = queue.dequeue()
            allvalue.append(node.data)

            if node.left:
                queue.enqueue(node.left)
            
            if node.right:
                queue.enqueue(node.right)




    
    
    