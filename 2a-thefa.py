def solution(l,t):
    ans=[-1,-1]
    for keyi,i in enumerate(l):
        for keyj,j in enumerate(l):
            if sum(l[keyi:keyj+1]) == t:
                return [keyi, keyj]
    return ans