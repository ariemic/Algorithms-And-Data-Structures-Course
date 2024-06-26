class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
#end class


def put_guardian(p):
    q = Node(None)
    q.next = p 
    return q 
#end def


def print_all(p):
    while p is not None:
        print(p.val, end = " ")
        p = p.next
#end def


def create_linked_list_with_given_elements(L):
  g = Node(None)
  p = g

  for elem in L:
    p.next = Node(elem)
    p = p.next
  
  return g.next
#end def


# Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę elementów w cyklu

def cycle(p):

    if p is None:
        return False

    counter = 0 
    fast = p
    slow = p
    
    while 1:

        fast = fast.next.next
        slow = slow.next

        if fast == slow: break

    #end while

    fast = fast.next.next
    slow = slow.next
    counter += 1 

    while fast != slow:
        counter += 1
        fast = fast.next.next
        slow = slow.next 
    #end while

    return counter 
#end def



x = Node(1)
p = Node(2)
x.next = p
a = Node(3)
p.next = a
b = Node(4)
a.next = b
c = Node(5)
b.next = c
d = Node(6)
c.next = d
d.next = b




print( cycle(x) ) 

