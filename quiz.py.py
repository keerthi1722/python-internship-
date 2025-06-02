print("Welcome to my computer quiz!")

score = 0
playing = input("Do you want to play? (yes/no): ").lower()

if playing != "yes":
    print("Maybe next time!")
    quit()

print("Okay! Let's play ❤️")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct 😍")
    score += 1
else:
    print("Incorrect 😔")

answer = input("What does API stand for? ").lower()
if answer == "application programming interface":
    print("Correct 😍")
    score += 1
else:
    print("Incorrect 😔")

answer = input("What does GUI stand for? ").lower()
if answer == "graphical user interface":
    print("Correct 😍")
    score += 1
else:
    print("Incorrect 😔")

answer = input("What does HTML stand for? ").lower()
if answer == "hyper text markup language":
    print("Correct 😍")
    score += 1
else:
    print("Incorrect 😔")

answer = input("What does CSS stand for? ").lower()
if answer == "cascading style sheets":
    print("Correct 😍")
    score += 1
else:
    print("Incorrect 😔")

print(f"\nYour final score is {score}/5")

if score >= 4:
    print("You are a Genius 😇")
else:
    print("Don't worry, try again 🫠")
