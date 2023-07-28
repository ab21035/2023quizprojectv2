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

#main routine goes here
print()
show_instructions = yes_no("Have you ever played this game before?")
print()
print("You chose {}".format(show_instructions))
print()
