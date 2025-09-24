n = int(input())
t=0
lst = [0 for x in range(1001)]
for x in range(n):
  a, b, c = map(int, input().split())
  t = a-1
  for y in range(b-a+1):
    lst[t] += c
    t += 1
print(max(lst))