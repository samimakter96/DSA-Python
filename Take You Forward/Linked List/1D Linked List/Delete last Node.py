class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_tail(head):
    # Check if the linked list is empty or has only one node
    if head is None or head.next is None:
        return None

    # Create a temporary pointer for traversal
    temp = head

    # Traverse the list until the second-to-last node
    while temp.next.next is not None:
        temp = temp.next
    # Nullify the connection from the second-to-last node to delete the last node
    temp.next = None
    # Return the updated head of the linked list
    return head


def print_linked_list(head):
    current = head

    while current is not None:
        print(current.data, end="->")
        current = current.next
    print(None)


head = Node(2)
head.next = Node(4)
head.next.next = Node(7)
head.next.next.next = Node(6)

print("Original Linked List")
print_linked_list(head)

print("Linked List after deleting last")
delete_tail(head)
print_linked_list(head)
