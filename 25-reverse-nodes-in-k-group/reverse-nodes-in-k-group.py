# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        ptr = head
        while count< k and ptr:
            ptr = ptr.next
            count+=1
        if count == k:
            reversedHead = self.reverseLinkedList(head, k)
            head.next = self.reverseKGroup(ptr, k)
            return reversedHead
        return head

    def reverseLinkedList(self, head, k):
        prev, curr = None, head
        while k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            k-=1
        return prev