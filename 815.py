from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stationToRoute = defaultdict(set)
        for i, route in enumerate(routes):
            for station in route:
                stationToRoute[station].add(i)
        queue = deque([source])

        seenRoutes, seenStations = set(), set()
        buses = 1

        while queue:
            numStations = len(queue)

            for _ in range(numStations):
                station = queue.popleft()
                seenStations.add(station)

                for routeIndex in stationToRoute[station]:
                    if routeIndex not in seenRoutes:
                        for newStation in routes[routeIndex]:
                            if newStation == target:
                                return buses

                            if newStation not in seenStations:
                                queue.append(newStation)

                        seenRoutes.add(routeIndex)

            buses += 1

        return -1
