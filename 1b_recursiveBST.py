#end with Rec 
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None 
        self.right=None 

class BST:
    def __init__(self,val):
        self.root=Node(val)

    def insertRec(self,num):
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
        else:
            # Meaning root is none since we never check if currNode is an empty node except when we start at root 
            self.root=Node(num)
    def fixir(self):
        # ok so i could NOT find a reason why the val of some nodes that were "removed"
        # were set to None in SOME cases, the tree is still correct but there are "None" value gaps between values
        # i implemented a fixir class to remove the leftovers. 

        self.fixirHelper(self.root)
    def fixirHelper(self,currNode):
        if currNode!=None:
            if currNode.left!=None:
                if currNode.left.val==None:
                    currNode.left=currNode.left.left
                self.fixirHelper(currNode.left)
            elif currNode.right!=None:
                if currNode.right.val==None:
                    currNode.right=currNode.right.right
                self.fixirHelper(currNode.right)

    def deleteRec(self,num):
        self.deleteHelper(self.root,num)
    def deleteHelper(self,currNode,num):
        #in this case, current is the starting root
        if currNode!=None:
            #only occurs with root node
            if currNode.val==num:
                targetNode=currNode
                #NO LEAVES on deletion node
                if targetNode.right==None and targetNode.left==None:
                    currNode=None
                #ONE LEAF on either side
                if targetNode.right==None and targetNode.left!=None:
                    currNode=targetNode.left
                if targetNode.right!=None and targetNode.left==None: 
                    currNode=targetNode.right
                 #TWO LEAVES
                else:
                   # if targetNode.left!=None:
                    highest=self.findMaxHelper(targetNode.left)
                    if highest==None and targetNode.left!=None:
                        targetNode.val=targetNode.left.val
                        targetNode.left=None
                    else:
                        targetNode.val=highest
                        self.deleteHelper(targetNode.left,highest)
                    self.fixir()
            elif currNode.left!=None and currNode.left.val==num:
                targetNode=currNode.left
                #NO LEAVES on deletion node
                if targetNode.right==None and targetNode.left==None:
                    currNode.left=None
                #ONE LEAF on either side
                if targetNode.right==None and targetNode.left!=None:
                    currNode.left=targetNode.left
                if targetNode.right!=None and targetNode.left==None: 
                    currNode.left=targetNode.right
                 #TWO LEAVES
                else:
                    highest=self.findMaxHelper(targetNode.left)
                    targetNode.val=highest
                    self.deleteHelper(targetNode.left,highest)
                    self.fixir()
            #NO LEAVES on deletion node
            elif currNode.right!=None and currNode.right.val==num:
                targetNode=currNode.right
                #NO LEAVES on deletion node
                if targetNode.right==None and targetNode.left==None:
                    currNode.right=None
                #ONE LEAF on either side
                if targetNode.right==None and targetNode.left!=None:
                    currNode.right=targetNode.left
                if targetNode.right!=None and targetNode.left==None: 
                    currNode.right=targetNode.right
                 #TWO LEAVES
                else:
                    highest=self.findMaxHelper(targetNode.left)
                    targetNode.val=highest
                    self.deleteHelper(targetNode.left,highest)
                    self.fixir()
            elif num>currNode.val:
                self.deleteHelper(currNode.right,num)
            elif num<currNode.val:
                self.deleteHelper(currNode.left,num)
            
    def findMaxRec(self):
        return self.findMaxHelper(self.root)
    def findMaxHelper(self,currNode):
        if currNode!=None:
            res=currNode.val
            if currNode.right!=None:
                res=self.findMaxHelper(currNode.right)
            return res
        else:
            return None

    def findMinRec(self):
        return self.findMinHelper(self.root)
    def findMinHelper(self,currNode):
        if currNode!=None:
            res=currNode.val
            if currNode.left!=None:
                res=self.findMinHelper(currNode.left)
            return res
        else:
            return None

    def inOrderRec(self):
        return self.inOrderHelper(self.root)
    def inOrderHelper(self,currNode):
        arr=[]
        if currNode!=None:
            arr.extend(self.inOrderHelper(currNode.left))
            arr.append(currNode.val)
            arr.extend(self.inOrderHelper(currNode.right))
        return arr
        
    def findNextRec(self,num):
        return self.findNextHelper(self.root,num)
    def findNextHelper(self,currNode,num):
        # I implemented a recursive inOrder traversal to make this problem simple at the cost of space and some time complexity on average
        ordered=self.inOrderRec()
        if num in ordered:
            if num!=ordered[-1]:
                return ordered[ordered.index(num)+1]
        return None

    def findPrevRec(self,num):
        return self.findPrevHelper(self.root,num)
    def findPrevHelper(self,currNode,num):
        # I implemented a recursive inOrder traversal to make this problem simple
        ordered=self.inOrderRec()
        if num in ordered:
            if num!=ordered[0]:
                return ordered[ordered.index(num)-1]
        return None

    def printTreeRec(self,currNode):
        if currNode!=None:
            # Pre-order traversal for debugging / visualizing the tree
            print(currNode.val, end=" ")
            self.printTreeRec(currNode.left)
            self.printTreeRec(currNode.right)
            

tree=BST(20)
tree.insertRec(10)
tree.insertRec(15)
tree.insertRec(12)
tree.insertRec(16)
tree.printTreeRec(tree.root)
print("")
print(tree.findPrevRec(12))
tree.deleteRec(20)
tree.printTreeRec(tree.root)
