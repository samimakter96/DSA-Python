class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Print the linked list in the format: value1->value2->value3->...
    def print_linked_list(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "->"
            temp_node = temp_node.next
        return result

    # Insert a node with the given value at the end of the linked list
    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # Insert a node with the given value at the beginning of the linked list
    def insert_at_beginning(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # Insert a node with the given value at the specified index
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True

    # Traverse and print the values of the linked list
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    # Search for a target value in the linked list and return its index
    def search(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1

    # Get the node at the specified index
    def get(self, index):
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    # Update the value of the node at the specified index
    def update_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    # Remove and return the first node in the linked list
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
        return popped_node

    # Remove and return the last node in the linked list
    def pop_end(self):
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
        self.length -= 1
        return popped_node

    # Remove and return the node at the specified index
    def remove(self, index):
        if index >= self.length or index < -1:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1 or index == -1:
            return self.pop_end()
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    # Delete all nodes in the linked list
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0


# Example usage:

# Create a new linked list
new_linked_list = LinkedList()

# Insert nodes with values 10, 20, and 30 at the end of the linked list
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(20)
new_linked_list.insert_at_end(30)

# Insert a node with the value 5 at the beginning of the linked list
new_linked_list.insert_at_beginning(5)

# Insert a node with the value 50 at index 1
new_linked_list.insert(1, 50)

# Print the linked list: 5->50->10->20->30
print(new_linked_list.print_linked_list())

# Traverse and print the values of the linked list
new_linked_list.traverse()

# Search for the value 30 in the linked list and print its index
print(new_linked_list.search(30))

# Get the node at index 2 and print its value
print(new_linked_list.get(2))

# Update the value of the node at index 1 to 100
print(new_linked_list.update_value(1, 100))

# Print the linked list after the update: 5->100->10->20->30
print(new_linked_list.print_linked_list())

# Remove and print the first node in the linked list
new_linked_list.pop_first()
print(new_linked_list.print_linked_list())

# Remove and print the last node in the linked list
new_linked_list.pop_end()
print(new_linked_list.print_linked_list())

# Remove and print the node at index -1 (last node) in the linked list
new_linked_list.remove(-1)
print(new_linked_list.print_linked_list())
