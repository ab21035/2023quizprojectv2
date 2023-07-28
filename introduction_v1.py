show_instructions = ""
while show_instructions.lower() != "xxx":  
    # ask the user if they have played this game before
  show_instructions = input("Have you played this game before?").lower()
  
  # if they say "yes", output 'Program continues'
  if show_instructions == "yes" or show_instructions == "y" :
    print("Program continues")
  #If they say "no" output, 'Display instructions'
  elif show_instructions == "no" or show_instructions == "n" :
    print("Display instructions")
  #If they output is yes/no, display 'Please answer the quetsion with yes or no'
  else:
    print("Please answer the question with yes/no")