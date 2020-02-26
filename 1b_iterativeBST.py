#rename all methods with Iter at the end
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None 
        self.right=None 

class BST:
    def __init__(self,val):
        self.root=Node(val)

    def insertIter(self,num):
        if self.root==None:
            self.root=Node(num)
        else:
            currNode=self.root
            while currNode:
                if currNode.val<num:
                    if currNode.right==None:
                        currNode.right=Node(num)
                        break
                    else:
                        currNode=currNode.right
                else:
                    if currNode.left==None:
                        currNode.left=Node(num)
                        break
                    else:
                        currNode=currNode.left
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
            
            prev=currNode
            if num>currNode.val:
                pMove=1
                currNode=currNode.right
            else:
                pMove=0
                currNode=currNode.left
            

    def printTreeIter(self):
        # Pre-order traversal for debugging and visualization
        stack=[self.root]
        while stack:
            currNode=stack.pop()
            if currNode!=None:
                print(currNode.val, end=" ")
                stack.extend([currNode.right,currNode.left])
        print("")




tree=BST(20)
tree.insertIter(5)
tree.insertIter(25)
tree.insertIter(4)
tree.insertIter(6)
tree.insertIter(30)
tree.insertIter(21)
print(tree.findMinIter())
print(tree.findMaxIter())
x=21
print("next smallest after %d" %(x))
print(tree.findPrevIter(x))

tree.printTreeIter()
tree.deleteIter(20)
tree.printTreeIter()