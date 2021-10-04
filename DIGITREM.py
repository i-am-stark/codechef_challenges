def check_num(n, d):
    num = n
    sm1 = 1
    sm2 = 0
    pos = 1
    rm = 0
    
    while(num):
        rm = num%10
        if rm == d:
            sm1 *= pos
            return sm1-sm2
        else:
            sm2+= rm*pos
            pos*= 10
            num= int(num/10)
    return 0
    
def sol(n, d, ans):
    tmp = check_num(n, d)
    if(tmp == 0):
        print(ans)
        return
    else:
        ans+= tmp
        n+= tmp
        sol(n,d,ans)

def main():
    for _ in range(int(input())):
        n, d = list(map(int, input().split()))
        ans = 0
        sol(n,d,ans)
        
main()