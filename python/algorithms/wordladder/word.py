from copy import deepcopy
from algorithms.wordladder import large_input


class Solution(object):
    def __init__(self):
        self.tracked = []

    def differ_by_one(self, word1, word2, word_size):
        differ = 0
        for i in xrange(word_size):
            if word1[i] != word2[i]:
                differ += 1
                if differ > 1:
                    return False
        return True

    def find_mutations(self, word, wordlist):
        possible_mutations = []
        size_word = len(word)

        for dictword in wordlist:
            if self.differ_by_one(word, dictword, size_word):
                possible_mutations.append(dictword)

        return possible_mutations

    def remove_words(self, wordlist, words):
        for word in words:
            wordlist.remove(word)

    def findLadders(self, begin_word, end_word, wordlist):

        paths = [WordTracked(begin_word)]
        i = 0

        while i < len(paths):
            path = paths[i]

            if path.is_word(end_word):
                return len(path.tracked), path.tracked

            possible_mutations = self.find_mutations(path.word, wordlist)

            for possible in possible_mutations:
                new_path = deepcopy(path)
                new_path.add(possible)
                paths.append(new_path)
            else:
                if self.differ_by_one(path.word, end_word, len(end_word)):
                    path.tracked.append(end_word)
                    return len(path.tracked), path.tracked

            self.remove_words(wordlist, possible_mutations)

            i += 1


class WordTracked(object):
    def __init__(self, word):
        self.word = word
        self.tracked = [word]

    def add(self, word):
        self.word = word
        self.tracked.append(word)

    def is_word(self, word):
        return self.word == word

    def __repr__(self):
        return ', '.join(self.tracked)


print Solution().findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
