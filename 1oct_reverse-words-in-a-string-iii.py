class Solution:
    def reverseWords(self, str1: str) -> str:
        lis1= str1.split(" ")
        lis2=[]

        for i in lis1:
            a= list(i)
            a.reverse()
            es= "".join(a)
            lis2.append(es)

        st= " ".join(lis2)

        return st
        