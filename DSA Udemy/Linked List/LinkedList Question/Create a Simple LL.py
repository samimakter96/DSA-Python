class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = self.head
        self.length = 1


new_linked_list = LinkedList(10)
print(new_linked_list.head.value)
print(new_linked_list.tail.value)
print(new_linked_list.length)



