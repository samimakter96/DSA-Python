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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def reverse(self):
        # Initialize variables
        prev_node = None  # Previous node initially set to None
        current_node = self.head  # Start from the head of the linked list

        # Traverse the linked list
        while current_node is not None:
            next_node = current_node.next  # Store the next node before modifying the link
            current_node.next = prev_node  # Reverse the link: make current node point to the previous node
            prev_node = current_node  # Update previous node to the current node
            current_node = next_node  # Move to the next node in the original order

        # Update head and tail pointers after the reversal
        self.head, self.tail = self.tail, self.head


new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
print(new_linked_list)
new_linked_list.reverse()
print(new_linked_list)