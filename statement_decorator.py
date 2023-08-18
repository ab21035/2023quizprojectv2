def satement_decorator(statement, decoration):

  sides = decoration * 3

  statement = "{} {} {}".format(sides,statement,sides)
  top_bottom = decoration * len(statement)

  print(top_bottom)
  print(statement)
  print(top_bottom)

  return ""
  
satement_decorator("Welcome To The Annual MATH QUIZ", "=")
satement_decorator("Correct","-")
satement_decorator("Incorrect","!")