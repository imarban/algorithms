__author__ = 'igomez'


class Heap(object):
    def __init__(self, data):
        self.data = data
        self.end = len(data) - 1
        self.heapify()

    def heapify(self):
        for i in xrange((self.end - 1) / 2, -1, -1):
            self.siftdown(i)

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    @staticmethod
    def parent(i):
        return (i - 1) / 2

    def is_empty(self):
        return self.end < 0

    def poll(self):
        if self.is_empty():
            raise IndexError

        max_val = self.data[0]
        self.data[0], self.data[self.end] = self.data[self.end], None
        self.end -= 1

        self.siftdown(0)

        return max_val

    def is_full(self):
        return self.end >= len(self.data)

    def insert(self, data):
        if self.is_full():
            raise OverflowError
        self.end += 1
        self.data[self.end] = data

        self.siftup(self.end)

    def siftup(self, i):
        parent = Heap.parent(i)
        child = i
        while parent >= 0:
            if self.data[parent] < self.data[child]:
                self.data[parent], self.data[child] = self.data[child], self.data[parent]

            child = parent
            parent = Heap.parent(child)

    def siftdown(self, i):
        l = Heap.left(i)
        r = Heap.right(i)

        if l <= self.end and self.data[l] > self.data[i]:
            largest = l
        else:
            largest = i

        if r <= self.end and self.data[r] > self.data[largest]:
            largest = r

        if largest != i:
            self.swap(i, largest)
            self.siftdown(largest)

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def sort(self):
        while self.end >= 0:
            self.data[0], self.data[self.end] = self.data[self.end], self.data[0]
            self.end -= 1
            self.heapify()

        return self.data

    @property
    def size(self):
        return self.end + 1


def heapsort(array):
    return Heap(array).sort()


if __name__ == '__main__':
    a = [5, 7, 15, 8, 2, 21, 11, 4, 3]
    h = Heap(a)

    h.poll()
    print h.data

    h.poll()
    print h.data

    h.poll()
    print h.data
