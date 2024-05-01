class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_linked_list(self):
        curr = self.head
        while curr is not None:
            print(curr.value, end="-->")
            curr = curr.next
        print(None)

    def inset_at_beginning(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def inset_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        prev_node = self.head
        for _ in range(index - 1):
            prev_node = prev_node.next
        new_node.next = prev_node.next
        prev_node.next = new_node

    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1

    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        return popped_node

    def remove(self, index):
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        popped_node = temp.next
        temp.next = popped_node.next
        popped_node.next = None

    def find_middle(self):
        if self.head is None:
            return None

        slow = self.head
        first = self.head

        while first is not None  and first.next is not None:
            slow = slow.next
            first = first.next.next

        return slow


new_linked_list = LinkedList()
new_linked_list.inset_at_beginning(10)
new_linked_list.inset_at_beginning(30)
new_linked_list.inset_at_end(20)
new_linked_list.inset_at_end(40)
new_linked_list.insert(1, 50)
new_linked_list.insert(2, 100)
# new_linked_list.pop_first()
# new_linked_list.pop_first()
# new_linked_list.pop()
# new_linked_list.remove(1)
new_linked_list.print_linked_list()

# middle = new_linked_list.find_middle();
# print(middle.value)
