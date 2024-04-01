#Nested Decisions 1 task 1

# The Addventure Game
# You are provided with a python script that is supposed to guide a user through an 
# adventure game, but it has some errors.  Identify them.abs

place = input("Choose a place. (forest / cave):")
action = input("What would you like to do? (climb a tree / cross a river / pass):")

if place == "forest":
  if action == "climb a tree":
    print("You found a birds nest!")
  elif action == "cross a river":
    print("You found a boat!")
  elif place == "cave":
    print("You found a treasure!")
else:
  print("Let's go back to the car!")

# Nested Decisions 1 Task 2  

# Based on te corrected code from Task1, expand the game.  If the user chooses "cave", ask
# them if they want to "light a torch" or "proceed in the dark", and provide outcomes for 
# each decision.abs

place = input("Choose a place. (forest / cave):")
action1 = input("Make a choice. (climb a tree / cross a river / pass):")
action2 = input("Make another choice. (light a torch / proceed in the dark / stop):")

if place == "forest":
  if action1 == "climb a tree":
    print("You found a birds nest!")
  else:
    print("You found a boat!")
if place == "cave":
  if action2 == "light a torch":
    print("Continue with a lighted torch!")
  elif action2 == "proceed in the dark":
    print("You are on your own!") 
else:
  print("Let's go back to the car!")  
    
# Nested Decisions 1 Task 3    

place = input("Choose a place. (forest / cave):")
action1 = input("Make a choice. (climb a tree / cross a river / pass):")
action2 = input("Make another choice. (light a torch / proceed in the dark / stop):")

if place == "forest":
  if action1 == "climb a tree": 
    pass # pass statement
    print("You found a birds nest!")
  else:
    print("You found a boat!")
if place == "cave":
  if action2 == "light a torch":
    print("Continue with a lighted torch!")
  elif action2 == "proceed in the dark":
    print("You are on your own!") 
else:
  print("Let's go back to the car!") 


