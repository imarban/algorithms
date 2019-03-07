class Solution(object):
    def wordPattern(self, pattern, chk):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        words = chk.split(" ")
        letters = [c for c in pattern]

        if len(words) != len(letters):
            return False

        byletter = {letter: word for letter, word in zip(letters, words)}
        byword = {word: letter for letter, word in byletter.items()}

        i = 0
        for word in words:
            if byword.get(word, None) != letters[i]:
                return False
            i += 1

        return True


print Solution().wordPattern("abba", "dog cat cat dog")
print Solution().wordPattern("abba", "dog dog dog fish")
print Solution().wordPattern("aaaa", "dog cat cat dog")
print Solution().wordPattern("abba", "dog dog dog dog")
print Solution().wordPattern("aaa", "aa aa aa aa")
