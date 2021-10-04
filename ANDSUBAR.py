# cook your dish here
def inp():
    t = int(input())
    return t
    
def main():
    for _ in range(inp()):
        n= inp()
        i = 0
        if(n==1):
            print('1')
        else:
            while(True):
                if 2**(i+1)>=n:
                    break
                i+=1
            if(2**(i+1) == n):
                ans = 2**(i+1) - 2**i
            else:
                tmp1 = n- 2**i +1
                tmp2 = 2**i- 2**(i-1)
                ans = max(tmp2, tmp1)
            print(ans)
main()