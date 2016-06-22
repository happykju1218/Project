class binarySearchPointerTreeNode:
      def __init__(self,point,val):
            self.val = val
            self.point = point
            self.left = None
            self.right = None
            self.parant = None # if parant is none => root node.

class binarySearchPointerTree:
      def __init__(self):
            self.root = None

      def insert(self, point, val):
            newNode = binarySearchPointerTreeNode(point,val)
            if (self.root == None):
                  self.root = newNode
                  return print('complete')
            else:
                  tmp1 = self.root
                  tmp2 = None
                  tmp3 = True
                  while tmp1:
                        tmp2 = tmp1
                        if (tmp1.val < newNode.val):
                              tmp1 = tmp1.right
                        elif(tmp1.val > newNode.val):
                              tmp1 = tmp1.left
                              tmp3 = False
                        else:
                              return print('error(has same value)')
                  if (tmp3):
                        tmp2.right = newNode
                        newNode.parant = tmp2
                        return print('complete')
                  else:
                        tmp2.left = newNode
                        newNode.parant = tmp2
                        return print('complete')
                  return print('error')

      def search(self,val):
            tmp = self.root
            while tmp:
                  if (tmp.val < val):
                        tmp = tmp.right
                  elif(tmp.val > val):
                        tmp = tmp.left
                  else:
                        return tmp
            return None
            
      def delete(self,val):
            tmp = self.search(val)
            if (tmp != None):
                  if(tmp.left == None):
                        self.transplant(tmp,tmp.right)
                        print('complete')
                  elif (tmp.right == None):
                        self.transplant(tmp,tmp.left)
                        print('complete')
                  else:
                        tmpS = tmp.right
                        while tmpS.left:
                              tmpS = tmpS.left
                        if (tmpS.parant != tmp):
                              self.transplant(tmpS,tmpS.right)
                              tmpS.right = tmp.right
                              tmpS.right.parant = tmpS
                        self.transplant(tmp,tmpS)
                        tmpS.left = tmp.left
                        tmpS.left.parnat = tmpS
                        print('complete')
                        
            else:
                  return print('error(no such value)')

      def transplant(self,f,g):
            if (f.parant == None):
                  self.root = g
            elif (f == f.parant.left):
                  f.parant.left = g
            else:
                  f.parant.right = g
            if(g != None):
                  g.parant = f.parant
      
k = binarySearchPointerTree()
k.insert(4,4)
k.insert(7,7)
k.insert(6,6)
k.insert(8,8)
k.insert(13,13)
k.insert(1,1)
k.insert(2,2)
k.delete(7)
k.delete(10)
k.delete(13)
k.delete(4)
