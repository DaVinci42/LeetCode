class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return "/"

        s, p = [], path.split("/")
        for d in p:
            if d == "." or not d:
                continue
            elif d == "..":
                if s:
                    s.pop()
            else:
                s.append(d)

        return "/" + "/".join(s)
