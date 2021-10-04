# cook your dish here
def inp():
    t = int(input())
    return t
    
def main():
    for _ in range(inp()):
        s,l = list(map(int, input().split()))
        if(s>0 and l>0):
            print("Solution")
        elif(s>0):
            print("Solid")
        else:
            print("Liquid")
main()