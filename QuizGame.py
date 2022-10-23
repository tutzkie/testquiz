print("Welcome to my malupet na quiz!")

name = input("What is your name?: ")

print("Hello " + name + " are you ready?")

playing = input("Do you want to play? yes or no? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play putangina mo :D")
score = 0

answer = input("What is nothing? ")
if answer.lower() == "nothing":
    print('Correct! howd you know')
    score += 1
else:
    print("Incorrect! the answer is nothing")

answer = input("Is dogsex good? yes or no ")
if answer.lower() == "yes":
    print('Correct! you sick fuck')
    score += 1
else:
    print("Incorrect! bro it's good")

answer = input("Who is the best vtuber? ")
if answer.lower() == "gura":
    print('Correct! Im biased')
    score += 1
else:
    print("Incorrect! bobo si gura best vtuber")

answer = input("BBM or Leni? ")
if answer.lower() == "Pacquiao":
    print('Correct! uy bat mo alam')
    score += 1
else:
    print("Incorrect! tanga si Pacquiao number 1")

answer = input("bobo ka ba? oo o hindi? ")
if answer.lower() == "oo":
    print('Correct! buti alam mo')
    score += 1
else:
    print("Incorrect! patingin mo na utak mo")

answer = input("BBM 6.9% inflation tama o mali? ")
if answer.lower() == "tama":
    print('Correct! galing mo naman')
    score += 1
else:
    print("Incorrect! ew apologist")

answer = input("Single ba si Archie? (1)yes, (2)no, (3)tropa time ")
if answer.lower() == "3":
    print('Correct! tropa time muna')
    score += 1
else:
    print("Incorrect! di mo need ng bebe tropa time lang")

answer = input("cat anal is the best? yes or no? ")
if answer.lower() == "no":
    print('Correct! good')
    score += 1
else:
    print("Incorrect! kadiri ka")

answer = input("ML best game? yes or no? ")
if answer.lower() == "no":
    print('Correct! yan di ka bobo')
    score += 1
else:
    print("Incorrect! ew maglaro ka nga ng ibang laro bata")

answer = input("pogi/maganda ka ba? yes or no? ")
if answer.lower() == "yes":
    print('Correct! naks')
    score += 1
else:
    print("Incorrect! grabe naman tingin mo sa sarili mo, baka totoo pero kahit na")

print("You got " + str(score) + " questions correct!")
print("overall " + str(score) + " out of 10!")

answer = input("goodjob galing mo naman! sige close mo na tapos na ")