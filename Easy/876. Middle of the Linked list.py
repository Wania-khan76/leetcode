# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution(object):
    #  def middleNode(self, head) :
    #     slow = head
    #     fast = head

    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next

    #     return slow

    def gett(self,head,target):
        traverse=head
        while traverse:
            if traverse.val==target:
                return traverse
            traverse = traverse.next
        return None
    def lengthL(self,head):
        leng=0
        a=head
        while a:
            leng+=1
            a=a.next
        return leng
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """ 
        totalleng = self.lengthL(head)
        mid = totalleng // 2
        traverse = head
        for i in range(mid):
            traverse = traverse.next
        return traverse
        

   
