n = int(input())
city = list(map(int, input().split()))
price = list(map(int, input().split()))
c = price[0]
t = 0
for x in range(len(city)):
  if price[x] < c:
    c = price[x]
  t += c*city[x]
print(t)