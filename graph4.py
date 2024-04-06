import matplotlib.pyplot as plt
import random
#Define dice()
def dice():
	return random.randint(1,6)
#Define dicesum()
def dicesum():
	return dice() + dice()
#Define dicegame(n)
def dicegame(n):
	n = int(n)
	sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	V = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	#Count the number of times
	for num in range(n):
		sum = dicesum()
		if sum == 2:
			sums[0] = sums[0] + 1
		elif sum == 3:
			sums[1] = sums[1] + 1
		elif sum == 4:
			sums[2] = sums[2] + 1
		elif sum == 5:
			sums[3] = sums[3] + 1
		elif sum == 6:
			sums[4] = sums[4] + 1
		elif sum == 7:
			sums[5] = sums[5] + 1
		elif sum == 8:
			sums[6] = sums[6] + 1
		elif sum == 9:
			sums[7] = sums[7] + 1
		elif sum == 10:
			sums[8] = sums[8] + 1
		elif sum == 11:
			sums[9] = sums[9] + 1
		else:
			sums[10] = sums[10] + 1
	print("Probability distribution of the dice sum with", n, "simulations:")
	#Calculate and display probabilities
	for totall in range(11):
		V[totall] = sums[totall] / n
		print("P(dice_sum=", totall + 2, ") is", V[totall])
	labels = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
	x_pos = range(11)
	plt.bar(x_pos, V, tick_label = labels) #Draw the graph
	plt.show() #Show the graph

dicegame(1000)
