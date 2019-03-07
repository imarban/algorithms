from heaps.heap import Heap

__author__ = 'igomez'


class MinHeap(Heap):
    def __init__(self, data):
        self.data = data
        self.start = 0
        self.heapify()

    def heapify(self):
        for i in xrange((len(self.data) - 1) / 2, self.start, -1):
            self.siftdown(i)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def is_empty(self):
        return self.start >= len(self.data)

    def poll(self):
        if self.is_empty():
            raise IndexError

        max_val = self.data[0]
        self.start += 1
        self.heapify()

        return max_val

    def is_full(self):
        return self.start >= 0

    def insert(self, data):
        if self.is_full():
            raise OverflowError
        self.data[self.end] = data
        self.heapify()

    def siftdown(self, i):
        l = self.left(i)
        r = self.right(i)

        if l < len(self.data) and self.data[l] < self.data[i]:
            smallest = l
        else:
            smallest = i

        if r < len(self.data) and self.data[r] < self.data[smallest]:
            smallest = r

        if smallest != i:
            self.swap(i, smallest)
            self.siftdown(smallest)

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def sort(self):
        while self.start > len(self.data):
            self.start += 1
            self.heapify()

        return self.data

    @property
    def size(self):
        return self.start


if __name__ == '__main__':
    a = [5, 7, 15, 8, 2, 21, 11, 4, 3]
    h = MinHeap(a)
    print h.data

    print h.sort()
