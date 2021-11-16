class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None


    def prepend(self,value):
        if self.head == None:
            self.head = Node(value)
            return
        node = self.head
        self.head = Node(value)
        self.head.next = node
    def append(self,value):
        if self.head == None:
            self.head = Node(value)
            return None
        tail = self.head
        # moving to last tail
        while tail.next:
            tail = tail.next
        tail.next = Node(value)

    def to_list(self):
        list_values = []
        head = self.head
        while head:
            list_values.append(head.value)
            head = head.next
        return list_values

    def search(self,value):
        """
        searching for a value in linkedlist
        with time complexity of O(n)

        :param value:
        :return node:
        """
        head = self.head
        while head.next:
            if head.value == value:
                return head
            head = head.next

ll = LinkedList()
ll.prepend(10)
ll.prepend(20)
ll.prepend(30)
ll.append(40)
ll.append(50)
print(ll.to_list())
print(ll.search(40))