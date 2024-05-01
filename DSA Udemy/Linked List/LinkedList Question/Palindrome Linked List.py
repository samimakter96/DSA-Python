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


def is_palindrome(head):

    # step-1: find middle
    slow = head
    first = head

    while first is not None and first.next is not None:
        slow = slow.next
        first = first.next.next

    # step-2: reverse second half of the linked list
    prev = None
    while slow is not None:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    # step-3: chck palindrome of not
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

print(is_palindrome(head))