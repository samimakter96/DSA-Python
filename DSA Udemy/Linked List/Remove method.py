class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True

    def pop_first(self):    # pop first method remove first element of the linked list
        if self.length == 0:    # edge case
            return None
        popped_node = self.head
        if self.length == 1:    # edge case
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
            self.length -= 1
        return popped_node

    def pop(self):   # pop method remove the last element of the linked list
        if self.length == 0:    # edge case
            return None
        popped_node = self.tail
        if self.length == 1:    # edge case
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node

    def get(self, index):   # get method get the value
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def remove(self, index):
        if index >= self.length or index < -1:    # edge case
            return None
        if index == 0:  # edge case
            return self.pop_first()
        if index == self.length-1 or index == -1:   # edge case
            return self.pop()
        else:
            prev_node = self.head
            for _ in range(index - 1):
                prev_node = prev_node.next
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
        self.length -= 1
        return popped_node

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0


new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.prepend(40)
new_linked_list.insert(1, 50)
print(new_linked_list)
print(new_linked_list.remove(-1))
print(new_linked_list)
print(new_linked_list.tail.value)
print(new_linked_list.delete_all())
print(new_linked_list)