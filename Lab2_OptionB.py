class Node(object):

    def __init__(self, item, next=None, count=1):
        self.item = item
        self.next = next
        self.count = count

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def prints(self):
        print("password:", self.item.replace("\n", ""), "\nduplicates:", self.count, "\n")


class LinkedList(object):
    def __init__(self, head=None, next=None):
        self.head = head
        self.next = next

    def add(self, item):
        self.head = Node(item, self.head)

    def search(self, x):
        if self.head is None:
            return False
        curr = self.head
        while curr is not None:
            if curr.item == x:
                curr.count += 1
                return True
            else:
                curr = curr.next
        return False

    def print(self):
        temp = self.head
        while temp is not None:
            temp.prints()
            temp = temp.next


    def size(self):
        counts = 0
        temp = self.head
        while temp is not None:
            counts = counts + 1
            temp = temp.next
        return counts




# Bubble Sort
    def bubble_sort(self):
        end = None
        while end != self.head:
            start = self.head
            while start.next != end:
                pointer = start.next
                if start.count < pointer.count:
                    start.item, pointer.item = pointer.item, start.item
                    start.count, pointer.count = pointer.count, start.count
                start = start.next
            end = start


# Solution A
LL = LinkedList()
Left = LinkedList()
Right = LinkedList()

text = open("test3.txt", "r")
read = text.readlines()
for line in read:
    password = line.split("	")
    if (LL.search(password[-1])) == False:
        LL.add(password[-1])
LL.print()

# Solution B
dict = {}
texts = open("test.txt", "r")
reads = texts.readlines()
for lines in reads:
    password = lines.split("	")
    if password[-1] in dict:
        dict[password[-1]] = dict[password[-1]] + 1
    else:
        dict[password[-1]] = 1

for num in dict:
    print(dict[num])
print("\n")


# Merge sort didn't work
# def merge_sort(A):
#     if A == None or A.next == None:
#         return A
#     left_half, right_half = split(A)
#     lefty = merging(left_half)
#     righty = merging(right_half)
#     return merging(lefty, righty)
#
# def split(A):
#     if A == None or A.next == None:
#         left_half = A
#         right_half = None
#         return left_half, right_half
#     else:
#         mid = A
#         t = A.next
#         while t is not None:
#             t = t.next
#             mid = mid.next
#         left = A
#         right = A.next
#         mid.next = None
#         return left, right
#
# def merging(left, right):
#     result = Node("", -1, None)
#     curr = result
#     while left and right:
#         if left.count > right.count:
#             curr.next = left
#         else:
#             curr.next = right
#     if left is None:
#         curr.next = right
#     if right is None:
#         curr.next = left
#         return result.next


LL.size()
LL.bubble_sort()
LL.print()
# merge_sort(LL)
# LL.print()