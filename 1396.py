class UndergroundSystem:
    def __init__(self):
        self.travelTimes = {}
        self.checkedIn = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedIn[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkedInStation, checkedInTime = self.checkedIn.pop(id)
        tripTime = t - checkedInTime

        trip = (checkedInStation, stationName)
        trips, tripsTimeSum = self.travelTimes.get(trip, (0, 0))
        self.travelTimes[trip] = (trips + 1, tripsTimeSum + tripTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trips, tripsTimeSum = self.travelTimes.get((startStation, endStation), (0, 0))
        return tripsTimeSum / trips


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
