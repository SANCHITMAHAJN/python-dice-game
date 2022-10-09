import random
#Sanchit Mahajan , 000819207
print("COMP 10001 - W2020 Final Project by Sanchit Mahajan, "
      "student number 000819207" + "\n" +
      " Welcome to my dice game, good luck!" +  "\n" )

score = []                                                    #This list contains individual scores of each game.
dieRolls = []                                                 #This list contains the randomly generated numbers of the current game.
bonus = []                                                    #This list contains the bonus points for matching patterns

#My Student Number: 000819207
# Therefore 000819207 % 500 = 207, we'll add this to our score later on. Till then let's name it "a"
a = 207
turn = 1         #It's the current turn which the user is playing.
nextTurn = ""    # It's the input for asking about the next turn from the user.
faces = 0        # No. of faces/ sides of the die.
total=0
while not faces:                                                #Here we are using a while loop so that the input
        try:                                                    #command keeps on showing until the user inputs a valid
            faces = input("Enter # of faces [2,20]: ")          #number.
            if 20 < int(faces) or int(faces) < 2:
                raise ValueError
        except ValueError:
            faces = 0
            print("I'm sorry, that isn't a valid positive integer, please try again a number between 2 and 20: ")

if 2<= int(faces) <= 20:                                #This is where the game continues when the number of faces are valid.

        diceNumber = 0                                  #The number of dice being used in the game, We're starting with 0 to start a loop.
        while not diceNumber:
                try:
                    diceNumber = input("Enter # of dice [3,6]: ")
                    if 6 < int(diceNumber) or int(diceNumber) < 3:
                        raise ValueError
                except ValueError:
                    diceNumber = 0
                    print("I'm sorry, that isn't a valid positive integer, please try again using a number between 3 and 6")

        if 2<= int(diceNumber) <= 20:       #This is where the game continues when both the sides and number of dice are valid.
             while turn != 0:  #While loop to keep continuing the game until the user says no.
                bonus = []
                total = 0
                dieRolls=[]
                count = 0                   #count is a variable which will keep adding up until it generates the required number of values.
                while count < int(diceNumber):
                    value = random.randint(1,int(faces))
                    dieRolls.append(value)
                    count=count+1

                rolledSum = int(sum(dieRolls))             #Sum of all the die rolls in the particular game.
                roundedValue = int(rolledSum/int(diceNumber)) #Truncating the decimal part.
                print("\n You have rolled:" + str(dieRolls) +"\n These die sum to" , rolledSum , "and have an average rounded value of" ,roundedValue)

                maxScore = int(int(diceNumber)*int(faces))   #The maximum possible score per game
                percentage = float(rolledSum/maxScore)       #Percentage is calculated to be further multiplied by bonus factor.


                #MATCHING PATTERNS
                #Pattern1
                if int(faces) >= 4:
                    if int(len(set(dieRolls))) <= 1:    #len(set) = 1 when all the numbers are same
                        bonus.append(10)
                        print("\nPattern 1 matched! All the die rolls have the same value.")

                    else:
                        print("\nPattern 1 not matched in your roll" , dieRolls, "some dice are different.")
                else:
                    print("\nPattern 1 not matched, the number of sides on the dice is less than 4.")

                #Pattern 2
                if maxScore >= 20:
                    for i in range(2, rolledSum//2):  #A number is prime when it isn't divisible by any number from 2 to number/2
                        if  rolledSum % i == 0:
                            print("Pattern 2 not matched,", rolledSum, "is not a prime number.")
                            break

                    else:
                        print("Pattern 2 matched,", rolledSum, "is a prime number.")
                        bonus.append(15)
                else:
                    print("Pattern 2 not matched,the maximum score here is less than 20.")



                #Pattern 3
                if int(diceNumber) >= 5:
                    greaterNumbers= len([i for i in dieRolls if i >= roundedValue])  #For a number in dieRolls to be greater than the rounded value
                    if greaterNumbers >= int(len(dieRolls)/2):
                        print("Pattern 3 matched, at least half of dices in", dieRolls,"are greater than rounded value.")
                        bonus.append(5)
                    else:
                        print("Pattern 3 not matched, at least half of dices in", dieRolls,"are NOT greater than rounded value.")
                else:
                    print("Pattern 3 not matched, your number of dices is less than 5.")


                #Pattern 4
                if 4 < int(diceNumber) < int(faces):
                     if int(len(set(dieRolls))) == int(diceNumber):  #len(set) is always equal to the number of results when all the results are different
                        bonus.append(8)
                        print("Pattern 4 matched, all the values in", dieRolls," are different.")
                     else:
                         print("Pattern 4 not matched, some of the values in", dieRolls," are same.")
                else:
                    print("Pattern 4 not matched, either the number of dice is less than 4 or the number of dice is more than the number of sides.")


                #Pattern 5
                if sum(bonus) == 0:
                    print("Pattern 5 matched! You didn't match any other pattern.")
                    bonus.append(1)
                else:
                    print("Pattern 5 not matched, you already matched 1 or more patterns.")

                bonusFactor = sum(bonus)                               #Adding up all the bonus factor
                print("\n Your bonus factor is", bonusFactor)

                product = percentage*bonusFactor
                total = int(207 + product,)     #We were told that our final score will be the sum of 207 + the product of bonus factor and percentage
                print("\n These dice are worth", total, "points.")




                #Rerolling the dice
                ifReroll=input("\nDo you want to reroll any dice? ['yes', 'no']: ")

                while ifReroll.lower() != "yes" and ifReroll.lower() != "no":
                    print("I'm sorry, the choices are ['yes', 'no']. Please pick one of them. ")
                    ifReroll=input("Do you want to reroll any dice? ['yes', 'no']: ")

                    if ifReroll.lower() == "yes" or ifReroll.lower() == "no":
                        break

                if ifReroll.lower() == "yes":
                    ifRerollValue = 0
                    currentDie = 1
                    while True:                           #While loop so that the program keeps asking to re roll until all the die rolls are covered.
                        print("\nDie", currentDie , "is", dieRolls[ifRerollValue])
                        reroll= input("Do you want to roll again?['yes', 'no']: ")

                        while reroll.lower() != "yes" and reroll.lower() != "no":
                            print("I'm sorry, the choices are ['yes', 'no']. Please pick one of them. ")
                            reroll=input("Do you want to roll again? ['yes', 'no']: ")

                            if reroll.lower() == "yes" or reroll.lower() == "no":
                                break

                        if reroll.lower() == "yes":
                            sure= input("Are you sure?['yes', 'no']: ")   #Confirming the re rolling

                            while sure.lower() != "yes" and sure.lower() != "no":
                                print("I'm sorry, the choices are ['yes', 'no']. Please pick one of them. ")
                                sure=input("Are you sure? ['yes', 'no']: ")

                                if sure.lower() == "yes" or sure.lower() == "no":
                                    break

                            if sure.lower() == "yes":


                                

                                #Calculation
                                dieRolls[ifRerollValue] = random.randint(1,int(faces))
                                rolledSum = int(sum(dieRolls))
                                roundedValue = round(rolledSum/int(diceNumber), 0)
                                print("\n You have rolled:" + str(dieRolls) +"\n These die sum to" , rolledSum , "and have an average rounded value of" ,roundedValue)

                                maxScore = int(int(diceNumber)*int(faces)) #The maximum score possible
                                percentage = float(rolledSum/maxScore) #percentage

                                

                                #Patterns for re rolling
                                if int(faces) >= 4:
                                    if int(len(set(dieRolls))) <= 1:
                                        bonus.append(10)
                                        print("\nPattern 1 matched!")

                                    else:
                                        print("\nPattern 1 not matched in your roll" , dieRolls, ".. some dice are different.")
                                else:
                                    print("\nPattern 1 not matched, the number of sides on the dice is less than 4.")

                                if maxScore >= 20:
                                    for i in range(2, rolledSum//2):
                                        if  rolledSum % i == 0:
                                            print("Pattern 2 not matched,", rolledSum, "is not a prime number.")
                                            break

                                    else:
                                        print("Pattern 2 matched! ", rolledSum, "is a prime number.")
                                        bonus.append(15)
                                else:
                                    print("Pattern 2 not matched,the maximum score here is less than 20.")

                                if int(diceNumber) >= 5:
                                    greaterNumbers= len([i for i in dieRolls if i >= roundedValue])
                                    if greaterNumbers >= int(len(dieRolls)/2):
                                        print("Pattern 3 matched! At least half of dices in", dieRolls,"are greater than rounded value.")
                                        bonus.append(5)
                                    else:
                                        print("Pattern 3 not matched, at least half of dices in", dieRolls,"are NOT greater than rounded value.")
                                else:
                                    print("Pattern 3 not matched, your number of dices is less than 5.")

                                if 4 < int(diceNumber) < int(faces):
                                     if int(len(set(dieRolls))) == int(diceNumber):
                                        bonus.append(8)
                                        print("Pattern 4 matched! all the values in", dieRolls," are different.")
                                     else:
                                         print("Pattern 4 not matched, some of the values in", dieRolls," are same.")
                                else:
                                    print("Pattern 4 not matched, either the number of dice is less than 4 or the number of dice is more than the number of sides.")

                                if sum(bonus) == 0:
                                    print("Pattern 5 matched!You didn't match any other pattern.")
                                    bonus.append(1)
                                else:
                                    print("Pattern 5 not matched, you already matched 1 or more patterns.")


                                print("\n Your bonus factor is", bonusFactor)

                                b = percentage*bonusFactor
                                total = int(a + b)
                                print("\n These dice are worth", total, "points.")

                            if sure.lower()== "no":
                                print("Dice not rerolled!")
                        if reroll.lower() == "no":
                            print("Dice not rerolled!")

                        ifRerollValue = ifRerollValue + 1
                        currentDie = currentDie + 1

                        if ifRerollValue >= int(diceNumber) :
                            break
                score.append(total)
                avgScore = int(sum(score)/turn) #The average score for all the turns played
                if ifReroll.lower() == "no":
                    print("No dice were re rolled.")

                if  total == avgScore:
                    print("\n This was your turn number", turn,"and you scored", total, "points, which is equal to the average score of", avgScore)

                elif total < avgScore:
                    print("\n This was your turn number", turn,"and you scored", total, "points, which is less than the average score of", avgScore)

                else:
                    print("\n This was your turn number", turn,"and you scored", total, "points, which is greater than the average score of", avgScore)

                #Next Turns



                #For second turn
                if turn == 1:
                    print("Let's play again!")

                    turn += 1

                # For other turns
                else:
                    nextTurn = input("\n Wannna play again?")

                    if nextTurn.lower() == "yes":
                        turn+=1

                    if nextTurn.lower() == "no":
                        print("\n You played", turn, "turns today with an average score of", avgScore, "points.")
                        break











































