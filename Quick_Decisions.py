# Quick Decisions 2 Task 1
# To practice the use of shorthand if statements in determining event-related
# decisions.

# Code Correction
# you are provided with a python scripts that is supposed to help in event 
# planning, but it has errors.  Identify and fix them.abs

attendees = int(input("Enter number of attendees:"))

venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Quick Decisions 2 Task 2
# Based opn the corrected code from Task1 1, further enhance the program to
# recommend additonal facilities like "audio system" or "projector"based on number 
# of attendees.

attendees = int(input("Enter number of attendees:"))

venue = "large hall" if attendees > 100 else "conference room"
print(venue)
tech = "audio system" if attendees > 20 else "one speaker"
print(tech)

#Quick Decsions 2 Task 3
# Ask the user if they want vegetarian.  Recommend "Vieegie Delight Caterers"
# if yes, otherwise reo=commend "Gourmet Meal Caterers"

attendees = int(input("Enter number of attendees:"))
food_type = input("Would you like vegetarian? (yes / no):")

venue = "large hall" if attendees > 100 else "conference room"
print(venue)
tech = "audio system" if attendees > 20 else "one speaker"
print(tech)
caterer = "Veggie Delight Caterers" if food_type == "yes" else "Gourment Meals Caterers"
print(caterer)