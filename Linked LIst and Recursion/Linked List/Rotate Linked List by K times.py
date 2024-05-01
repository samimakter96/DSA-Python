class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def rotate_linked_list(head, k):
    if not head or k <= 0:
        return head

    # Find the length of the linked list
    current = head
    length = 1
    while current.next is not None:
        current = current.next
        length += 1

    # Adjust k to be within the length of the list
    k = k % length

    if k == 0:
        return head  # No rotation needed

    # Connect the last node to the head
    current.next = head

    # Move to the new head position
    for _ in range(length - k):
        current = current.next

    # Set the new head and disconnect the rotated part
    new_head = current.next
    current.next = None

    return new_head


def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end="->")
        temp = temp.next
    print(None)


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Given List")
print_linked_list(head)

print("Rotate Linked List")
rotated_head = rotate_linked_list(head, 2)
print_linked_list(rotated_head)

