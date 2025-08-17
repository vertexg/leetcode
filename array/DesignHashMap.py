class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [dict() for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        self.buckets[self._hash(key)][key] = value

    def get(self, key: int) -> int:
        return self.buckets[self._hash(key)].get(key, -1)

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        if key in bucket:
            del bucket[key]

    def contains(self, key: int) -> bool:
        return key in self.buckets[self._hash(key)]

https://leetcode.com/problems/design-hashmap/
