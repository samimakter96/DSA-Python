class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def inset_at_end(self, value):
        new_node = Node(value)
        # check if the linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


new_linked_list = LinkedList()
new_linked_list.inset_at_end(10)
new_linked_list.inset_at_end(20)
print(new_linked_list.tail.value)
new_linked_list.inset_at_end(30)
print(new_linked_list.head.value)
print(new_linked_list.tail.value)