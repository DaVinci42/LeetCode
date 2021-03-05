class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleDict = {"type": 0, "color": 1, "name": 2}
        return sum(map(lambda i: 1 if i[ruleDict[ruleKey]] == ruleValue else 0, items))
