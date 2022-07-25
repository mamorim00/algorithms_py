# file name: tree.py, author: Marina and Daniel ,
#  version: 1.0, date: 04/18/2021, course: CSCI 262,
#  Traverse the tree and count the leaves


class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def getRoot(self):
        return self.root
    
    def add(self,value):
        if (self.root == None):	
            self.root = Node(value)
        else:	
            self.addNode(value,self.root)

    def addNode(self,value,node):
        if value < node.data:
            if (node.left is None):	
                node.left = Node(value)
            else:
                self.addNode(value,node.left)
        else:
            if (node.right is None):	
                node.right = Node(value)
            else:						
                self.addNode(value,node.right)
                
    def find(self,value):
        if self.root is None:
            return None
        else:
            self.findNode(value, self.root)

    def findNode(self,value,node):
        if node is None: 
            return None
        if value == node.data: 
            return node
        elif value < node.data:
            self.findNode(value,node.left)
        elif value > node.data:
            self.findNode(value,node.right)
            
    def printTree(self):
        if self.root is not None:
            self.printTreeFromNode(self.root)
    
    def printTreeFromNode(self,node):
        if node is not None:
            self.printTreeFromNode(node.left)
            print(str(node.data))
            self.printTreeFromNode(node.right)
    
    def returnInOrderTree(self):
        if self.root is not None:
            return self.inOrderList(self.root)
    
    def inOrderList(self, node):
        nodeList = []
        if node is not None:
            nodeList = self.inOrderList(node.left)
            nodeList.append(node.data)
            nodeList = nodeList + self.inOrderList(node.right)
        return nodeList

    def returnPreOrderTree(self):
        if self.root is not None:
            return self.preOrderList(self.root)
    
    def preOrderList(self, node):
        nodeList = []
        if node is not None:
            nodeList.append(node.data)
            nodeList = nodeList + self.preOrderList(node.left)
            nodeList = nodeList + self.preOrderList(node.right)
        return nodeList

    def returnPostOrderTree(self):
        if self.root is not None:
            return self.postOrderList(self.root)
    
    def postOrderList(self, node):
        nodeList = []
        if node is not None:
            nodeList = self.postOrderList(node.left)
            nodeList = nodeList + self.postOrderList(node.right)
            nodeList.append(node.data)
        return nodeList

    def countTreeLeaf(self):
      if self.root is not None:
        return self.countLeaf(self.root)

    def countLeaf(self,node):
      if node is None:
        return 0
      elif (node.left is None and node.right is None):
        return 1
      else:
        return self.countLeaf(node.left)+ self.countLeaf(node.right)
    
    
   
    
   

def testInorder(testNumber,nodeList,expectedResult):
  actualResult = (generateTree(nodeList).returnInOrderTree())
  if actualResult == expectedResult: print ("Test Inorder",testNumber,"passed.")
  else: print ("Test Inorder ",testNumber,"failed.  Expected",expectedResult, "but found",actualResult)

def testA():
  testInorder(1,[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8])
  testInorder(2,[7,2,11,5,10,3,6,9,1,8],[1,2,3,5,6,7,8,9,10,11])
  testInorder(3,[],None)
  testInorder(4,[3,7,2,5,6],[2,3,5,6,7])
  testInorder(5,[5,6,2,1,3],[1,2,3,5,6])
  testInorder(6,[10,5,12,11,20],[5, 10,11,12,20])

def testPreOrder(testNumber,nodeList,expectedResult):
  actualResult = (generateTree(nodeList).returnPreOrderTree())
  if actualResult == expectedResult: print ("Test Preorder",testNumber,"passed.")
  else: print ("Test Pre order ",testNumber,"failed.  Expected",expectedResult, "but found",actualResult)

def testB():
  testPreOrder(1,[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8])
  testPreOrder(2,[7,2,11,5,10,3,6,9,1,8],[7, 2, 1, 5, 3, 6, 11, 10, 9, 8])
  testPreOrder(3,[],None)
  testPreOrder(4,[3,7,2,5,6],[3, 2, 7, 5, 6])
  testPreOrder(5,[5,6,2,1,3],[5,2,1,3,6])
  testPreOrder(6,[10,5,12,11,20],[10, 5, 12, 11, 20])

def testPostOrder(testNumber,nodeList,expectedResult):
  actualResult = (generateTree(nodeList).returnPostOrderTree())
  if actualResult == expectedResult: print ("Test Postorder",testNumber,"passed.")
  else: print ("Test Postorder ",testNumber,"failed.  Expected",expectedResult, "but found",actualResult)

def testC():
  testPostOrder(1,[1,2,3,4,5,6,7,8],[8, 7, 6, 5, 4, 3, 2, 1])
  testPostOrder(2,[7,2,11,5,10,3,6,9,1,8],[1, 3, 6, 5, 2, 8, 9, 10, 11, 7])
  testPostOrder(3,[],None)
  testPostOrder(4,[3,7,2,5,6],[2,6,5,7,3])
  testPostOrder(5,[5,6,2,1,3],[1,3,2,6,5])
  testPostOrder(6,[10,5,12,11,20], [5, 11, 20, 12, 10])

def testNumLeafs(testNumber,nodeList,expectedResult):
  actualResult = (generateTree(nodeList).countTreeLeaf())
  if actualResult == expectedResult: print ("testNumLeafs",testNumber,"passed.")
  else: print ("testNumLeafs ",testNumber,"failed.  Expected",expectedResult, "but found",actualResult)

def testD():
  testNumLeafs(1,[1,2,3,4,5,6,7,8],1)
  testNumLeafs(2,[7,2,11,5,10,3,6,9,1,8],4)
  testNumLeafs(3,[],None)
  testNumLeafs(4,[3,7,2,5,6],2)
  testNumLeafs(5,[5,6,2,1,3],3)
  testNumLeafs(6,[10,5,12,11,20], 3)




def generateTree(nodeList):
  tree = Tree()
  for value in nodeList:
    tree.add(value)
  return tree

def main():
    tree = Tree()
    for value in [5, 3, 4, 9, 1, 6]:
        tree.add(value)
    tree.printTree()
    print(tree.returnInOrderTree())
    print(tree.returnPreOrderTree())
    print(tree.returnPostOrderTree())
    print(tree.countLeaf(tree.root))
    
  

main()
testA()
testB()
testC()
testD()