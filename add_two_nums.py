# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = str(self.val)
        n = self.next
        while n:
            s += ", " + str(n.val)
            n = n.next
        return s

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        res = ListNode()
        n = res
        t1, t2, carry_over = l1, l2, 0
        while t1 or t2 or carry_over:
            t1_v = t1.val if t1 else 0
            t2_v = t2.val if t2 else 0
            t_sum = t1_v + t2_v + carry_over
            if carry_over > 0:
                carry_over = 0
            if t_sum > 9:
                t_sum = t_sum - 10
                carry_over = 1
            n.val = t_sum
            t1 = t1.next if t1 else None
            t2 = t2.next if t2 else None
            if t1 or t2 or carry_over:
                n.next = ListNode()
                n = n.next
        return res


def build_ll(l: list[int]) -> ListNode:
    top = ListNode(l[0])
    n = top
    if len(l) > 1:
        for i in range(1, len(l)):
            n.next = ListNode(l[i])
            n = n.next
    return top

s = Solution()
# print(s.addTwoNumbers(
#     build_ll([2,4,3]),
#     build_ll([5,6,4]),
# ))
print(s.addTwoNumbers(
    build_ll([9,9,9,9,9,9,9]),
    build_ll([9,9,9,9]),
))
print(s.addTwoNumbers(
    build_ll([0]),
    build_ll([0]),
))