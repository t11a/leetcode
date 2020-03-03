class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head

        p1 = head
        p2 = p1.next

        head.next = None
        while p2 is not None:
            t = p2.next
            p2.next = p1
            p1 = p2
            p2 = t

        return p1