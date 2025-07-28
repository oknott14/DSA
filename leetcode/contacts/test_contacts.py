from typing import Dict, List, Tuple


class Trie:
    def __init__(self, num_below: int = 0):
        self.next: Dict[str, Trie] = {}
        self.num_below = num_below

    def add(self, s: str):
        curr = self
        idx = 0

        while idx < len(s) and s[idx] in curr.next:
            curr.num_below += 1
            curr = curr.next[s[idx]]
            idx += 1
        
        curr.num_below += 1
        
        while idx < len(s):
            curr.next[s[idx]] = Trie(1)
            curr = curr.next[s[idx]]
            idx += 1

    def search(self, s: str) -> int:
        curr = self

        for char in s:
            if char in curr.next:
                curr = curr.next[char]
            else:
                return 0

        return curr.num_below


def contacts(queries: List[Tuple[str, str]]) -> List[int]:
    # Write your code here
    trie = Trie()
    output = []
    for action, inp in queries:
        if action == "add":
            trie.add(inp)
        else:
            output.append(trie.search(inp))

    return output


def test_case_1():
    queries = [
        ("add", "ed"),
        ("add", "eddie"),
        ("add", "edward"),
        ("find", "ed"),
        ("add", "edwina"),
        ("find", "edw"),
        ("find", "a"),
    ]

    assert contacts(queries) == [3, 2, 0]
