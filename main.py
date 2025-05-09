import time

# define ANSI colors
yellow = "\033[1;33m"
green = "\033[1;32m"
red = "\033[1;31m"
cyan = "\033[36m"
reset = "\033[0m"

print(red + ("=-" * 30) + reset)
print(yellow + "YOU LOST YOUR WALLET!!!")
print(red + ("=-" * 30) + reset)

# story introduction
print(cyan + """\nYou were shopping at a busy street market in the heart of the city.
You're standing near three small market stalls, when suddenly...
You feel a strong push from someone in the crowd. As you check your pockets, you realize
your wallet is gone. YOU'VE BEEN ROBBED BY A PICKPOCKET! (unfortunately, not unusual in this area)
The thief must have hidden in one of the three stalls.\n""" + reset)

# create a notebook to store notes
notebook = []

# NPC dialogues
npc1 = "Fruit vendor James: I was just cutting some veggies, didn’t see anything."
npc2 = "Craftsman Alex: I was scrolling through TikTok, but I think Carlos and his son from the next stall might know something."
npc3 = "Shoemaker Carlos: I heard about the wallet. I asked my son and he said he saw someone running down the street."

# list of stalls
stalls = ["Fruit Stall", "Craft Stall", "Shoe Stall"]

# investigation loop
print(red + ("=-" * 30) + reset)
for stall in stalls:
    # investigate fruit stall
    if stall == "Fruit Stall":
        print(yellow + "\nLet’s start investigating at the fruit stall." + reset)
        print(cyan + npc1 + reset)
        note = input("\nNotebook: ")
        print(red + "Writing the note..." + reset)
        time.sleep(2)
        notebook.append(note)

    # investigate craft stall
    elif stall == "Craft Stall":
        print(yellow + "\nNow let's check out the craftsman." + reset)
        print(cyan + npc2 + reset)
        note = input("\nNotebook: ")
        print(red + "Writing the note..." + reset)
        time.sleep(2)
        notebook.append(note)

    # investigate shoe stall
    elif stall == "Shoe Stall":
        print(yellow + "\nTime to investigate the shoemaker and that kid in the Cyclone shirt." + reset)
        print(cyan + npc3 + reset)
        note = input("\nNotebook: ")
        print(red + "Writing the note...\n" + reset)
        time.sleep(2)
        notebook.append(note)

# suspect list
suspects = ["James", "Alex", "Carlos and his son"]
print(red + ("=-" * 30) + reset)
print(yellow + "YOUR NOTEBOOK:" + reset)
for entry in notebook:
    print(entry)

print(yellow + "SUSPECTS: " + reset)
for s in suspects:
    print(s)

print(red + ("=-" * 30) + reset)
guess = int(input("JAMES(1), ALEX(2), OR CARLOS AND HIS SON(3)? Who's the culprit?: "))

# check guess
if guess == 3:
    print(green + "You guessed correctly! Carlos's son returns your wallet and the thief is caught." + reset)
else:
    print(red + "You accused an innocent worker! You lost your wallet and got someone arrested unfairly." + reset)
