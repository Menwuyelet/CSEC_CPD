# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# a = Node(1)
# b = Node(2)
# c = Node(3)
# a.next = b
# b.next = c

# head = a
# while  head != None:
#     print(head.value)
#     head = head.next
# print()
# A = Node(5)
# a.next = A
# A.next = b
# head = a
# Z = Node(0)
# head = Z
# Z.next = a
# while  head != None:
#     print(head.value)
#     head = head.next



# class Node:
#     def __init__(self, value):
#         self.val = value
#         self.next = None

# class MyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.dummy = Node(0)
#         self.dummy.next = self.head
#         self.length = 0

#     def get(self, index: int) -> int:
#         if index >= self.length:
#             return -1
#         temp = self.head
#         for i in range(index-1):
#             temp = temp.next
#         return temp.val
    
#     def addAtHead(self, val: int) -> None:
#         node = Node(val)
#         node.next = self.dummy.next
#         self.dummy = node
#         self.head = node
#         self.length +=1

#     def addAtTail(self, val: int) -> None:
#         temp = self.head
#         while temp.next != None:
#             temp = temp.next
#         temp.next = Node(val)

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index > self.length:
#             return -1
#         temp = self.head
#         for i in range(index):
#             temp = temp.next
#         var = Node(val)
#         var.next = temp.next
#         temp.next = var

#     def deleteAtIndex(self, index: int) -> None:
#         if index > self.length:
#             return -1
#         temp = self.head
#         for i in range(index-2):
#             temp = temp.next
#         var = temp.next.next
#         temp.next = var

# index = 1
# val = 2

# obj = MyLinkedList()
# param_1 = obj.get(index)
# print(param_1)
# print(obj.addAtHead(val))

# print(obj.addAtTail(val))

# print(obj.addAtIndex(index,val))
# print(obj.deleteAtIndex(index))



a = [0, 1, 3, 4, 5, 6, 7, 8, 9, 20, 22, 23, 44, 56, 100]
n=len(a)
k = 20
a.append(k)
i = 0
while a[i] < k:
    i +=1
if a[i] > k or i >= n:
    print(-1)
else:
    print(i)