class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            if s not in check:
                check[s] = [strs[i]]
            else:
                check[s].append(strs[i])
        return list(check.values())