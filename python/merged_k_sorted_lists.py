# https://www.geeksforgeeks.org/merge-k-sorted-linked-lists/

from heapq import heappush, heappop

class Node(object):
    def __init__(self, data):
        self.next = None
        self.data = data

    def __str__(self):
        return str(self.data)

    def __cmp__(self, other):
        return cmp(self.data, other.data)

#This function assumes that lists is an iterable
def merge_k(lists):
    # If lists is empty
    if not len(lists):
        return

    # Initializing an array that is going to work as a min-heap
    pq = [lst for lst in lists]

    # Extracting min and storing reference to the head
    result = heappop(pq)
    head = result

    if result.next:
        heappush(pq, result.next)

    # Extracting min and replacing with next one from list
    while pq:
        min_item = heappop(pq)
        result.next = min_item
        result = result.next

        if min_item.next:
            heappush(pq, min_item.next)

    return head