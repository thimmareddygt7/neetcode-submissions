class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        so = {}
        
        for s in strs:
            key = "".join(sorted(s))
            
            if key not in so:
                so[key] = []
            so[key].append(s)
            
        return list(so.values())