from heapq import heappush, heapify


class MinStack:
    def __init__(self):
        self.ms = []
        self._hq = []

    def push(self, val: int) -> None:
        heappush(self._hq, val)
        self.ms.append(val)

    def pop(self) -> None:
        self._hq.remove(self.ms.pop())
        heapify(self._hq)

    def top(self) -> int:
        return self.ms[-1]

    def getMin(self) -> int:
        return self._hq[0]
