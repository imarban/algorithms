class Solution(object):
    def is_match(self, s, p):

        if p == '*':
            return True

        if '*' not in p and len(s) != len(p):
            return False

        sidx = 0
        pidx = 0

        while pidx < len(p):
            if p[pidx] == '?':
                sidx += 1
                pidx += 1
                if sidx > len(s):
                    return False

            elif p[pidx] == '*':
                pidx += 1

                if pidx >= len(p):
                    return True

                for k in xrange(sidx, len(s)):
                    if s[sidx] != p[pidx]:
                        sidx += 1
                    else:
                        pidx += 1
                        break

            else:
                if sidx >= len(s) or p[pidx] != s[sidx]:
                    return False
                pidx += 1
                sidx += 1

        return True


print Solution().is_match("abefcdgiescdfimde", "ab*cd?i*de")
