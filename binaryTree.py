import math
class treeNode():
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
        return 

class Stack():
    def __init__(self):
        self.list = []

    def empty(self):
        return len(self.list) == 0

    def pop(self):
        if self.empty() ==True:
            return False
        else:
            currentValue = self.list[len(self.list)-1]
            self.list.remove(self.list[len(self.list)-1])
            return currentValue
        
    def push(self,value):
        try:
            self.list.append(value)
            return True
        except:
            return False

class Queue():
    def __init__(self):
        self.list = []

    def empty(self):
        return len(self.list) == 0

    def offer(self,value):
        try:
            self.list.append(value)
            return True
        except:
            return False

    def remove(self):
        if self.empty() == True:
            return False
        else:
            currentValue = self.list[0]
            self.list.remove(self.list[0])
            return currentValue

def depthFirstValue(root):
    stack = Stack()
    string = "depthFirstValue travels:"
    stack.push(root)
    
    while stack.empty() != True:
        currentNode = stack.pop()
        string += " "+ str(currentNode.value)
        if currentNode.right!= None:
            stack.push(currentNode.right)
        if currentNode.left!=None:
            stack.push(currentNode.left)
    return string

def breadthFirstValue(root):
    queue = Queue()
    string = "breadthFirstValue travels:"
    queue.offer(root)

    while queue.empty()!=True:
        currentNode = queue.remove()
        string += " " + str(currentNode.value)
        if currentNode.left!=None:
            queue.offer(currentNode.left)
        if currentNode.right!=None:
            queue.offer(currentNode.right)
    return string

def treeIncludes(root, value):
    queue = Queue()
    queue.offer(root)

    while queue.empty()!=True:
        currentNode = queue.remove()
        if currentNode.value == value:
            return True
        if currentNode.left!=None:
            queue.offer(currentNode.left)
        if currentNode.right!=None:
            queue.offer(currentNode.right)
    return False

def treeSum(root):
    if root == None:
        return 0
    else:
        return root.value +treeSum(root.right) + treeSum(root.left)

def treeMinValue(root):
    queue = Queue()
    queue.offer(root)
    minimum = None
    while queue.empty()!=True:
        currentNode = queue.remove()
        if minimum == None:
            minimum = currentNode.value
        else:
            if minimum >currentNode.value:
                minimum = currentNode.value
            else:
                pass
        if currentNode.left!=None:
            queue.offer(currentNode.left)
        if currentNode.right!=None:
            queue.offer(currentNode.right)
    return minimum

def maxRootToLeafPathSum(root):
    if root == None:
        return -math.inf

    elif root.left == None and root.right == None:
        return root.value

    else:
        return (root.value +
                max(maxRootToLeafPathSum(root.left),
                    maxRootToLeafPathSum(root.right)))
        
a = treeNode(1)
b = treeNode(2) 
c = treeNode(3)
d = treeNode(9)
e = treeNode(5)
f = treeNode(6)

a.left = b
a.right = c 
b.left = d 
b.right = e
c.right = f

print(depthFirstValue(a))
print(breadthFirstValue(a))
print(treeIncludes(a,1))
print(treeSum(a))
print(treeMinValue(a))
print(maxRootToLeafPathSum(a))