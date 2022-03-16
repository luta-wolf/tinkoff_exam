# m, n = map(int, input().split())
# count = 0
# while(True):
# 	if (m == n):
# 		count += 1
# 		break
# 	if ( m > n ):
# 		m = m - n
# 		count += 1
# 	elif (n > m):
# 		n = n - m
# 		count += 1
# print(count)

m, n = map(int, input().split())
count = 0
while(n != 0 and m != 0):
	if ( m >= n ):
		count += m//n
		m = m % n
	elif (n > m):
		count += n//m
		n = n % m
print(count)