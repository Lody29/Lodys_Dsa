class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
def list_adder(self,L1,L2,carry):
    dummy = ListNode(0)
    current = dummy
    carry = 0
    while L1 or L2 or carry:
        val1 = L1.val if L1 else 0 
        val2 = L2.val if L2 else 0 

        total = val1 + val2 + carry
        carry = total // 10

        current.next = ListNode(total%10)

        current = current.next

        if L1: L1 = L1.next
        if L2: L2 = L2.next
    return dummy.next