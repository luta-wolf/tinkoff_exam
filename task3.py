# x = 0
# n = int(input())
# list = input().split()
# num_list = [int(i) for i in list]
# num_list.sort()
# while(True):
# 	for i in range(n):
# 		if (i == 0):
# 			t = x * x - num_list[i]
# 		else:
# 			t = t * t - num_list[i]
# 		if (t < 0):
# 			x += 1
# 			break
# 	if (t > 0):
# 		break
# print(x)

from math import sqrt
from math import ceil

x = 0
n = int(input())
list = input().split()
num_list = [int(i) for i in list]
num_list.sort()
for i in range(n - 1, -1, -1):
	x = sqrt(x + num_list[i])
print(ceil(x))