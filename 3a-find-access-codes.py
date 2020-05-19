def solution(l):
    res=0
    twoCount=[0 for _ in range(len(l))]
    
    for i in range(1, len(l)-1):
        for j in range(0, i):
            if(l[i]%l[j]==0):
                twoCount[i]+=1

    for i in range(2, len(l)):
        for j in range(1, i):
            if(l[i]%l[j]==0):
                res += twoCount[j];

    return res