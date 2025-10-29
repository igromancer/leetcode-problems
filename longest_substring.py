def lengthOfLongestSubstring(s: str) -> int:
    max_len = 0
    start = 0
    end = 1
    while end <= len(s):
        tmp = s[start:end]
        print(len(tmp))
        if len(tmp) == len(set(tmp)):
            max_len = max(max_len, len(tmp))
            end += 1
        else:
            start += 1
            end += 1
    return max_len


# print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring(" "))
