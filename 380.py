import random


class RandomizedSet:

    def __init__(self):
        self.itemMap = {}
        self.stack = []

    def insert(self, val: int) -> bool:
        if val in self.itemMap:
            return False

        self.stack.append(val)
        self.itemMap[val] = len(self.stack) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.itemMap:
            return False

        lastStackItem = self.stack[-1]
        thisItemIndex = self.itemMap.pop(val)

        # Update last iteme
        if lastStackItem != val:
            self.itemMap[lastStackItem] = thisItemIndex
            self.stack[thisItemIndex] = lastStackItem
        self.stack.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.stack)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
