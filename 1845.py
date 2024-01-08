import heapq


class SeatManager:

    def __init__(self, n: int):
        self.heap = [i for i in range(1, n + 1)]

    def reserve(self):
        return heapq.heappop(self.heap)

    def unreserve(self, seatNumber: int):
        heapq.heappush(self.heap, seatNumber)
