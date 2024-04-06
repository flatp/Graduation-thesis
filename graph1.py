import random
#Determine the score
n = random.randint(0,100) 
#Assign ratings to score
if n < 30 :
	print("Score:", n, "(D)")
elif n < 60 :
	print("Score:", n, "(C)")
elif n < 80 :
	print("Score:", n, "(B)")
else :
	print("Score:", n, "(A)")