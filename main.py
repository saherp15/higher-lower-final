from art import logo
from game_data import data
import random
from art import vs
from replit import clear
print(logo)
def format_data(account):
  account_name=account["name"]
  account_desc=account["description"]
  account_country=account["country"]
  return f"{account_name}, {account_desc}, from {account_country}"
def check(user,A_follower,B_follower):
  if A_follower>B_follower and user=="a":
    return True
  elif B_follower>A_follower and user=="b":
    return True
  else:
    return False
score=0
game_should=True
B=random.choice(data)
while game_should:
  A=B
  B=random.choice(data)
  if A==B:
    B=random.choice(data)
  print(f"Compare A:{format_data(A)}")
  print(vs)
  print(f"Compare B:{format_data(B)}")
  user=input("Who has more followers? Type 'A' or 'B': ").lower()
  A_follower=A["follower_count"]
  B_follower=B["follower_count"]
  is_correct=check(user,A_follower,B_follower)
  clear()
  print(logo)
  if is_correct:
    score+=1
    print(f"You're right! Current score: {score}")
    
  else:
    game_should=False
    print(f"Sorry, That's wrong. Final score is {score}.")
  
  




