class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def find_middle(self):
        if self.head is None:
            return None

        slow = self.head
        first = self.head

        while first is not None and first.next is not None:
            slow = slow.next
            first = first.next.next

        return slow

    def print_linked_list(self):
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print(None)


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Given List")

new_linked_list = LinkedList()
new_linked_list.head = head
new_linked_list.print_linked_list()

middle_element = new_linked_list.find_middle()
print(middle_element)

