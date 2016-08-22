import heapq

class PriorityQueue:
    def __init__(self, priority_function):
        self.heap = []
        self.count = 0
        self.priority_function = priority_function

    def push(self, item):
        priority = self.priority_function(item)
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def is_empty(self):
        return len(self.heap) == 0
