# Brute Force Approach:

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        first_set = set()
        curr = headA

        while curr:
            first_set.add(curr)
            curr = curr.next

        curr = headB
        while curr:
            if curr in first_set:
                return curr
            curr = curr.next

        return None


# Time Complexity: O(n + m)     Space Complexity: O(n)

# Optimal Approach:

# one = headA
# two = headB
#
# while one != two:
#     one = one.next if one else headB
#     two = two.next if two else headA
# return one

# Time Complexity: O(n + m)   Space Complexity: O(1)

