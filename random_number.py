import random

# low = 1
# high = 100
# number = random.randint(low, high) this will return a return int() number between 1 -100
# number = random.random() this will return a random float() numbers
# options = ("rock", "paper", "scissors")
# option = random.choice(options)

cards = ["2","3","4","5","6", "7","8", "9" , "j", "k", "l", "m"]
random.shuffle(cards)
print(cards)
  
options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
while player not in options:
  player = input("Enter a choice(rock, paper, scissors): ")

print(f"Player: {player}")
print(f"Computer: {computer}")

if player == computer:
    print("It's a tie!")
elif player =="rock"   and computer == "scissors":
    print("Player wins!")
elif player == "paper" and computer == "rock":
    print("Player wins!")
elif player == "scissors" and computer == "paper":  
    print("Player wins!")
elif computer == "rock" and player == "scissors":
    print("Computer wins!")
elif computer == "paper" and player == "rock":
    print("Computer wins!")
elif computer == "scissors" and player == "paper":
    print("Computer wins!")
else:
    print("You lose!")