# Beginning: create variables
winter_points = 0
summer_points = 0


# Middle: ask questions
# question 1
answer = input ("Would you rather A) Ski or Snowboard, or B) Swim or Dive?")
if answer == "A":
    winter_points += 1
elif answer == "B":
    summer_points += 1


# question 2
answer = input ("Do you prefer A) Christmas, or B) Memorial Day?")
if answer == "A":
    winter_points += 1
elif answer == "B":
    summer_points += 1


# question 3
answer = input ("Would you rather A) Build a snowman, or B) Build a sandcastle?")
if answer == "A":
    winter_points += 1
elif answer == "B":
    summer_points += 1


# question 4
answer = input ("Do you like A) Snow, or B) Sun?")
if answer == "A":
    winter_points += 1
elif answer == "B":
    summer_points += 1


# question 5
answer = input ("Would you rather A) Relax indoors, or B) Adventure outdoors?")
if answer == "A":
    winter_points += 1
elif answer == "B":
    summer_points += 1

 # End of quiz:
if winter_points > summer_points:
    print ("You are a winter person")
elif winter_points < summer_points:
    print ("You are a summer person")