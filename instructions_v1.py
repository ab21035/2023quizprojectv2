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
  print("In the Quiz you will have 3 lives, you will lose 1 live everytime\nyou get a question wrong.")
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




