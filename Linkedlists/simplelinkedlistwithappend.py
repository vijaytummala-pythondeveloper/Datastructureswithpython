class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,value):
        if self.head == None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
    def convert_to_list(self):
        res = []
        node = self.head
        while node:
            res.append(node.value)
            node = node.next
        return res


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print(ll.convert_to_list())