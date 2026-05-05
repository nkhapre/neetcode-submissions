class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            check[sortedS].append(s)
        return list(check.values())