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

def instructions():
  print()
  print("****How To Play****")
  print()
  print("The rules of the quiz go here")
  print()
  return ""

#main routine goes here
print()
played_before = yes_no("Have you played this game before?\n")

if played_before == "no":
  instructions()
print()
print("Program continues\n")




