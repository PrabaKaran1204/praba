import random 
print('welcome to rock/paper/scissors game')
computer_score=0
your_score=0
option=('rock','paper','scissors')

while True:
   random_number=random.randint(0,2)
   computer_pick=option[random_number]
   guess=input('Type rock/paper/scissors or Q to quit:')
   if 'q'==guess.lower():
     print('your score:',your_score,'and','computer score:',computer_score)
     break
   if guess.lower()==computer_pick:
          print('you win')
          your_score+=1
   elif guess.lower() not in option:
      continue
   else:
      print('computer win')
      computer_score+=1
        
          
    
    
    
    
    
       
    
        
    
    
    
    
 
