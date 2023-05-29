t = "car"
s = "rat"
if len(t) != len(s):
    print("not anagram")
else:
    count_t, count_s = {}, {}
    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(s[i], 0)
    for c in count_s:
        if count_s[c] != count_t.get(c, 0):
            print("not anagram")
