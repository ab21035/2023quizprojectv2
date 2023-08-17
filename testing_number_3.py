import random

def num_gen():
    
    for x in range(10):
        
        
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
            
        else:
            print("Incorrect")
            
            print("The correct answer is:\n{}".format(answer))
        



num_gen()
  


  
  
 
  
  






  


    
    
