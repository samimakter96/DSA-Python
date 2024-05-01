class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_linked_list(head):
    temp_node = head
    while temp_node is not None:
        print(temp_node.val, end="-->")
        temp_node = temp_node.next
    print(None)


def check_palindrome(head):

    slow = head
    first = head

    while first is not None and first.next is not None:
        slow = slow.next
        first = first.next.next

    prev = None
    while slow is not None:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    while prev is not None:
        if head.val != prev.val:
            return False
        head = head.next
        prev = prev.next
    return True


head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)

print("Given Linked List")
print_linked_list(head)

print(check_palindrome(head))
