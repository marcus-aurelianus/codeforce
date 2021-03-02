class Node:
     
    def __init__(self, x):
         
        self.data = x
        self.next = None
 
# Function for rearranging a linked 
# list with high and low value
def rearrange(head):
     
    if not head:
        # Quick response for empty linked list
        return None
    
    oriHead = head
    
    fast, slow = head, head
    
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        
    mid = slow
    
    # ------------------------------------------
    # Reverse second half
    
    prev, cur = None, mid
    
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    
    head_of_second_rev = prev
    
    # ------------------------------------------
    # Update link between first half and reversed second half
    
    first, second = head, head_of_second_rev
    
    while second.next:
        
        next_hop = first.next
        first.next = second
        first = next_hop
        
        next_hop = second.next
        second.next = first
        second = next_hop
    return oriHead
 
# Function to insert a node in the
# linked list at the beginning
def push(head, k):
     
    tem = Node(k)
    tem.data = k
    tem.next = head
    head = tem
    return head
 
# Function to display node of linked list
def display(head):
     
    curr = head
     
    while (curr != None):
        print(curr.data, end = " ")
        curr = curr.next
 
# Driver code
if __name__ == '__main__':
 
    head = None
 
    # Let create a linked list
    # 9 . 6 . 8 . 3 . 7
    head = push(head, 7)
    head = push(head, 3)
    head = push(head, 8)
    head = push(head, 6)
    head = push(head, 9)
 
    head = rearrange(head)
 
    display(head)
