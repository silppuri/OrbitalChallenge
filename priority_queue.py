import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item):
        entry = (item[0], self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def is_empty(self):
        return len(self.heap) == 0
