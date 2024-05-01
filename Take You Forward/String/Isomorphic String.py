
def isomorphic(s, t):
    s_map = {}
    t_map = {}

    for i in range(len(s)):
        c1 = s[i]
        c2 = t[i]

        if (c1 in s_map and s_map[c1] != c2) or (c2 in t_map and t_map[c2] != c1):
            return False
        s_map[c1] = c2
        t_map[c2] = c1
    return True


s = "foo"
t = "bar"
print(isomorphic(s, t))

