class DoubleNode:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,value):
        if self.head == None:
           self.head = DoubleNode(value)
           self.tail = self.head
           return
        self.tail.next = DoubleNode(value)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
# print in forward
headnode = dll.head
while headnode:
    print(headnode.value)
    headnode = headnode.next
print("**************************")
# print in reverse
tailnode = dll.tail
while tailnode:
    print(tailnode.value)
    tailnode = tailnode.prev
