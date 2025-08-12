from collections import OrderedDict, defaultdict
from typing import Self


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.count = 1
        self.prev: Self | None = None
        self.next: Self | None = None

    def remove(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node

        if node.next:
            node.next.prev = node

    def empty(self):
        return self.head.next is self.tail

    def remove(self):
        if self.empty():
            return
        return self.tail.prev.remove()  # type: ignore


class LFUCache_DLL:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.manifest = {}
        self.counts = defaultdict(DoubleLinkedList)
        self.min_count = 1

    def get(self, key: int) -> int:
        if key in self.manifest:
            self.manifest[key].count += 1
            self.increment(key)
            return self.manifest[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.manifest:
            self.manifest[key].val = value
            self.manifest[key].count += 1
        else:
            if self.capacity <= len(self.manifest):
                self.delete()

            self.manifest[key] = Node(key, value)
            self.min_count = 1
        self.increment(key)

    def increment(self, key: int):
        node = self.manifest[key]
        node.remove()
        if self.counts[node.count - 1].empty() and self.min_count == node.count - 1:
            self.min_count += 1

        self.counts[node.count].insert(node)
        return node

    def get_lfu_node(self):
        return self.counts[self.min_count].tail.prev

    def delete(self):
        node = self.get_lfu_node()
        if node:
            node.remove()
            self.manifest.pop(node.key)


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_count = defaultdict(int)
        self.count_to_keys = defaultdict(OrderedDict)
        self.min_count = 0

    def get(self, key: int) -> int:
        if key in self.key_to_count:
            self.increment(key)
            return self.get_value(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_count:
            self.increment(key)
            self.set_value(key, value)
        elif 0 < self.capacity:
            if self.capacity <= len(self.key_to_count):
                self.remove_lfu()

            self.key_to_count[key] = 1
            self.min_count = 1
            self.set_value(key, value)

    def get_storage(self, key: int):
        return self.count_to_keys[self.get_count(key)]

    def get_value(self, key: int):
        return self.get_storage(key)[key]

    def set_value(self, key: int, value: int):
        self.get_storage(key)[key] = value

    def increment(self, key: int):
        value = self.get_storage(key).pop(key)

        if len(self.get_storage(key)) == 0 and self.key_to_count[key] == self.min_count:
            self.min_count += 1

        self.key_to_count[key] += 1
        self.get_storage(key)[key] = value

    def get_count(self, key: int):
        return self.key_to_count[key]

    def get_lfu(self):
        return next(reversed(self.count_to_keys[self.min_count].items()))

    def remove_lfu(self):
        key, value = self.count_to_keys[self.min_count].popitem(False)
        count = self.key_to_count.pop(key)

        if count == self.min_count and len(self.count_to_keys[count]) == 0:
            self.min_count += 1
            self.count_to_keys.pop(count)

        return key, value, count


def test_dll():
    dll = DoubleLinkedList()
    nodes = [Node(i, i) for i in range(10)]

    for node in nodes:
        dll.insert(node)

    assert not dll.empty()

    assert nodes[0].next is dll.tail
    assert nodes[-1].prev is dll.head

    for _idx in range(10):
        idx = (7 * _idx) % 10
        prev = nodes[idx].prev
        next = nodes[idx].next
        nodes[idx].remove()

        assert prev and prev.next is next
        assert next and next.prev is prev

    assert dll.empty()

    for node in nodes:
        dll.insert(node)

    for idx in range(9):
        node = dll.remove()

        assert nodes[idx + 1].next is dll.tail
        assert dll.tail.prev is nodes[idx + 1]


def test_cache_get():
    cache = LFUCache(2)
    cache.put(1, 1)
    assert cache.get_count(1) == 1
    assert cache.get(1) == 1
    assert cache.get_count(1) == 2
    assert cache.get(2) == -1

    # assert cache.counts[1].empty()
    # assert not cache.counts[2].empty()
    # node = cache.counts[2].head.next
    # assert node and node.key == node.val == 1
    # assert node and node.count == 2


def test_cache_put_below_cap():
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get_count(1) == cache.get_count(2) == 1
    assert cache.get(1) == 1
    assert cache.get(2) == 2
    assert cache.get_count(1) == cache.get_count(2) == 2


def test_cache_put_above_cap():
    cache = LFUCache(1)
    cache.put(1, 1)
    assert cache.get_count(1) == 1
    lfu_key, _ = cache.get_lfu()
    assert lfu_key == 1 and cache.get_count(lfu_key) == 1
    cache.put(2, 2)
    assert cache.get_count(2) == 1
    assert cache.get(1) == -1
    assert cache.get(2) == 2


def test_cache_put_increments():
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(1, 2)
    lfu_key, _ = cache.get_lfu()
    assert cache.get_count(1) == cache.get_count(lfu_key) == 2


def test_lfu_is_lru_at_level():
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)

    assert cache.get(1) == 1
    assert cache.get(2) == 2


def test_lfu_after_remove():
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1

    # lfu = cache.get_lfu_node()
    # assert lfu and lfu.key == lfu.val == 2
    # assert lfu and lfu.count == 1

    cache.put(3, 3)

    assert cache.get(2) == -1

    # lfu = cache.get_lfu_node()
    # assert lfu and lfu.key == lfu.val == 3


def test_zero_cap_cache():
    cache = LFUCache(0)
    cache.put(1, 1)
    assert cache.get(1) == -1


def test_cache_2():
    # [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)

    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    assert cache.get(3) == 3
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
