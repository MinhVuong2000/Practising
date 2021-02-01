class Solution:
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def convert(s):
        res = [0]*26
        for char in s:
            res[ord(char)-ord('a')] += 1
        return tuple(res)
    rec = {}
    res = []
    for s in strs:
        t = convert(s)
        if t in rec:
            res[rec[t]].append(s)
        else:
            res.append([s])
            rec[t] = len(res)-1
    return res
