import random
sum = 0
while sum <= 26:
	#Decide on two numbers
	n = random.randint(1,13)
	m = random.randint(1,13)
	sum = n + m
	#Stop on the condition that the remaining number that makes the sum 21 is between 1 and 13
	if 8 <= sum < 21:
		break
print(n, m, 21 - n - m)