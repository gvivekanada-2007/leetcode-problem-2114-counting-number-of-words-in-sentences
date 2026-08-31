class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        #vivek = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
        k = 0
        for j in range(len(sentences)):
            s = sentences[j] 
            tem = 1
            for i in range(len(s)):
                v = s[i]
                if v == ' ':
                   tem = tem + 1
            k=max(k , tem)
        return k
