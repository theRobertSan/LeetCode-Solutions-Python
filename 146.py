class Node:

    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.mru, self.lru = Node(0, 0), Node(0, 0)
        self.lru.next, self.mru.prev = self.mru, self.lru

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.capacity:
            lru_node = self.lru.next
            self.remove(lru_node)
            del self.cache[lru_node.key]

    def add(self, node: Node):
        prev, nxt = self.mru.prev, self.mru
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
