class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # print Linked List
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "->"
            temp_node = temp_node.next
        return result

    # insert element at the end
    def append(self, value):
        new_node = Node(value)
        if self.head is None:   # if linked list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # insert element at the beginning
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # insert element at the mid
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:    # edge case
            return False
        if self.length == 0:        # edge case
            self.head = new_node
            self.tail = new_node
        elif index == 0:            # edge case
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.prepend(40)
new_linked_list.insert(1, 50)
print(new_linked_list)
new_linked_list.traverse()