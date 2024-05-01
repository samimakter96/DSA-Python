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
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "-->"
            temp_node = temp_node.next
        return result

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

    def remove(self, index):
        # Check if the index is out of bounds
        if index < 0 or index >= self.length:
            return None

        # Case: Removing the head node
        if index == 0:
            popped_node = self.head

            # Adjust head and tail if there's only one node
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

            popped_node.next = None
            self.length -= 1
            return popped_node

        # Case: Removing a node in the middle or at the tail
        else:
            temp = self.head

            # Traverse to the node before the one to be removed
            for _ in range(index - 1):
                temp = temp.next

            popped_node = temp.next

            # Update tail if the node to be removed is the tail
            if popped_node.next is None:
                self.tail = temp

            # Adjust pointers to skip the node to be removed
            temp.next = temp.next.next
            popped_node.next = None
            self.length -= 1
            return popped_node


new_linked_list = LinkedList()
new_linked_list.inset_at_end(10)
new_linked_list.inset_at_end(20)
new_linked_list.inset_at_end(30)
new_linked_list.inset_at_end(40)
new_linked_list.inset_at_end(50)
print(new_linked_list)
new_linked_list.remove(0)
print(new_linked_list)
new_linked_list.remove(2)
print(new_linked_list)