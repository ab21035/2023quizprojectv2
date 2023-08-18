import random

#funtions go here
def yes_no(question):
  valid = False
  while not valid:
    response = input(question).lower()
    
   # if they say "yes", output 'Program continues'
    if response == "yes" or response == "y":
      response = "yes"
      return response
  
    #If they say "no" output, 'Display instructions'
    elif response == "no" or response == "n":
      response = "no"
      return response
      
    else:
      print()
      print("Please answer the question with yes/no")
      print()

print("Welcome To The Annual MATH QUIZ.")
#instructions funtion goes here
def instructions():
  print()
  print("****How To Play****")
  print()
  print("The rules of the quiz are simple.")
  print()
  print("You will be asked 10 randomized mathematical questions that you\nwill have to answer.")
  print()
  print("The question will be Multiplication questions.")
  print()
  print("In the Quiz you will have 3 lives or al 10 questions are answered, you will lose 1 live everytime\nyou get a question wrong.")
  print()
  print("When all 3 lives are lost, the quiz will end.")
  return ""

#main routine goes here
print()
played_before = yes_no("Have you played this game before?\n")

if played_before == "no":
  instructions()
print()
print("Good Luck and Have Fun!")

def multiplication_gen():
  #Variables
  score = 0
  lives = 3
  rounds_played = 0

  #run the game until users plays all 10 rounds or loses all 3 lives
  while lives > 0 and rounds_played < 10:
    #generate two random numbers
    num1 = random.randint(1,10)
    num2 = random.randint(1,15)
    #User stats
    

      #increase # of rounds played
    rounds_played += 1
      #Print round number
    print()
    print("*** Round #{} ***".format(rounds_played))
    print()
    print(f"Score: {score}  Lives: {lives}")

    #ask user the question
    print()
    print("What is", num1, "x" ,num2, "=")
    #user answer
    answer = input()
    #To check if answer is invalid or blank
    if not answer or not answer.isdigit():
      print("Invalid input. Please enter a number.") 
      lives -= 1
      print(f"Lives: {lives}")
      continue 
    #if answer is correct/incorrect  
    if int(answer) == num1 * num2:
      print("Correct!")
      score += 1
    else:
      print("Incorrect")
      print()
      print(f"The correct answer is {num1 * num2}")
      lives -= 1


multiplication_gen()

  #end game counclusion
  print()
  print("Game over...")
  print()
  print(f"Rounds Played: {rounds_played}")
  print()
  print(f"Correct Answer: {score}")
  print()
  print(f"Lives Left: {lives}")
  
  print()
  print("Thank you for playing the Multiplication quiz")
