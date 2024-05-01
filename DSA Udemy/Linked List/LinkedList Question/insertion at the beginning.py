class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1


new_linked_list = LinkedList()
new_linked_list.insert_at_beginning(10)
new_linked_list.insert_at_beginning(5)
new_linked_list.insert_at_beginning(100)
print(new_linked_list.head.value)
print(new_linked_list.length)