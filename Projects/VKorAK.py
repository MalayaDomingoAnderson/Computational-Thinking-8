# Beginning: create variables
VK_points = 0
AK_points = 0

# Middle: Ask questions
answer = input ("What type of color do you like most A) cold colors, or B) warm colors, or C) i like shades not colors")
if answer == "A":
    VK_points += 1
elif answer == "B":
    AK_points += 1
elif answer == "C":
    VK_points += 1


answer = input ("What do you describe yourself as A) Bad, or B) good, or C) half good half bad")
if answer == "A":
    VK_points += 1
elif answer == "B":
    AK_points += 1
elif answer == "C":
    AK_points += 1


answer = input ("Do you want to rule A) No, or B) yes or C) Idk")
if answer == "A":
    AK_points += 1
elif answer == "B":
    VK_points += 1
elif answer == "C":
    AK_points += 1


answer = input ("where would you rather live A) Auradon, or B) Isle of the lost")
if answer == "A":
    AK_points += 1
elif answer == "B":
    VK_points += 1


answer = input("do you wear gloves to school A)No, or B) yes")
if answer == "A":
    VK_points += 1
if answer == "B":
    AK_points += 1

# End: determine results
if VK_points > AK_points:
    print("you are a VK!")
elif AK_points > VK_points:
    print("you are a AK!")
elif AK_points -- VK_points:
    print("you are like mal and are both!")