from heapq import heappush, heappop
from heaps.heap import Heap


class Node(object):
    def __init__(self, data):
        self.next = None
        self.data = data

    def __str__(self):
        return str(self.data)

    def __cmp__(self, other):
        return cmp(self.data, other.data)


# This function assumes that lists is an iterable
def merge_k(lists):
    # If lists is empty
    if not len(lists):
        return

    # Initializing an array containing the first element of each list
    data = [lst for lst in lists]

    # Initializing a heap with the data
    heap = Heap(data)

    # Extracting min and storing reference to the head
    result = heap.poll()
    head = result

    if result.next:
        heap.insert(result.next)

    # Extracting min and replacing with next one from list
    while not heap.is_empty():
        min_item = heap.poll()
        result.next = min_item
        result = result.next

        if min_item.next:
            heap.insert(min_item.next)

    return head


if __name__ == '__main__':
    l1 = Node(1)
    l1.next = Node(4)
    l1.next.next = Node(7)
    l1.next.next.next = Node(10)
    l1.next.next.next.next = Node(13)

    l2 = Node(2)
    l2.next = Node(5)
    l2.next.next = Node(8)
    l2.next.next.next = Node(11)
    l2.next.next.next.next = Node(14)

    h = merge_k([l1, l2])

    while h:
        print h.data
        h = h.next
