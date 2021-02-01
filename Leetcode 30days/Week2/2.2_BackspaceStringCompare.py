class Solution:
def backspaceCompare(self, S: str, T: str) -> bool:
    lenS = len(S)-1
    lenT = len(T) - 1
    delete = 0
    
    while (lenS >=0 or lenT >=0):
        while (lenS >=0):
            if (S[lenS]=='#'):
                lenS-=1
                delete +=1
            elif (delete>0):
                lenS-=1
                delete -=1
            else:
                break
                
        while (lenT >=0):
            if (T[lenT]=='#'):
                lenT-=1
                delete +=1
            elif (delete>0):
                lenT-=1
                delete -=1
            else:
                break
                
        if (lenS<0): return lenT <0
        if (lenT<0): return lenS <0
        if (S[lenS]!=T[lenT]): return False
        lenS-=1
        lenT-=1
    return True
    
#other
"""
    s,t=[],[]
    
    for char in S:
        if char!='#':
            s.append(char)
        else:
            if len(s)>0:
                s.pop()
    
    for char in T:
        if char!='#':
            t.append(char)
        else:
            if len(t)>0:
                t.pop()
    
    return s==t
"""
