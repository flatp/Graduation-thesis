#Determine one of the number to be multiplied
for n in range(1,10):
	#Determine the other number to be multiplied
	for m in range(1,n):
		print(m, "*", n, "=", m * n, end = "  ")
	print(n, "*", n, "=", n * n)