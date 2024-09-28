class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        temp = []
        for c in s:
            temp.append(c)
        for i in range(len(temp)):
            s[i] = temp.pop()