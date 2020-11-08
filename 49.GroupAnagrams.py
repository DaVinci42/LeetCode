from typing import List, Dict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache: Dict[str, List[str]] = {}
        for s in strs:
            k = "".join(sorted(s))
            cache[k] = cache.get(k, []) + [s]
        return list(cache.values())
