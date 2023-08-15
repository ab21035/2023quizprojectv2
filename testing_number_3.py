import random

def num_gen():
    
  #Generate a multiplication quiz with score and lives.
  
    score = 0
    lives = 3
    rounds_played = 0
    
    for x in range(10):
        rounds_played += 1
        
        # Generate two random numbers
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 15)
        
        print()
        print("What is {} x {} =".format(num1, num2))
        user_ans = int(input(""))
        answer = num1 * num2
        
        # Check if the user's answer is correct
        if user_ans == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect")
            lives -= 1
            print("The correct answer is:\n{}".format(answer))
        
        print("Your score is: {}".format(score))
        print("You have {} lives left".format(lives))



num_gen()
  


  
  
 
  
  






  


    
    
