import re

class Solution:
    def vowelError(self, query, word, regex):
        query = re.sub(regex, "0", query.lower())
        word = re.sub(regex, "0", word.lower())
        for i in range(len(query)):
            if word[i] != query[i]:
                return False
        return True
    
    def spellchecker(self, wordlist, queries):
        matchList = [""]*len(queries)
        queryIndexList = list(range(len(queries)))
        regexVowel = re.compile("[AaEeIiOoUu]")
        
        for i in queryIndexList:
            query = queries[i]
            hasMatch = False
            #exact match
            for word in wordlist:
                if query == word:
                    matchList[i] = word
                    hasMatch = True
                    break
                
            if hasMatch:
                continue

            #case insensitive match
            for word in wordlist:
                if query.lower() == word.lower():
                    matchList[i] = word
                    hasMatch = True
                    break

            if hasMatch:
                continue      
                    
            #vowel error match
            for word in wordlist:
                if len(query) == len(word) and self.vowelError(query, word, regexVowel):
                    matchList[i] = word
                    break
                    
        return matchList

sol = Solution()
match = sol.spellchecker(["KiTe","kite","hare","Hare"], ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"])
print(match)
#["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

class Solution2(object):
    def spellchecker(self, wordlist, queries):
        def devowel(word):
            return "".join('*' if c in 'aeiou' else c
                           for c in word)

        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(devowel(wordlow), word)

        def solve(query):
            if query in words_perfect:
                return query

            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]

            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ""

        return map(solve, queries)