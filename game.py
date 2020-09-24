#python 3.7.1
import random
print ("Hello, Welcome To The Stone, paper and scissor Game")
print()
print("Game Rules:-\n1.You have to Play This Game 10 Times\n2.Maximum Number of win will win the game")
print()
print("Method To Play:-\n1.Stone can beat Scissor\n2.Paper can beat Stone\n3.Scissor can beat Paper")

i=1
c=0
u=0

l=["stone","paper","scissor"]
		
while(i<=10):
  print()
  print("Option:- stone, paper, scissor")
  
  comp = random.choice(l)
  print()
  user=input("Your Choice:- ")
  
  if(user==comp):
  	
      print("\nTie 😯")
      print("\nOpponent has chosen ", comp)
      c+=1
      u+=1
   
  elif(user=="scissor" and comp=="paper"):
    
      print("\nYou Win!")
      print("\nOpponent has chosen ", comp)
      u+=1
    
  elif(user=="stone" and comp=="scissor"):
      
     print("\nYou Win!")
     print("\nOpponent has chosen ", comp)
     u+=1
    
  
  elif(user=="paper" and comp=="stone"):
      
      print("\nYou Win!")
      print("\nOpponent has chosen ", comp)
      u+=1
    
  elif(user=="paper" and comp=="scissor"):
  	
      print("\nOpponent Wins!")
      print("\nOpponent has chosen ", comp)
      c+=1
    
  elif(user=="stone" and comp=="paper"):
      print("\nOpponent Wins!")
      print("\nOpponent has chosen ", comp)
      c+=1
    
  elif(user=="scissor" and comp=="stone"):

      print("\nOpponent Wins!")
      print("\nOpponent has chosen ", comp)
      c+=1
  else:
  	print("\n! Invalid Input")
  	i=i-1
  print("\nPlay more ",10-i,'times for final result.')
  i+=1   
    
  
print("\nFinal Result 😱:-")
if(c==u):
  print("\nBoth Win🤣")
  
elif (c>u):
  print("\nOpponent Wins😭")
  
else:
  print("\nYay! You are a champion 🤘\n")

print("\nHope I will See You again😉")
