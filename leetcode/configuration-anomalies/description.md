# Configuration Anomalies

The software developers at Amazon are working on detecting configuration anomolies in a Server. They are provided with a set of configurations represented by _config_, a string of concatenated decimal digits (0-9). However, some digits in these configuraitons have been inadvertantly erased.

These configurations were initially generated using a specific procedure involving two integer parameters, _x_ and _y_.

The procedure begins with the two numbers, _x_ and _y_, and initializes a current value (cur) to 0. The following operation can be performed any number of times:

- In each step either x or y is added to curr
- Compute the unit digit of cur % 10 after each addition
- record this digit as part of the configuration sequence.

The first character of each sequence is either _x_ or _y_.

Identify the final configuration with the minimal possible decimal value from which the given configuration is can be constructed by removing specific digits of the final configuraiton. If multiple configurations can be formed by reconstructing the missing digits, return the one with the minimum decimal value among all possible valid configurations.

If no valid configurations can be restored using the described procedure, return the string '-1'

### Example 1

config = '27'
x = 2
y = 3

ans = 247

**Explanation**
cur = 0
cur += x % 10 = 2
cur += x % 10 = 4
cur += y % 10 = 7

Note: 257 is also possible but less than 
