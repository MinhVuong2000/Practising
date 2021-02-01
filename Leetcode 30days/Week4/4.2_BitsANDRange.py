class Solution:
def rangeBitwiseAnd(self, m: int, n: int) -> int:
    #sure that in range it only similar in first bits
    i=0
    while m!=n:
        m>>=1
        n>>=1
        i+=1
    return n<<i
