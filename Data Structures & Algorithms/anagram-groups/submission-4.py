class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = defaultdict(list)
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
        
            check[s].append(strs[i])
        return list(check.values())