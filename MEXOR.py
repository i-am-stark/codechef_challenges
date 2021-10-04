for _ in range(int(input())):
    n = int(input())
    i = 1
    if(n==0):
        print('1')
    elif(n==1 or n== 2):
        print('2')
    else:
        while(2**i <=n):
            i+=1
        tmp = 2**(i-1)
        if(tmp == n):
            print(n)
        elif((tmp*2 -1) == n):
            print(n+1)
        else:
            print(tmp)

            