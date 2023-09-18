from collections import defaultdict
import heapq
from typing import List


class Twitter:
    def __init__(self):
        self.subscriptions = defaultdict(set)
        self.posts = defaultdict(list)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([tweetId, self.counter])
        self.counter -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        minHeap = []

        self.subscriptions[userId].add(userId)
        for followeeId in self.subscriptions[userId]:
            if followeeId in self.posts:
                index = len(self.posts[followeeId]) - 1
                latestPostId, postCounter = self.posts[followeeId][-1]
                heapq.heappush(
                    minHeap, [postCounter, latestPostId, followeeId, index - 1]
                )

        while minHeap and len(result) < 10:
            postCounter, latestPostId, followeeId, index = heapq.heappop(minHeap)
            result.append(latestPostId)
            if index >= 0:
                newPostId, newPostCount = self.posts[followeeId][index]
                heapq.heappush(
                    minHeap, [newPostCount, newPostId, followeeId, index - 1]
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.subscriptions[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.subscriptions:
            self.subscriptions[followerId].remove(followeeId)
