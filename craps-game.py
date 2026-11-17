import random


def roll_dice():
 
  die1 = random.randint(1, 6)
  die2 = random.randint(1, 6)
  total = die1 + die2
  return die1, die2, total


def play_craps():
  welcome_message = ("\n Welcome to the Python Craps Game! \n")
  rules = ("RULES: " 
           "You need to roll dice. In order to win, the sum of dice numbers needs to be 7 or 11. If you get 2,3 or 12, you lose. \n"
  "ATTENTION! If your sum is any other number (4,5,6,8,9), the previous rules do not matter anymore. \n"
  "That number you got is called a goal number, which becomes the one you should get by rolling the dice again. \n"
  "If your sum appears to be 7, you lose. If your sum is the goal number, you win. \n"
  "Good Luck! \n")
  print(welcome_message)
  print(rules)

  point_numbers = [4, 5, 6, 8, 9, 10]

  input("To roll the dice press Enter ")

  d1, d2, sum_val = roll_dice()
  print(f"You rolled a {d1} and a {d2}. Total sum: {sum_val}")

  if sum_val in [7, 11]:
      print("You won!")
      return True
  elif sum_val in [2, 3, 12]:
      print("Craps! The casino won.")
      return False
  else:
      goal_number = sum_val
      print(f" Your goal number is set to: {goal_number}.")

      while True:
        input("Press Enter to roll again ")
        d1, d2, sum_val = roll_dice()
        print(f"You rolled a {d1} and a {d2}. Total sum: {sum_val}")

        if sum_val == goal_number:
          print("You hit your goal! You win!")
          return True
        elif sum_val == 7:
          print("You lost. (you rolled a 7 before your goal number)")
          return False

play_craps()