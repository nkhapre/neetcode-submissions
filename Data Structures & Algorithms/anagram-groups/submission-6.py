class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS not in check:
                check[sortedS] = [s]
            else:
                check[sortedS].append(s)
        return list(check.values())