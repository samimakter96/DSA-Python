# Brute Force Solution Using : Set
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


def inset_at_end(head, val):
    new_node = Node(val)

    if head is None:
        head = new_node
        return head

    temp = head
    while temp.next is not None:
        temp = temp.next

    temp.next = new_node
    return head


def create_cycle(head, pos):
    temp = head
    ptr = head
    count = 0

    while temp.next is not None:
        if count != pos:
            ptr = ptr.next
            count = count + 1
        temp = temp.next
    temp.next = ptr


def detect_cycle(head):
    st = set()

    while head is not None:
        if head in st:
            return head
        st.add(head)
        head = head.next
    return None


if __name__ == "__main__":
    head = None
    head = inset_at_end(head, 1)
    head = inset_at_end(head, 2)
    head = inset_at_end(head, 3)
    head = inset_at_end(head, 4)
    head = inset_at_end(head, 3)
    head = inset_at_end(head, 6)
    head = inset_at_end(head, 10)
    create_cycle(head, 2)
    node_recieve = detect_cycle(head)
    if node_recieve == None:
        print("No Cycle")
    else:
        temp = head
        pos = 0
        while temp != node_recieve:
            pos += 1
            temp = temp.next
        print("tail connect at position", pos)

# Time Complexity: O(N)  Space Complexity: O(N)
