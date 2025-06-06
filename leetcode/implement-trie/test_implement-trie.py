from ast import Dict, In
from typing import List, Self
import os
class Node:
  @property
  def is_leaf(self) -> bool:
    return len(self.next) == 0
  
  @property
  def length(self) -> int:
    return len(self.val)
  
  def __init__(self, val: str, next: List[Self] = []):
    self.val = val
    self.next = next

  def search(self, word: str) -> bool:
    if self.is_leaf:
      return self.val == word
    elif word.startswith(self.val):
      return any(node.search(word[self.length:]) for node in self.next)
    return False

  def startsWith(self, word: str) -> bool:
    if len(word) <= self.length:
      return self.val.startswith(word)
    else:
      return any(node.startsWith(word[self.length:]) for node in self.next)
  
  def insert(self, word: str) -> bool:
    if self.val == '' and word == '':
      return True
    
    idx = 0
    end = min(self.length, len(word))

    while idx < end and word[idx] == self.val[idx]:
      idx += 1

    if idx == 0:
      return False
    
    elif idx < self.length: # split val
      node = Node(self.val[idx:], self.next.copy())
      self.val = self.val[:idx]
      self.next = [Node(word[idx:], []), node]
    elif self.is_leaf and idx < len(word):
      self.next = [Node(word[idx:], []), Node('', [])]
    else:
      if not any(node.insert(word[idx:]) for node in self.next):
        self.next.append(Node(word[idx:], []))

    return True

# class Trie:
#   def __init__(self):
#     self.head = {}

#   def insert(self, word: str) -> None:
#     if word[0] in self.head:
#       self.head[word[0]].insert(word)
#     else:
#       self.head[word[0]] = Node(word, [])

#   def search(self, word: str) -> bool:
#     if word[0] in self.head:
#       return self.head[word[0]].search(word)
#     return False

#   def startsWith(self, word: str) -> bool:
#     if word[0] in self.head:
#       return self.head[word[0]].startsWith(word)
#     return False

class CharNode:

  def __init__(self, val: str):
    self.val = val[0]
    self.is_leaf = len(val) == 1
    self.next = {}
    
    if not self.is_leaf:
      self.next[val[1]] = CharNode(val[1:])

  def insert(self, word: str): 
    if self.val == word[0]:
      if len(word) == 1:
        self.is_leaf = True
      elif word[1] in self.next:
        self.next[word[1]].insert(word[1:])
      else:
        self.next[word[1]] = CharNode(word[1:])
  
  def search(self, word: str):
    if self.val == word[0]:
      if len(word) == 1:
        return word == self.val and self.is_leaf
      elif word[1] in self.next:
        return self.next[word[1]].search(word[1:])
    return False
  
  def startsWith(self, prefix: str):
    if self.val == prefix[0]:
      if len(prefix) == 1:
        return True
      elif prefix[1] in self.next:
        return self.next[prefix[1]].startsWith(prefix[1:])
      
    return False
    

class Trie:
  def __init__(self):
    self.head = dict()

  def insert(self, word: str) -> None:
    node = self.head
    for char in word:
      if not char in node:
        node[char] = dict()
      node = node[char]
    node['#'] = True
        
  def search(self, word: str) -> bool:
    node = self.head
    for char in word:
      if not char in node:
        return False
      node = node[char]
    return '#' in node

  def startsWith(self, word: str) -> bool:
    node = self.head
    for char in word:
      if not char in node:
        return False
      node = node[char]
    return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

def test_case_1():
  trie = Trie()
  trie.insert("apple")
  assert trie.search("apple") # return True
  assert not trie.search("app") # return False
  assert trie.startsWith("app") # return True
  trie.insert("app")
  assert trie.search("app")

def test_case_2():
  trie = Trie()
  words = [
    'clean'
    'remedy'
    'favorable'
    'momentum'
    'bulb'
    'situation'
    'axis'
    'influence'
    'simplicity'
    'sacred'
    'strange'
    'share'
    'time'
    'forecast'
    'raise'
    'laborer'
    'core'
    'cat'
    'quarrel'
    'squash'
  ]
  for word in words:
    trie.insert(word)

  for word in words:
    assert trie.search(word)

    for idx in range(1, len(word)):
      assert trie.startsWith(word[:idx])

def test_case_3():
  trie = Trie()
  assert not trie.startsWith('a')

def test_node_init():
  node = Node('apple')
  assert node.val == 'apple'
  assert node.is_leaf

def test_node_search_whole_word():
  node = Node('apple')
  assert node.search('apple')

def test_node_search_partial_word():
  node = Node('apple')
  assert not node.search('app')

def test_node_startswith_whole_word():
  node = Node('apple')
  assert node.startsWith('apple')

def test_node_startswith_partial_word():
  node = Node('apple')
  assert node.startsWith('app')

def test_insert_node_with_commonality():
  node = Node('apple')
  assert node.insert('app')
  assert node.val == 'app'
  assert len(node.next) == 2
  assert all(n.val == 'le' or n.val == '' for n in node.next)

def test_insert_node_with_no_commonality():
  node = Node('apple')
  assert not node.insert('bark')
  assert node.val == 'apple'
  
def test_node_insert_many():
  node = Node('apple')
  assert node.insert('apricot')
  assert node.val == 'ap'
  assert any(n.val == 'ricot' for n in node.next)
  assert any(n.val == 'ple' for n in node.next)
  node.insert('app')
  assert any(n.val == 'ricot' for n in node.next)
  assert any(n.val == 'p' for n in node.next)
  assert node.next[1].val == 'p'
  assert any(n.val == '' for n in node.next[1].next)
  assert any(n.val == 'le' for n in node.next[1].next)
  

def test_case_4():
  trie = Trie()
  for word in ["app","apple", "beer","add","jam","rental"]:
    trie.insert(word)
  
  for word, result in [("apps", False),("app", True),("ad", False),("applepie",False),("rest", False),("jan", False),("rent", False),("beer", True),("jam", True)]:
    assert result == trie.search(word)

  for word, result in [("apps", False),("app", True),("ad", True),("applepie",False),("rest", False),("jan", False),("rent", True),("beer", True),("jam", True)]:
    assert result == trie.startsWith(word)

def test_case_5():
  trie = Trie()
  trie.insert('apple')
  trie.insert('app')
  assert trie.search('apple')
  assert trie.search('app')

def test_abaa():
  trie = Trie()
  trie.insert('ab')
  assert not trie.search('a')
  assert trie.startsWith('a')