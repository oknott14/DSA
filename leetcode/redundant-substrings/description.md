# Redundant Substrings

A string is redundant if the length of the string `|string| = a * V + b * C` where a and b are given and V and C are the number of vowels and consonants in the string. Given a string `string` find the number of redundant substrings.

### Example 1

word = 'abbacc'
a = -1
b = 2
output = 3

| Substring | Vowels | Consonants | Length | a _ V + b _ C |
| --------- | ------ | ---------- | ------ | ------------- |
| abb       | 1      | 2          | 3      | 3             |
| bba       | 1      | 2          | 3      | 3             |
| bac       | 1      | 2          | 3      | 3             |
