class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print(None)

    def insert_at_beginning(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


new_linked_list = LinkedList()
new_linked_list.insert_at_beginning(10)
new_linked_list.insert_at_beginning(20)
new_linked_list.insert_at_beginning(30)
new_linked_list.print_linked_list()
new_linked_list.reverse()
new_linked_list.print_linked_list()