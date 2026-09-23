class Solution:
    def interpret(self, command: str) -> str:
        def signFunc(x):
            
            ans = ''
            for i in range(len(x)):
                if x[i]=='G':
                    ans=ans+"G"
                elif x[i:i+2]=='()':
                    ans=ans+'o'
                elif x[i:i+4]=='(al)':
                    ans=ans+'al'
            return ans
        return signFunc(command)
 