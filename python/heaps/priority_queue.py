from heaps.heap import Heap

__author__ = 'igomez'


class PriorityQueue(object):
    def __init__(self, data):
        self.heap = Heap(data)

    # TODO Do this in an efficient way
    def poll(self):
        self.heap.data[0], self.heap.data[self.heap.end] = self.heap.data[self.heap.end], self.heap.data[0]
        self.heap.end -= 1

        self.heap.heapify()

        return self.heap.data[self.heap.end + 1] if self.heap.end > -2 else None

    @property
    def size(self):
        return self.heap.end


if __name__ == '__main__':
    a = [5, 7, 15, 8, 2, 21, 11, 4, 3]
    pq = PriorityQueue(a)
