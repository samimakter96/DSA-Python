class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.val, end="->")
        temp = temp.next
    print(None)


def reverse(head):
    prev_node = None
    curr_node = head

    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    # Update the head to the last node, which is now the first node after reversal
    head = prev_node
    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(5)
head.next.next.next = Node(7)
head.next.next.next.next = Node(6)

print("Given Linked List")
print_linked_list(head)

# Update the head after reversing
head = reverse(head)

print("Linked list after reverse")
print_linked_list(head)
