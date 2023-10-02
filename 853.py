from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for carPosition, carSpeed in zip(position, speed):
            cars.append((carPosition, carSpeed))
        cars.sort(reverse=True)

        stack = []
        for position, speed in cars:
            stack.append((target - position) / speed)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
