# Definition for singly-linked list given by Leetcode itself
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()      # placeholder of head
        current = dummy             
        carry = 0               #initialize carry to 0 as there is no carry at the start

        while l1 or l2 or carry: #instead of for loop we used while because test cases specified UnEven lengths of l1,l2 and this logic can also handle leftover carry at the end.
            total = carry       #total equals to carry will handle leftover carry when no l1 and l2 element exists.    
            if l1:              #if l1 element exists
                total += l1.val #assign total (also has carry value if exists) equals to l1 current value.
                l1 = l1.next    # update l1 pointer to next node
            if l2:
                total += l2.val #same goes to l2 just like l1
                l2 = l2.next

            carry = total // 10 #floor division by 10 to get the quotient without float value and this gives us carry only when total is greater than 10
            current.next = ListNode(total % 10) #modulo of total with 10 which gives remainder. (this is the value filled inside node)
            current = current.next #update the cur pointer to next node
            
            #this loop runs until all elements in l1 and l2, along with leftover carry are added to current linked list


        return dummy.next  #return the linked list as output
    
    