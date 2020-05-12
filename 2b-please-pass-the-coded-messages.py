def solution(l):
    while(sum(l)%3 > 0):
        m = sum(l)%3
        if(m==1 and 1 in l):
            l.remove(1)
        elif(m==2 and 2 in l):
            l.remove(2)
        elif(m==1 and 4 in l):
            l.remove(1)
        elif(m==2 and 5 in l):
            l.remove(5)
        elif(m==1 and 7 in l):
            l.remove(7)
        elif(m==2 and 8 in l):
            l.remove(8)
        else:
            l.remove(min(l))
        
    l.sort(reverse = True)
    res = sum(d * 10**i for i, d in enumerate(l[::-1])) 
    return res