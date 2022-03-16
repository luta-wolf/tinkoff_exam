a, b, n = map(int, input().split())
if (a > b and a - n >= b + n and (a - b) %2 == 0):
	print("YES")
else:
	print("NO")