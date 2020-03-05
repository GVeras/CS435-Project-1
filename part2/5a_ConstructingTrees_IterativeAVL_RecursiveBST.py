import random

def getRandomArray(n):
    returnArray=[]
    while len(returnArray)!=n:
        randomNum=random.randint(1,n)
        if randomNum not in returnArray:
            returnArray.append(randomNum)
    return returnArray

#-----Iterative AVL-----
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None 
        self.right=None
        self.height=1
class AVL:
    def __init__(self,val):
        self.root=Node(val)

    def BF(self,currNode):
        if currNode==None:
            return 0
        L=R=0
        if currNode.left!=None:
            self.updateHeight(currNode.left)
            L=currNode.left.height
        if currNode.right!=None:
            self.updateHeight(currNode.right)
            R=currNode.right.height
        return L-R

    def updateHeight(self,startNode):
        #level order traversal, return the amount of levels
        if startNode!=None:
            levels=1
            stack=[startNode]
            temp=[]
            while stack:
                currNode=stack.pop()
                if currNode!=None:
                    temp.extend([currNode.right,currNode.left])
                #any true values in temp AKA no "None" value
                if stack==[] and any(temp):
                    levels+=1
                    stack=[node for node in temp]
                    temp=[]
            startNode.height=levels

    def insertIter(self,num):
        if self.root==None:
            self.root=Node(num)
        else:
            parent=self.root
            ancestors=[]
            while parent:
                ancestors.append(parent)
                if parent.val<num:
                    if parent.right==None:
                        parent.right=Node(num)
                        self.updateHeight(parent)
                        break
                    else:
                        #grandparent=parent
                        parent=parent.right
                else:
                    if parent.left==None:
                        parent.left=Node(num)
                        self.updateHeight(parent)
                        break
                    else:
                        parent=parent.left
            while ancestors:
                parent=ancestors.pop()
                if len(ancestors)>0:
                    grandparent=ancestors[-1]
                else:
                    break
                if len(ancestors)>1:
                    greatgrandparent=ancestors[-2]
                else:
                    greatgrandparent=self.root
                if abs(self.BF(grandparent))>1:
                    #print("rebalance")
                    self.rebalanceIter(parent,grandparent,greatgrandparent)
                #else:
                    #print("at val:",grandparent.val,self.BF(grandparent), "no rebalance needed")
                self.updateHeight(parent)
                self.updateHeight(grandparent)

    def rebalanceIter(self,parent,grandparent,greatgrandparent):
        #check Nones in case, for delete..
        newParent=None 
        balanceFactor=self.BF(grandparent)
        #R cases
        if balanceFactor<-1:
            if self.BF(parent)<0:
                #RR case
                grandparent.right=parent.left
                parent.left=grandparent
            else:
                #RL case
                newParent=parent.left 
                grandparent.right=newParent.left
                parent.left=newParent.right

                newParent.left=grandparent
                newParent.right=parent
        #L cases
        elif balanceFactor>1:
            if self.BF(parent)>0:
                #LL case
                grandparent.left=parent.right
                parent.right=grandparent
            else:
                #LR case
                newParent=parent.right 

                grandparent.left=newParent.right
                parent.right=newParent.left

                newParent.right=grandparent
                newParent.left=parent

        if grandparent==self.root:
            #CHANGED THIS
            if newParent!=None:
                self.root=newParent
                self.updateHeight(newParent)
            else:
                self.root=parent
        else:
            if greatgrandparent.val<grandparent.val:
                #right side of ancestor
                if newParent!=None:
                   greatgrandparent.right=newParent
                   self.updateHeight(newParent)
                else:
                    greatgrandparent.right=parent
            else:
                #left side of ancestor
                if newParent!=None:
                    greatgrandparent.left=newParent
                    self.updateHeight(newParent)
                else:
                    greatgrandparent.left=parent
                
    def findMinIter(self, *args):
        #args in this case for optional arguments, rather than always starting at root/having to make a helper function
        if len(args)==1:
            currNode=args[0]
        else:
            currNode=self.root
        if currNode==None:
            return None
        while currNode.left!=None:
            currNode=currNode.left
        return currNode.val

    def findMaxIter(self, *args):
        if len(args)==1:
            currNode=args[0]
        else:
            currNode=self.root
        if currNode==None:
            return None
        while currNode.right!=None:
            currNode=currNode.right
        return currNode.val

    def findNextIter(self,num, *args):
        if len(args)==1:
            currNode=args[0]
        else:
            currNode=self.root
        if currNode==None:
            return None
        res=float('inf')
        inTree=False

        while currNode!=None:
            if currNode.val==num:
                inTree=True
                res2=self.findMinIter(currNode.right)
                if res2!=None:
                    if res2>num:
                        res=min(res2-num,res)
                break
            else:
                if currNode.val>num:
                    res=min(currNode.val-num,res)

            if num>currNode.val:
                currNode=currNode.right
            else:
                currNode=currNode.left

        if res==float('inf') or not inTree:
            return None 
        return res + num

    def findPrevIter(self,num, *args):
        if len(args)==1:
            currNode=args[0]
        else:
            currNode=self.root
        if currNode==None:
            return None
        res=float('inf')
        inTree=False
        answer=0
        prev=res
        while currNode!=None:
            if currNode.val==num:
                inTree=True
                res2=self.findMaxIter(currNode.left)
                if res2!=None:
                    if res2<num:
                        res=min(num-res2,res)
                        if res!=prev:
                            answer=res2
                        prev=res
                break
            else:
                if currNode.val<num:
                    res=min(num-currNode.val,res)
                    if res!=prev:
                        answer=currNode.val
                    prev=res
            if num>currNode.val:
                currNode=currNode.right
            else:
                currNode=currNode.left
        if res==float('inf') or not inTree:
            return None 
        return answer
    
    def deleteIter(self,num):
        ancestors=[]
        currNode=self.root
        prev=currNode
        pMove=-1 #0 for left 1 for right, to represent which way currNode just went
        while currNode!=None:
            if currNode.val==num:
                if currNode.left!=None and currNode.right==None:
                    if prev==currNode:
                        self.root=currNode.left
                    else:
                        prev.left=currNode.left

                elif currNode.left==None and currNode.right!=None:
                    if prev==currNode:
                        self.root=currNode.right
                    else:
                        prev.right=currNode.right   
                elif currNode.left==None and currNode.right==None:
                    if prev==currNode:
                        self.root=None
                    else:
                        if pMove==1:
                            prev.right=None 
                        else:
                            prev.left=None
                else: #if neither child is null
                    highest=self.findMaxIter(currNode.left)
                    currNode.val=highest
                    num=highest
            ancestors.append(prev)
            prev=currNode
            if num>currNode.val:
                pMove=1
                currNode=currNode.right
            else:
                pMove=0
                currNode=currNode.left
        ancestors=ancestors[1:]
        firstTime=True
        while ancestors:
            parent=ancestors.pop()
            # firstTime was implemented to handle the double rebalance after deletion case
            # for example after inserting 2,1,4,3,5 delete 1 would result in a double rotation
            if firstTime:
                grandparent=parent
                firstTime=False
                if parent.left==None:
                    parent=grandparent.right
                else:
                    parent=grandparent.left
                if parent==None:
                    continue
            else:
                if len(ancestors)>0:
                    grandparent=ancestors[-1]
                else:
                    break
            #print(grandparent.val)
            if len(ancestors)>1:
                greatgrandparent=ancestors[-2]
            else:
                greatgrandparent=self.root
                
            if abs(self.BF(grandparent))>1:
                self.rebalanceIter(parent,grandparent,greatgrandparent)
            self.updateHeight(parent)
            self.updateHeight(grandparent)

    def printTreeIter(self):
        # Pre-order traversal for debugging and visualization
        stack=[self.root]
        while stack:
            currNode=stack.pop()
            if currNode!=None:
                print(currNode.val," h:",currNode.height, end=" | ")
                stack.extend([currNode.right,currNode.left])
        print("")

#----- Recursive BST -----
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

arr=getRandomArray(10000)

BSTTree=BST(arr[0])
for val in arr[1:]:
    BSTTree.insertRec(val)
print("BST Done")

AVLTree=AVL(arr[0])
for val in arr[1:]:
    AVLTree.insertIter(val)
print("AVL Done")




