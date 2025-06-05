class Solution:
  def minWindow(self, s: str, t: str) -> str:
    if len(t) == 1 and t in s:
      return t
    
    chars = {}
    found_chars = dict.fromkeys(list(t), 0)
    min_char = 0
    sub_string = ''
    
    for char in t:
      found_chars[char] -= 1
    
    while min_char < len(s) and not s[min_char] in found_chars:
      min_char += 1

    if min_char == len(s):
      return sub_string
    
    chars[s[min_char]] = min_char
    found_chars[s[min_char]] += 1
    found = 1

    for idx in range(min_char + 1, len(s)):
      char = s[idx]

      if char in found_chars:
        if char in chars:
          if not found_chars[char] < 0:
            chars[char] = s.index(char, chars[char] + 1)
            
          else:
            found_chars[char] += 1
            found += 1

          if s[min_char] == char:
            min_char = min(chars.values())
        else:
          chars[char] = idx
          found_chars[char] += 1
          found += 1
        
        

        if found == len(t) and (sub_string == '' or idx - min_char < len(sub_string)):
          sub_string = s[min_char:idx+1]

    return sub_string
      


          
        

          
    

soln = Solution()

def test_case_1():
  s = "ADOBECODEBANC"
  t = "ABC"
  output = 'BANC'
  assert soln.minWindow(s,t) == output

def test_case_2():
  s = "a"
  t = "a"
  output = 'a'
  assert soln.minWindow(s,t) == output

def test_case_3():
  s = "a"
  t = "aa"
  output = ''
  assert soln.minWindow(s,t) == output

def test_case_4():
  s = "ABC"
  t = "ABC"
  output = 'ABC'
  assert soln.minWindow(s,t) == output

def test_case_5():
  s = "ABAABAACDB"
  t = "BC"
  output = 'CDB'
  assert soln.minWindow(s,t) == output


def test_case_6():
  s = "DAGABAACBBEDA"
  t = "DAABCB"
  output = 'ACBBEDA'
  assert soln.minWindow(s,t) == output

def test_case_7():
  s = "a"
  t = "b"
  output = ''
  assert soln.minWindow(s,t) == output