class LNode:
    def __init__(self, elm, next_=None):
        self.elem = elm
        self.next = next_

llist1 = LNode(1)
pnode = llist1
for i in range(2, 11):
    pnode.next = LNode(i)
    pnode = pnode.next

pnode = llist1
count = 1

y = int(input())
x = input()

while pnode:
    pnode = pnode.next
    count += 1
    if count == y:
        pnode.elem = x

pnode = llist1

while pnode:
    print(pnode.elem, end=" ")
    pnode = pnode.next