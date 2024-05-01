# First non repeating stream of characters using : Dictionary

A = "abadbc"

lst = []
mp = {}
ans = ""

for ch in A:
    if ch not in mp:     # new character visited first time
        lst.append(ch)
        mp[ch] = 1
    else:
        # any repeated character encountered
        if ch in lst:
            lst.remove(ch)

    ans += lst[0] if lst else "#"
print(ans)


# Approach 2: Using Queue

from collections import deque

A = "abadbc"
ans = ""
mp = {}
q = deque()

for i in range(len(A)):
    if A[i] not in mp:
        q.append(A[i])
    mp[A[i]] = mp.get(A[i], 0) + 1

    while len(q) > 0 and mp[q[0]] > 1:
        q.popleft()

    if len(q) > 0:
        ans += q[0]
    else:
        ans += "#"
print(ans)
