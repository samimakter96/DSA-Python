"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones
you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are
also jewels.
Letters are Case sensitive, so "a" is considered a different type of stone from "A".


Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0
"""

# Brute force Approach:
# stones = "aAAbbbb"
# jewels = "aA"
# count = 0
# for i in range(len(stones)):
#     for j in range(len(jewels)):
#         if stones[i] == jewels[j]:
#             count += 1
# print(count)

# Time Complexity : O(N^2)  Space Complexity : 0(1)


# Approach 2 : Using Set
# stones = "aAAbbbb"
# jewels = "aA"
# count = 0
# jewels_set = set(jewels)
# for stone in stones:
#     if stone in jewels_set:
#         count += 1
# print(count)

# Time Complexity : O(N)   Space Complexity : O(N)

# Optimal Approach: Using Dictionary
stones = "aAAbbbb"
jewels = "aA"

count = 0
freq_map = {}

# Count the frequency of each character in stones
for item in stones:
    freq_map[item] = freq_map.get(item, 0) + 1

# After the first loop, freq_map will be {'a': 1, 'A': 2, 'b': 4}

# Count the occurrences of jewels using the frequency map
for item in jewels:
    count += freq_map.get(item, 0)

# In the second loop, for 'a', count += freq_map['a'] => count += 1
# For 'A', count += freq_map['A'] => count += 2

# After the second loop, count will be 3

print(count)


# without using get() method
stones = "aAAbbbb"
jewels = "aA"

stone_frq_map = {}
for item in stones:
    if item in stone_frq_map:
        stone_frq_map[item] += 1
    else:
        stone_frq_map[item] = 1
print(stone_frq_map)

count = 0
for item in jewels:
    if item in stone_frq_map:
        count += stone_frq_map[item]
print(count)


'''freq_map.get(char, 0) + 1
Get the current count of the character from freq_map. If the character is not there, assume the count is 0. Then, 
add 1 to this count.'''

stones = "aAAbbbb"
freq_map = {}

# Initial state of freq_map is an empty dictionary: {}

# Iterating through each character in stones
# First iteration (char = 'a'):
freq_map['a'] = freq_map.get('a', 0) + 1
# freq_map is now {'a': 1}

# Second iteration (char = 'A'):
freq_map['A'] = freq_map.get('A', 0) + 1
# freq_map is now {'a': 1, 'A': 1}

# Third iteration (char = 'A'):
freq_map['A'] = freq_map.get('A', 0) + 1
# freq_map is now {'a': 1, 'A': 2}

# Fourth iteration (char = 'b'):
freq_map['b'] = freq_map.get('b', 0) + 1
# freq_map is now {'a': 1, 'A': 2, 'b': 1}

# Fifth iteration (char = 'b'):
freq_map['b'] = freq_map.get('b', 0) + 1
# freq_map is now {'a': 1, 'A': 2, 'b': 2}

# Sixth iteration (char = 'b'):
freq_map['b'] = freq_map.get('b', 0) + 1
# freq_map is now {'a': 1, 'A': 2, 'b': 3}

# Seventh iteration (char = 'b'):
freq_map['b'] = freq_map.get('b', 0) + 1
# freq_map is now {'a': 1, 'A': 2, 'b': 4}

# After iterating through all characters in stones, freq_map is {'a': 2, 'A': 2, 'b': 4}

