n = list(map(int, input().split()))
n.sort()
a = n[0]
b = n[1]
c = n[-1] - (a+b)
print(a, b, c)