class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        if self.head == None:
            self.head = Node(value)
            return
        node = self.head
        self.head = Node(value)
        self.head.next = node

    def append(self, value):
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

    def search(self, value):
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

    def remove(self, value):
        """
        removes node with matched value
        """
        head_node = self.head
        prev_node = None

        while head_node:
            if head_node.value == value:
                if prev_node == None:
                    self.head = head_node.next
                    return
                prev_node.next = head_node.next
                return
            prev_node = head_node
            head_node = prev_node.next

    def pop_first(self):
        head = self.head
        self.head = self.head.next
        return head.value

    def __len__(self):
        count = 0
        head = self.head
        while head:
            count = count + 1
            head = head.next
        return count

    def insert(self, val, pos):
        head = self.head
        prev_node = None
        next_node = None
        linked_list_len = self.__len__()
        if linked_list_len - 1 < pos:
            while head.next:
                head = head.next
            head.next = Node(val)
            return
        if pos == 0:
            next_node = self.head
            self.head = Node(val)
            self.head.next = next_node
            return
        i = 1
        while i <= pos:
            prev_node = head
            head = prev_node.next
            next_node = head.next
            i = i + 1
        prev_node.next = Node(val)
        prev_node.next.next = head
        return


