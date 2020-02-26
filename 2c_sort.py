class Node:
    def __init__(self,val):
        self.val=val
        self.left=None 
        self.right=None 

class BST:
    def __init__(self,val):
        self.root=Node(val)

    def insert(self,num):
        self.insertHelper(num,self.root)
    def insertHelper(self,num,currNode):
        if currNode!=None:
            if num>currNode.val:
                if currNode.right==None:
                    currNode.right=Node(num)
                else:
                    self.insertHelper(num,currNode.right)
            else:
                if currNode.left==None:
                    currNode.left=Node(num)
                else:
                    self.insertHelper(num,currNode.left)
    def inOrder(self):
        return self.inOrderHelper(self.root)
    def inOrderHelper(self,currNode):
        arr=[]
        if currNode!=None:
            arr.extend(self.inOrderHelper(currNode.left))
            arr.append(currNode.val)
            arr.extend(self.inOrderHelper(currNode.right))
        return arr


unsorted=[10,4,5,3,1,2,8,11,14,13,15]
tree=BST(unsorted[0])
for num in unsorted[1:]:
    tree.insert(num)

#sorted answer
print(tree.inOrder())