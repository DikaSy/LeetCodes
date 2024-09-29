class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        mergedWord = ""
        while word1 != "" or word2 != "":
            if word1 == "":
                mergedWord += word2
                break
            elif word2 == "":
                mergedWord += word1
                break
            mergedWord = mergedWord + word1[0] + word2[0]
            word1 = word1[1::]
            word2 = word2[1::]
        return mergedWord