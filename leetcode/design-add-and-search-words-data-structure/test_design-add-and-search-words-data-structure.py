import os
from typing import Dict

class WordDictionary:
  def __init__(self):
    self.w_dict = {}

  def addWord(self, word: str) -> None:
    curr = self.w_dict

    for w in word:
      if not w in curr:
        curr[w] = {}
      curr = curr[w]

    curr['#'] = True

  def search(self, word: str) -> bool:
    return self.search_helper(word, self.w_dict)
  
  def search_helper(self, word: str, curr: Dict) -> bool: 
    for idx in range(len(word)):

      if word[idx] == '.':
        return any(False if nxt is True else self.search_helper(word[idx+1:], nxt) for nxt in curr.values())
      
      elif not word[idx] in curr:
        return False
      
      curr = curr[word[idx]]

    return '#' in curr

def run_file_test(file_name: str):
  f = open(f'{os.path.dirname(__file__)}/test_cases/{file_name}.txt', 'r')
  
  line = f.readline()
  word_dict = WordDictionary()
  while line:
    [action, input, output] = line.strip('\n').split(' ')

    if action == 'WordDictionary':
      word_dict = WordDictionary()
    elif action == 'addWord':
      word_dict.addWord(input)
    elif action == 'search':
      res = output == 'true'
      assert word_dict.search(input) == res

    line = f.readline()
def test_case_1():
  run_file_test('case_1')

def test_false_with_any():
  words = WordDictionary()

  words.addWord('bad')
  words.addWord('mad')
  words.addWord('lad')

  assert not words.search('..b')
  assert not words.search('b.t')
  
  words.addWord('lab')
  words.addWord('bat')
  
  assert words.search('..b')
  assert words.search('b.t')

def test_empty_any():

  words = WordDictionary()
  assert not words.search('.')
  
def test_case_2():
  run_file_test('case_2')