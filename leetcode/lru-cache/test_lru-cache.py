from typing import List, Ordered


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            if self.capacity <= len(self.cache):
                self.cache.popitem(last=False)
            self.cache[key] = value


def run_test_case(actions: List[str], inputs: List[List[int]]) -> List[int | None]:
    cache = LRUCache(inputs[0][0])
    outputs: List[int | None] = [None]
    for action, input in zip(actions[1:], inputs[1:]):
        if action == "put":
            outputs.append(cache.put(input[0], input[1]))
        elif action == "get":
            outputs.append(cache.get(input[0]))
    return outputs


def test_case_1():
    actions = [
        "LRUCache",
        "put",
        "put",
        "get",
        "put",
        "get",
        "put",
        "get",
        "get",
        "get",
    ]
    inputs = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    outputs = [None, None, None, 1, None, -1, None, -1, 3, 4]

    assert run_test_case(actions, inputs) == outputs


def test_case_single_capac():
    cache = LRUCache(1)

    cache.put(1, 1)

    assert cache.get(1) == 1

    cache.put(2, 2)

    assert cache.get(1) == -1
    assert cache.get(2) == 2


def test_update():
    cache = LRUCache(2)
    cache.put(1, 1)
    assert cache.get(1) == 1
    cache.put(1, 2)
    assert cache.get(1) == 2
