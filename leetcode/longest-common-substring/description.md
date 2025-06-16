# 1143. Longest Common Subsequence

Medium

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
`A common subsequence of two strings is a subsequence that is common to both strings.`

### Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

### Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

### Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

### Constraints:

- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.

| Index | Text 1 | Text 2 | 
| ----- | ------ | ------ |
| 0     | a      | b      |
| 1     | b      | c      |
| 2     | c      | d      |
| 3     | d      | e      |
| 4     | e      |        |
| 5     | f      |        |
| 6     | z      |        |
| 7     | y      |        |
| 8     | t      |        |
| 9     | d      |        |
| 10    | x      |        |
| 11    | m      |        |
| 12    | r      |        |

| Index | Text 1 | Text 2 | 
| ----- | ------ | ------ |
| 0     | a      | d      |
| 1     | b      | f      |
| 2     | c      | a      |
| 3     | d      | d      |
| 4     | e      | z      |
| 5     | f      | m      |
| 6     | z      |        |
| 7     | y      |        |
| 8     | t      |        |
| 9     | d      |        |
| 10    | x      |        |
| 11    | m      |        |
| 12    | r      |        |

| Index | Text 1 | Text 2 | 
| ----- | ------ | ------ |
| 0     | a      | b      | 1
| 1     | b      | c      | 2
| 2     | c      | a      | 0
| 3     | d      | f      | 5
| 4     | e      | z      | 6
| 5     | f      | b      | 
| 6     | z      | c      |
| 7     | y      | d      |
| 8     | t      | e      |
| 9     | d      | f      |
| 10    | x      | t      |
| 11    | m      | x      |
| 12    | r      | m      |