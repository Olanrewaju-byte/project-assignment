print("welcome to femi's computer quiz!")

playing = input("Do you want to play? ")
 
if playing != "yes":
    quit()

print("Okay! let's play: )")
score = 0

answer = input("what does cpu stands for? ")
if answer == "central processing unit":
    print('correct!')
    score += 1
else:
    print("incorrect!")

answer = input("what does RAM stands for? ")
if answer == "random access memory":
    print('correct!')
    score += 1
else:
    print("incorrect!")      

answer = input("what does gpu stands for? ")
if answer == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print("incorrect!")

answer = input("does femi have sense? ")
if answer == "yes":
    print('correct!')
    score += 1
else:
    print("incorrect!")

print("you got " + str(score) + "questions correct!")

