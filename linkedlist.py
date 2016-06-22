class linkedListNode:
      def __init__(self,val):
            self.val = val
            self.prev = None
            self.next = None
            
class linkedList:
      def __init__(self):
            self.start = None
      def insert(self,val):
            newNode = linkedListNode(val)
            tmpS = self.start
            self.start = newNode
            newNode.next = tmpS
            if(tmpS != None):
                  tmpS.prev = newNode
      def delete(self,val):
            current = self.start
            while current:
                  if(val == current.val):
                        if(current.prev != None):
                              current.prev.next = current.next
                              current.next.prev = current.prev
                        else:
                              self.start = current.next
                              current.next.prev = None
                        return print('deleted')
                  else:
                        return print('error(no_value)')
                  current = current.next

k = linkedList()
k.insert(7)
k.insert(9)
k.delete(9)
