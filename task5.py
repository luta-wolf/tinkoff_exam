from math import sqrt


print(int(sqrt(100) + 2))
print(2**300)
a = 2**300
while(True):
	a = a/10**10
	print(a)
	if a < 3:
		break

