def solution(n):
    n=int(n)
    count = 0

    while(n!=1):
        if(n%2==0):
            n=n>>1
        elif((n==3) or ((n+1)&n) > ((n-1)&(n-2))):
            n-=1
        else:
            n+=1
        count+=1
    return count

    ######## FIRST IMPLEMENTATION ########
    ##### No idea why it didn't work #####
    ###### Help needed to debug it #######

    # count = 0
    # while(n > 3):
    #     if(n & 1):
    #         a=n+1
    #         b=n-1
    #         ac=bc=0
            
    #         while not (a & 1):
    #             a=a>>1
    #             ac+=1

    #         while not (b & 1):
    #             b=b>>1
    #             bc+=1

    #         if (ac>bc):
    #             n+=1
    #         else:
    #             n-=1
    #     else:
    #         n = n >> 1
    #     count+=1
        
    # if(n==3):
    #     count+=2
    # elif(n==2):
    #     count+=1
    # return count