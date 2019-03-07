# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or type(head) is not ListNode:
            return head

        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


l = ListNode(1)
l1 = ListNode(2)
l2 = ListNode(3)
l3 = ListNode(4)

l.next = l1
# l2.next = l3

ans = Solution().reverseList(l)
while ans:
    print str(ans.val) + "->",
    ans = ans.next
