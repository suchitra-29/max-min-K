l=list(map(int,input().split()))
l.sort()
k=int(input())
print(f"{k} minimum is {l[k-1]}")
print(f"{k} maximum is {l[-k]}")