# cook your dish here
def inp():
    t = int(input())
    return t
    
def main():
    for _ in range(inp()):
        a,b,c,d = list(map(int, input().split()))
        if(a<=d and a+b>d):
            print('3')
        elif(a+b <= d and a+b+c>d):
            print('2')
        else:
            print('1')
            
main()