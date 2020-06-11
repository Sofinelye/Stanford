'''
The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 3
lecture on heap applications). The text file contains a list of the integers from 1 to 10000 in
unsorted order; you should treat this as a stream of numbers, arriving one by one.
Compute the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). That is, you
should compute (m1 + m2 + ... + m10000) mod 10000, where constants next to m represent the ith
order statistic in the set of 10000 medians.
Also, compare the performance achieved by heap-based and search-tree-based implementations of the
algorithm.
'''
import time


# Heap class
# input: order is 0 for max heap, 1 for min heap
class Heap():
    def __init__(self, order=1):
        self._heap = []
        self._min_heap = order

    def __str__(self):
        output = '['
        size = len(self._heap)
        for i, v in enumerate(self._heap):
            txt = ', ' if i is not size - 1 else ''
            output += str(v) + txt
        return output + ']'

    # input: parent and child nodes
    def _is_balanced(self, p, c):
        is_min_heap = p <= c
        return is_min_heap if self._min_heap else not is_min_heap

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    # input: parent and child indices
    def _sift_up(self, p_i, c_i):
        if p_i == -1:
            return
        p = self._heap[p_i]
        c = self._heap[c_i]
        while (not self._is_balanced(p, c)):
            p_i = (c_i - 1) // 2
            self._swap(c_i, p_i)

            c_i = p_i
            if c_i is 0:
                break
            p = self._heap[(c_i - 1) // 2]

    # input: parent and child indices
    def _sift_down(self, p_i, c_i):
        while (c_i and not self._is_balanced(self._heap[p_i], self._heap[c_i])):
            self._swap(p_i, c_i)
            p_i = c_i
            c_i = self._get_swapped_child_index(p_i)

    def get_root(self):
        if self._heap:
            return self._heap[0]

    def get_nodes(self):
        return self._heap

    # inserts node in O(logn) time
    def insert(self, node):
        self._heap.append(node)
        node_i = len(self._heap) - 1
        self._sift_up((node_i - 1) // 2, node_i)

    # input: parent index
    # output: index of smaller or greater child, one index if other DNE, or None
    def _get_swapped_child_index(self, p_i):
        size = len(self._heap)
        i = p_i * 2 + 1
        j = p_i * 2 + 2
        if size <= i:
            return None
        elif size <= j:
            return i

        if self._heap[i] > self._heap[j]:
            return j if self._min_heap else i
        else:
            return i if self._min_heap else j

    def _extract_root(self):
        if self._heap:
            self._swap(0, len(self._heap) - 1)
            root = self._heap.pop()
            self._sift_down(0, self._get_swapped_child_index(0))
            return root

    # extracts minimum value in O(logn) time
    def extract_min(self):
        if not self._min_heap:
            raise ValueError('Only min heaps support extract_min')
        return self._extract_root()

    # extracts maximum value in O(logn) time
    def extract_max(self):
        if self._min_heap:
            raise ValueError('Only max heaps support extract_max.')
        return self._extract_root()

    # deletes node from anywhere in heap in O(logn) time
    # input: key (i.e. index) of node to delete
    def delete(self, key):
        self._swap(key, len(self._heap) - 1)
        removed = self._heap.pop()

        p_i = (key - 1) // 2
        if not self._is_balanced(self._heap[p_i], self._heap[key]):
            self._sift_up(p_i, key)
        else:
            self._sift_down(p_i, key)

        return removed

    # initializes a heap in O(n) time
    def heapify(self):  # to do
        return self._heap


# input: filename
# output: sum of 10000 medians (for 10000 numbers in input file) modulo 10000
def heap_median_maintenance(filename):
    sum = 0
    H_low = Heap(0)  # max heap
    H_high = Heap()  # min heap
    l_size = 0
    h_size = 0

    with open(filename) as f_handle:
        for line in f_handle:
            n = int(line)
            median = H_low.get_root()
            if not median:
                H_low.insert(n)
                sum += n
                l_size += 1
            elif l_size == h_size:
                # if n > median, insert n into high heap only to extract the min, insert this
                # median into low heap, and add it to sum
                if n > median:
                    H_high.insert(n)
                    high_min = H_high.extract_min()
                    H_low.insert(high_min)
                    sum += high_min
                # if n <= last median, insert n into low heap and add root to sum
                else:
                    H_low.insert(n)
                    sum += H_low.get_root()
                l_size += 1
            elif l_size > h_size:
                # if n >= median, add already known median to sum and insert into high heap
                if n >= median:
                    H_high.insert(n)
                    sum += median
                # if n < last median, insert n into low heap only to extract the max, insert
                # it into high heap, and add root of low heap to sum
                else:
                    H_low.insert(n)
                    H_high.insert(H_low.extract_max())
                    sum += H_low.get_root()
                h_size += 1

    return sum % 10000


def main():
    start = time.time()
    result = heap_median_maintenance('Median.txt')
    print('result: ', result)
    print('elapsed time: ', time.time() - start)


main()
