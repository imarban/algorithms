__author__ = 'igomez'


class Node(object):
    def __init__(self, data):
        self.next = None
        self.data = data

    def __str__(self):
        return str(self.data)

    def __cmp__(self, other):
        return cmp(self.data, other.data)


class LinkedList(object):
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def insert(self, x):
        if not self.first:
            self.first = Node(x)
            self.last = self.first
            # self.first.next = self.last
        else:
            self.last.next = Node(x)
            self.last = self.last.next

        self.size += 1

    def search(self, x):
        current = self.first
        while current:
            if current.data == x:
                return current
            current = current.next

        return None

    def remove(self, x):
        previous = None
        current = self.first

        while current.data != x and current.next:
            previous = current
            current = current.next

        if current.data == x:
            self.size -= 1
            if previous:
                previous.next = current.next
            else:
                self.first = current.next

            if not current.next:
                self.last = previous

    def remove_duplicates(self):
        current = self.first
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                    self.size -= 1
                else:
                    runner = runner.next
            current = current.next

    def find_kth_latest(self, x):
        if x >= self.size or x < 0:
            return None
        slow = self.first
        fast = slow

        for i in xrange(x):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        return slow.data

    def delete_node(self, node):
        current = self.first

        if self.first == node:
            self.first = current.next
            self.size -= 1
            return

        while current.next:
            if current.next == node:
                self.size -= 1
                current.next = current.next.next
                break

            current = current.next

        self.last = current

    def delete_node_at_middle(self, node):
        next_node = node.next

        if next_node:
            node.data = next_node.data
            node.next = next_node.next

    def partition(self, x):

        first = LinkedList()
        second = LinkedList()

        pointer = self.first

        while pointer:
            if pointer.data < x:
                first.insert(pointer.data)
            else:
                second.insert(pointer.data)

            pointer = pointer.next

        first.last.next = second.first
        return first if first.last else second

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.first
        while current:
            yield current
            current = current.next

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.data) + ', '
            while current.next is not None:
                current = current.next
                out += str(current.data) + ', '
            return out + ']'
        return 'LinkedList []'

    def __add__(self, other):
        pointer_self = self.first
        pointer_other = other.first

        result = LinkedList()

        carry = 0

        while pointer_self or pointer_other:
            partial = carry
            if pointer_other:
                partial += pointer_other.data
            if pointer_self:
                partial += pointer_self.data

            carry = partial / 10
            result.insert(partial % 10)

            pointer_self = pointer_self.next if pointer_self else pointer_self
            pointer_other = pointer_other.next if pointer_other else pointer_other

        return result
