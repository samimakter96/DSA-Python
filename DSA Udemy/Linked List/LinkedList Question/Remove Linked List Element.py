class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_element(head, val):

    dummy_head = Node(-1)
    dummy_head.next = head

    prev_head = dummy_head
    current_head = head

    while current_head is not None:
        if current_head.val == val:
            prev_head.next = current_head.next
        else:
            prev_head = current_head

        current_head = current_head.next


def print_linked_list(head):

    curr = head
    while curr is not None:
        print(curr.val, end="-->")
        curr = curr.next
    print(None)


head = Node(1)
head.next = Node(2)
head.next.next = Node(6)
head.next.next.next = Node(3)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(6)

print("Given Linked List")
print_linked_list(head)

print("Linked List after removing element")
remove_element(head, 6)

print_linked_list(head)
