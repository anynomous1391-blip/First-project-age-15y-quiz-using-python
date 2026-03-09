score = 0
Ans1 = "guido van rossum"
Ans2 = "elon musk"
Ans3 = "bill gates"
Ans4 = "steve jobs"


q1 = input("who is the creator of python:").lower()
if q1 == Ans1:
	print("correct answer")
	score += 5
	
else:
	print("wrong answer try next time")
	
q2 = input("who is richest man in the world:")
if q2 == Ans2:
	print("correct answer")
	score += 5
	
else:
	print("wrong answer try next time")

q3 = input("who is the founder of microsoft:").lower()
if q3 == Ans3:
	print("correct answer")
	score += 5
	
else:
	print("wrong answer try next time")
	
q4 = input("who is the founder of apple:")
if q4 == Ans4:
	print("correct answer")
	score += 5
	
else:
	print("wrong answer try next time")
	
print("Your total score is", score)

print("Thank you for playing quiz")
