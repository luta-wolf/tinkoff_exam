m, n = map(int, input().split())
arr = [[0 for i in range(m)] for j in range(n)]
arr[n-1][0] = 1
for y in range(n-1, -1, -1):
	for x in range(0, m, 1):
		e1 = 0
		e2 = 0
		if y == n - 1 and x == 0:
			continue
		if y + 2 <= n - 1 and x - 1 >= 0:
			e1 = arr[y + 2][x - 1]
		if y + 1 <= n - 1 and x - 2 >= 0:
			e2 = arr[y + 1][x - 2]
		arr[y][x] = e1 + e2
print(arr[0][m-1])