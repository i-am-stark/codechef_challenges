def mex(ar, n):
    st = []
    for i in range(1, n+2):
        st.append(0)
    for i in ar:
        if i<= n:
            st[i]= 1
    return(st.index(0))

for _ in range(int(input())):
    n, d = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    b = []
    
    for i in range(0, n):
        k = n-i-1
        for j in range(0,k+1):
            ar = nums[j:k+1]
            b.append(mex(ar, k+1-j))
    b.sort()
    print(b[d-1])
    