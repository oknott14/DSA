class Solution:
  def reverseBits(self, n: int) -> int:
    result = 0

    for _ in range(32):
      bit = n & 1
      result = (result << 1) | bit
      n >>= 1

    return result

soln = Solution()

def test_case_1():
  input = 43261596
  output = 964176192
  assert soln.reverseBits(input) == output

def test_case_2():
  input = 4294967293
  output = 3221225471
  assert soln.reverseBits(input) == output