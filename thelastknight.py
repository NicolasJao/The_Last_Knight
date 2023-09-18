
import random as r

# Welcome to my Python CPT!
# The game I made is an RPG, with its main focus on combat and choose your own adventure.
# It is called "The Last Knight."
# This is how I set up the story aspect of the game: First it will print what is currently happening.
# Then it will give you a choice. Every choice is in a while loop, so that if the user doesn't
# pick a valid choice, it will keep repeating. Until you answer correctly, you move on. It's all linear.
# When you enter combat, the combat aspect of the game comes into play. You have to defeat the enemy in the while loop
# before moving on in the story. Beating the boss finishes the program as you win the game. If you die,
# make a wrong decision, or even simply take too long to do anything you lose as well XD

# *note* it may look messy, if I were to redo it I would clean
# everything up and put everything in functions using parameters
# as well as fix all the bugs XD

# I searched up and learned how to send string text to a new line in one print function
#                   |
#                   |
#                   \/
print("Welcome to...\n K \n N \n I \n G \n H \n T \n S")

print("You are a chlvalrous and esteemed cavalier from the kingdom of Talonia, by the name of...")
name = input("Enter a name: ")
print("..." + name + " the Great! You have fought evil brigands, bandits, and mercenaries all your life. You are an experienced fighter.")
print("But now... a mad warlord by the name of Macedon from a faraway land is threatening to ravage the kingdom.")
print("The King himself has tasked you with defeating the warlord.")

adventure = input("Are you ready to begin your adventure? (Yes or No) \n")
decisiontime = 0

while adventure != "yes" or adventure != "Yes" or adventure != "no" or adventure != "No":
    decisiontime += 1
    if adventure == "no" or adventure == "No":
        print("5 years later...")
        print("The evil warlord has devastated Talonia and has slain its king. Now it reigns the kingdom with terror.")
        print("Everyone you know is dead because of your decision to not help. Good job.")
        print("GAME OVER")
        exit()
    elif adventure == "yes" or adventure == "Yes":
        break
    else:
        print("Okay, but yes or no?")
        adventure = input()
    if decisiontime > 1:
        print("Due to your lack of decision-making skills, enough time has passed and Macedon has taken over Talonia.")
        print("GAME OVER")
        exit()

print("You start by going to the fortress city of Arundel. The city has not fallen in a thousand years.")
print("However, brigands of Macedon's army are threatening to capture it today.")
print("You must save the citizens and defeat them!")
print("ENEMIES APPROACHING: 3 BRIGANDS")

fightflee = input("Fight or Flee? \n")
decisiontime = 0

while fightflee != "fight" or fightflee != "Fight" or fightflee != "flee" or fightflee != "Flee":
    decisiontime += 1
    if fightflee == "flee" or fightflee == "Flee":
        print("You ride your horse fast, but the brigands are blocking all the ports of Arundel.")
        print("You get captured and killed.")
        print("GAME OVER")
        exit()
    elif fightflee == "fight" or fightflee == "Fight":
        break
    else:
        print("Okay, but fight or flee?")
        fightflee = input()
    if decisiontime > 1:
        print("You take forever to make a decision. The brigands kill you on the spot, thinking, 'What a pathetic knight.'")
        print("GAME OVER")
        exit()


# So here's the battle. Most of its parts and aspects are put into functions. I didn't put the battle itself
# into a function because of problems with variables and scopes. The first battle, here, has comments
# and notes on what happens each step of the battle.

# for the player: the first stat is dmg, the second stat is hit, the third stat is avo, the fourth stat is HP
# recap: dmg = damage, hit = strike chance, avo = avoidance rate, HP = health points
# *note* since there is no need for duplicate stats, the player's hit stat will act as the enemy's avo stat
# and the player's avo stat will act as the enemy's hit stat
# for the enemy: the first stat is minimum dmg, second stat is maximum dmg, third stat is placeholder so the
# fourth stat, health, can both be [3] and I won't get confused
playerstats = [0, 0, 0, 30]
enemystats = [0, 0, 0, 30]
maxhealth = 30
enemymaxhealth = 30
# playercrit = critical strike chance. Only accessible during the 'Defend' option in combat. Only the player has it.
playercrit = 0
playerdefending = False
defendturn = False

# Telling the user the stats of each weapon and giving them an option to pick one.
print("ENEMY ENCOUNTER! BRIGAND #1 \n These are the weapon choices for the battle:")
print("SWORD: 5 - 7 damage, 80% strike chance, 40% dodge chance")
print("AXE: 1 - 20 damage, 70% strike chance, 5% dodge chance")
print("LANCE: 3 - 10 damage, 100% strike chance, 10% dodge chance")
print("BOW: 6 - 9 damage, 65% strike chance, 75% dodge chance")
print("MAGIC: 10 - 15 damage, 50% strike chance, 65% dodge chance \n")
print("RANGED ATTACKS: You are far away, harder to hit. But the range impacts your strike chance.")
print("\n 1. Sword \n 2. Axe \n 3. Lance \n 4. Bow \n 5. Magic \n")
print("Choose the number of the weapon you want for this fight:")

# weapons = ["sword", "axe", "lance", "bow", "magic"]
# I learned how to do 2-D arrays from a friend who suggested it after I had a problem with the damage not generating
# a random number each attack, only each battle. They are basically lists in lists.
# weaponsdmg[0][0] refers to 5, and weaponsdmg[0][1] refers to 7, and so on
#               |
#               |
#               \/
weaponsdmg = [[5, 7], [1, 20], [3, 10], [6, 9], [10, 15]] # first number is minimum dmg, second number is maximum dmg
weaponshit = [80, 70, 100, 65, 50]
weaponsavo = [40, 5, 10, 75, 65]

sword = weaponsdmg[0], weaponshit[0], weaponsavo[0] # I learned in coding club last year how to select specific items in a list
axe = weaponsdmg[1], weaponshit[1], weaponsavo[1]   # I also learned that the first item in a list is 0, not 1
lance = weaponsdmg[2], weaponshit[2], weaponsavo[2] # kind of like RGB in CSS, the first value is 0, not 1
bow = weaponsdmg[3], weaponshit[3], weaponsavo[3]   # also kind of like the range function, where if you put a single
magic = weaponsdmg[4], weaponshit[4], weaponsavo[4] # value, the first value in the range is 0.


# Choosing a weapon before a battle

def playerweapon():
    # the global statement allows the variable to be altered in any scope, scopes being kind of like the "realm"
    # a variable is in, and they can only be tinkered with within the same realm
    # global puts the variable on the global scope, allowed to be altered within functions such as now
    global playerstats
    for tries in range(5):
        choice = (input())
        if choice == "1":
            print("You chose sword!")
            playerstats = [sword[0], sword[1], sword[2], playerstats[3]]
            break
        elif choice == "2":
            print("You chose axe!")
            playerstats = [axe[0], axe[1], axe[2], playerstats[3]]
            break
        elif choice == "3":
            print("You chose lance!")
            playerstats = [lance[0], lance[1], lance[2], playerstats[3]]
            break
        elif choice == "4":
            print("You chose bow!")
            playerstats = [bow[0], bow[1], bow[2], playerstats[3]]
            break
        elif choice == "5":
            print("You chose magic!")
            playerstats = [magic[0], magic[1], magic[2], playerstats[3]]
            break
        else:
            if tries != 4:
                print("Not a weapon option. Try again.")
        if tries == 4:
            print("You took too long to choose a weapon.")
            print("You stand there uselessly, and the enemies kill you on the spot.")
            print("GAME OVER")
        # I searched up how to stop a running program when needed. I learned about the exit() function.
        # I will use this every time the user gets a GAME OVER. Only one life in this game :)
        #     |
        #     |
        #     \/
            exit()


# This is what you'll say during an attack.

def bcry():
    battlecrychoice = r.randint(1, 7)
    if battlecrychoice == 1:
        return "YAAAAAAA!"
    elif battlecrychoice == 2:
        return "RGAAAAAAAGHH!"
    elif battlecrychoice == 3:
        return "For His Majesty!"
    elif battlecrychoice == 4:
        return "Justice is served!"
    elif battlecrychoice == 5:
        return "Talonia is ours!"
    elif battlecrychoice == 6:
        return "I'll hit you where it hurts!"
    elif battlecrychoice == 7:
        return "Evil has no place in this world!"
    else:
        print("Uh, something went wrong.")
#                   /\
#                   |
#                   |
# This is simply an error check, for if any reason the random number generated isn't within the range,
# it will tell you with this message.


# This is what will be said when you miss an attack.

def missmessage():
    missmessagechoice = r.randint(1, 3)
    if missmessagechoice == 1:
        return "You missed!"
    elif missmessagechoice == 2:
        return "You were too slow!"
    elif missmessagechoice == 3:
        return "The enemy dodged!"
    else:
        return "Uh, something went wrong."


# This is what weapon the enemy will pick during a battle.
# some weapon stats are customarily changed for enemies for more friendliness

def enemyweapon():
    enemyweaponchoice = r.randint(1, 3)
    if enemyweaponchoice == 1:
        enemystats[0] += 5
        enemystats[1] += 7
        return "The enemy chose sword!"
    elif enemyweaponchoice == 2:
        enemystats[0] += 1
        enemystats[1] += 15
        return "The enemy chose axe!"
    elif enemyweaponchoice == 3:
        enemystats[0] += 3
        enemystats[1] += 10
        return "The enemy chose lance!"
    else:
        return "Uh, something went wrong."


# This is everything that goes on when you or the enemy picks heal. To make the game more friendly,
# the chance of getting a good heal option for the user is increased, and the chances for
# worse healing options for the enemy is increased. Also, it is a rarity for the enemy to heal.

def healoption(user):
    healoptionchoice = r.randint(1, 4)
    if playerstats[3] < maxhealth or enemystats[3] < enemymaxhealth:
        if user == "player":
            if healoptionchoice == 1:
                print("You chose concoction elixir!")
                if playerstats[3] + 5 > maxhealth:
                    playerstats[3] = maxhealth
                else:
                    playerstats[3] += 5
            elif healoptionchoice == 2 or healoptionchoice == 3:
                print("You chose healing magic!")
                if playerstats[3] + 10 > maxhealth:
                    playerstats[3] = maxhealth
                else:
                    playerstats[3] += 10
            elif healoptionchoice == 4:
                print("You chose bandage!")
                if playerstats[3] + 1 > maxhealth:
                    playerstats[3] = maxhealth
                else:
                    playerstats[3] += 1
        elif user == "enemy":
            if healoptionchoice == 1:
                print("The enemy chose concoction elixir!")
                if enemystats[3] + 5 > enemymaxhealth:
                    enemystats[3] = enemymaxhealth
                else:
                    enemystats[3] += 5
            elif healoptionchoice == 2:
                print("The enemy chose healing magic!")
                if enemystats[3] + 10 > enemymaxhealth:
                    enemystats[3] = enemymaxhealth
                else:
                    enemystats[3] += 10
            elif healoptionchoice == 3 or healoptionchoice == 4:
                print("The enemy chose bandage!")
                if enemystats[3] + 1 > enemymaxhealth:
                    enemystats[3] = enemymaxhealth
                else:
                    enemystats[3] += 1
        elif user == "boss":
            if healoptionchoice == 1:
                print("The enemy chose concoction elixir!")
                if enemystats[3] + 100 > enemymaxhealth:
                    enemystats[3] = enemymaxhealth
                else:
                    enemystats[3] += 100
            elif healoptionchoice == 2 or healoptionchoice == 3:
                print("The enemy chose healing magic!")
                if enemystats[3] + 200 > enemymaxhealth:
                    enemystats[3] = enemymaxhealth
                else:
                    enemystats[3] += 200
            elif healoptionchoice == 4:
                print("The enemy chose bandage!")
                if enemystats[3] + 5 > enemymaxhealth:
                    enemystats[3] = enemymaxhealth
                else:
                    enemystats[3] += 5
        else:
            return "Uh, something went wrong."
    else:
        print("You are at max HP!")


# This is everything that goes on during a defending turn. Defending is basically sacrificing or waiting a turn
# so your next one will be stronger.

def defend():
    global playercrit
    global playerdefending
    global defendturn
    playerdefending = True
    defendturn = True
    playerstats[0][0] += 10
    playerstats[0][1] += 10
    playerstats[1] += 20
    playercrit += 35


# The effects of a critical strike.

def criticalstrike():
    crit = r.randint(1, 100)
    if crit in range(playercrit):
        print("CRITICAL STRIKE!")
        global dmg
        dmg *= 2


# The player picking a weapon

playerweapon()

# The enemy picking a weapon

print(enemyweapon())

print("\n FIGHT! \n")
print("Battle Tactics:")
print("Attack: Deal damage with your weapon if it connects.")
print("Defend: Wait a turn. On your next turn, gain 10 dmg, 20 hit, 35 crit. Stacks every turn you do it.")
print("Heal: Randomly choose a concoction elixir, healing magic, or bandage to treat your wounds. \n")

# This is the actual fight. While your health and the enemy health is greater than 0, the battle continues.

while playerstats[3] > 0 and enemystats[3] > 0:
    print("Your HP:", playerstats[3])
    print("Enemy HP:", enemystats[3])
    print("It's your turn! Choose Attack, Defend, or Heal.")
    turnchoice = input()
    if turnchoice == "attack" or turnchoice == "Attack":
        print("You chose attack!")
        print('"' + bcry() + '" you say.')
        hit = r.randint(1, 100)
        if hit in range(playerstats[1]):
            dmg = r.randint(playerstats[0][0], playerstats[0][1])
            criticalstrike()
            enemystats[3] -= dmg
            print("You dealt", dmg, "damage!")
            if enemystats[3] <= 0:
                print("Victory!")
                break
        elif hit not in range(playerstats[1]):
            print(missmessage())
        else:
            print("Uh, something went wrong.")
        print("Your HP:", playerstats[3])
        print("Enemy HP:", enemystats[3])
    elif turnchoice == "defend" or turnchoice == "Defend":
        print("You are defending!")
        defend()
    elif turnchoice == "heal" or turnchoice == "Heal":
        print("You chose heal!")
        healoption("player")
        print("Your HP:", playerstats[3])
        print("Enemy HP:", enemystats[3])
    else:
        print("You didn't choose an option!")

    input("Press enter. \n")# This is simply to allow the user to command when the enemy attacks, so the screen doesn't
                            # look jumbled with messy text to read, and it comes in groups

    # reversing the effects of defend
    if playerdefending and not defendturn:
        playerstats[0][0] -= 10
        playerstats[0][1] -= 10
        playerstats[1] -= 20
        playercrit -= 35
        playerdefending = False
    print("It's the enemy's turn!")
    enemyturnchoice = r.randint(1, 15) # enemies won't have the option to defend, and healing will be a rarity
    if enemyturnchoice < 15:
        enemyhit = r.randint(1, 100)
        if enemyhit not in range(playerstats[2]):
            print("The enemy attacked!")
            enemydmg = r.randint(enemystats[0], enemystats[1])
            playerstats[3] -= enemydmg
            print("You took", enemydmg, "damage!")
            if playerstats[3] <= 0:
                print("You were defeated!")
                print("GAME OVER")
                exit()
        elif enemyhit in range(playerstats[2]):
            print("The enemy attacked!")
            print("You dodged!")
    elif enemyturnchoice == 15:
        if enemystats[3] < 30:
            print("The enemy chose heal!")
            healoption("enemy")
    else:
        print("Uh, something went wrong.")
    if defendturn:
        defendturn = False

input("Press enter to continue. \n")

print("ENEMY ENCOUNTER! BRIGAND #2 \n These are the weapon choices for the battle:")
print("SWORD: 5 - 7 damage, 80% strike chance, 40% dodge chance")
print("AXE: 1 - 20 damage, 70% strike chance, 5% dodge chance")
print("LANCE: 3 - 10 damage, 100% strike chance, 10% dodge chance")
print("BOW: 6 - 9 damage, 65% strike chance, 75% dodge chance")
print("MAGIC: 10 - 15 damage, 50% strike chance, 65% dodge chance")
print("\n 1. Sword \n 2. Axe \n 3. Lance \n 4. Bow \n 5. Magic \n")
print("Choose the number of the weapon you want for this fight:")

playerstats = [0, 0, 0, 30]
enemystats = [0, 0, 0, 35]
playercrit = 0
maxhealth = 30
enemymaxhealth = 35
playerdefending = False
defendturn = False

weaponsdmg = [[5, 7], [1, 20], [3, 10], [6, 9], [10, 15]]
weaponshit = [80, 70, 100, 65, 50]
weaponsavo = [40, 5, 10, 75, 65]

sword = weaponsdmg[0], weaponshit[0], weaponsavo[0]
axe = weaponsdmg[1], weaponshit[1], weaponsavo[1]
lance = weaponsdmg[2], weaponshit[2], weaponsavo[2]
bow = weaponsdmg[3], weaponshit[3], weaponsavo[3]
magic = weaponsdmg[4], weaponshit[4], weaponsavo[4]

playerweapon()

print(enemyweapon())

print("\n FIGHT! \n")

while playerstats[3] > 0 and enemystats[3] > 0:
    print("Your HP:", playerstats[3])
    print("Enemy HP:", enemystats[3])
    print("It's your turn! Choose Attack, Defend, or Heal.")
    turnchoice = input()
    if turnchoice == "attack" or turnchoice == "Attack":
        print("You chose attack!")
        print('"' + bcry() + '" you say.')
        hit = r.randint(1, 100)
        if hit in range(playerstats[1]):
            dmg = r.randint(playerstats[0][0], playerstats[0][1])
            criticalstrike()
            enemystats[3] -= dmg
            print("You dealt", dmg, "damage!")
            if enemystats[3] <= 0:
                print("Victory!")
                break
        elif hit not in range(playerstats[1]):
            print(missmessage())
            print("Your HP:", playerstats[3])
            print("Enemy HP:", enemystats[3])
        else:
            print("Uh, something went wrong.")
        print("Your HP:", playerstats[3])
        print("Enemy HP:", enemystats[3])
    elif turnchoice == "defend" or turnchoice == "Defend":
        print("You are defending!")
        defend()
    elif turnchoice == "heal" or turnchoice == "Heal":
        print("You chose heal!")
        healoption("player")
        print("Your HP:", playerstats[3])
        print("Enemy HP:", enemystats[3])
    else:
        print("You didn't choose an option!")

    input("Press enter. \n")

    if playerdefending and not defendturn:
        playerstats[0][0] -= 10
        playerstats[0][1] -= 10
        playerstats[1] -= 20
        playercrit -= 35
        playerdefending = False
    print("It's the enemy's turn!")
    enemyturnchoice = r.randint(1, 15)
    if enemyturnchoice < 15:
        enemyhit = r.randint(1, 100)
        if enemyhit not in range(playerstats[2]):
            print("The enemy attacked!")
            enemydmg = r.randint(enemystats[0], enemystats[1])
            playerstats[3] -= enemydmg
            print("You took", enemydmg, "damage!")
            if playerstats[3] <= 0:
                print("You were defeated!")
                print("GAME OVER")
                exit()
        elif enemyhit in range(playerstats[2]):
            print("The enemy attacked!")
            print("You dodged!")
    elif enemyturnchoice == 15:
        if enemystats[3] < enemymaxhealth:
            print("The enemy chose heal!")
            healoption("enemy")
    else:
        print("Uh, something went wrong.")
    if defendturn:
        defendturn = False

input("Press enter to continue. \n")

print("ENEMY ENCOUNTER! BRIGAND #3 \n These are the weapon choices for the battle:")
print("SWORD: 5 - 7 damage, 80% strike chance, 40% dodge chance")
print("AXE: 1 - 20 damage, 70% strike chance, 5% dodge chance")
print("LANCE: 3 - 10 damage, 100% strike chance, 10% dodge chance")
print("BOW: 6 - 9 damage, 65% strike chance, 75% dodge chance")
print("MAGIC: 10 - 15 damage, 50% strike chance, 65% dodge chance")
print("\n 1. Sword \n 2. Axe \n 3. Lance \n 4. Bow \n 5. Magic \n")
print("Choose the number of the weapon you want for this fight:")

playerstats = [0, 0, 0, 30]
enemystats = [0, 0, 0, 40]
playercrit = 0
maxhealth = 30
enemymaxhealth = 40
playerdefending = False
defendturn = False

weaponsdmg = [[5, 7], [1, 20], [3, 10], [6, 9], [10, 15]]
weaponshit = [80, 70, 100, 65, 50]
weaponsavo = [40, 5, 10, 75, 65]

sword = weaponsdmg[0], weaponshit[0], weaponsavo[0]
axe = weaponsdmg[1], weaponshit[1], weaponsavo[1]
lance = weaponsdmg[2], weaponshit[2], weaponsavo[2]
bow = weaponsdmg[3], weaponshit[3], weaponsavo[3]
magic = weaponsdmg[4], weaponshit[4], weaponsavo[4]

playerweapon()

print(enemyweapon())

print("\n FIGHT! \n")

while playerstats[3] > 0 and enemystats[3] > 0:
    print("Your HP:", playerstats[3])
    print("Enemy HP:", enemystats[3])
    print("It's your turn! Choose Attack, Defend, or Heal.")
    turnchoice = input()
    if turnchoice == "attack" or turnchoice == "Attack":
        print("You chose attack!")
        print('"' + bcry() + '" you say.')
        hit = r.randint(1, 100)
        if hit in range(playerstats[1]):
            dmg = r.randint(playerstats[0][0], playerstats[0][1])
            criticalstrike()
            enemystats[3] -= dmg
            print("You dealt", dmg, "damage!")
            if enemystats[3] <= 0:
                print("Victory!")
                break
        elif hit not in range(playerstats[1]):
            print(missmessage())
            print("Your HP:", playerstats[3])
            print("Enemy HP:", enemystats[3])
        else:
            print("Uh, something went wrong.")
        print("Your HP:", playerstats[3])
        print("Enemy HP:", enemystats[3])
    elif turnchoice == "defend" or turnchoice == "Defend":
        print("You are defending!")
        defend()
    elif turnchoice == "heal" or turnchoice == "Heal":
        print("You chose heal!")
        healoption("player")
        print("Your HP:", playerstats[3])
        print("Enemy HP:", enemystats[3])
    else:
        print("You didn't choose an option!")

    input("Press enter. \n")

    if playerdefending and not defendturn:
        playerstats[0][0] -= 10
        playerstats[0][1] -= 10
        playerstats[1] -= 20
        playercrit -= 35
        playerdefending = False
    print("It's the enemy's turn!")
    enemyturnchoice = r.randint(1, 15)
    if enemyturnchoice < 15:
        enemyhit = r.randint(1, 100)
        if enemyhit not in range(playerstats[2]):
            print("The enemy attacked!")
            enemydmg = r.randint(enemystats[0], enemystats[1])
            playerstats[3] -= enemydmg
            print("You took", enemydmg, "damage!")
            if playerstats[3] <= 0:
                print("You were defeated!")
                print("GAME OVER")
                exit()
        elif enemyhit in range(playerstats[2]):
            print("The enemy attacked!")
            print("You dodged!")
    elif enemyturnchoice == 15:
        if enemystats[3] < enemymaxhealth:
            print("The enemy chose heal!")
            healoption("enemy")
    else:
        print("Uh, something went wrong.")
    if defendturn:
        defendturn = False

input("Press enter to continue. \n")

print("The brigands were tough, but you managed to defeat them with the help of other knights and militia.")
print('Suddenly, a commoner yells, "Reinforcements coming!"')
print("'What?' you think. You look past the city gates to see a colossal army of cavaliers coming over the hill.")
print("Their horses create a dust cloud big enough to block the sun for days.")
print("You dread the thought of fighting that many, but you are brave. You yell at everyone to get ready.")
print("What will you do?")
print("ENEMIES APPROACHING: 200 CAVALIERS")

fightflee = input("Fight or Flee? \n")
decisiontime = 0

while fightflee != "fight" or fightflee != "Fight" or fightflee != "flee" or fightflee != "Flee":
    decisiontime += 1
    if fightflee == "fight" or fightflee == "Fight":
        print('You will die with honor! "FOR HIS MAJESTY!" you yell at the top of your lungs.')
        print("The battle cries and cheers of everyone around you ensue.")
        print("However, the sheer number of cavaliers destroy you and your makeshift army.")
        print("Each one you charge at, there are five more right behind.")
        print("You feel about ten lances pierce you before the world blacks out and darkness claims you.")
        print("GAME OVER")
        exit()
    elif fightflee == "flee" or fightflee == "Flee":
        break
    else:
        print("Okay, but fight or flee?")
        fightflee = input()
    if decisiontime > 1:
        print("You take forever to make a decision.")
        print("You look dumb standing there as Macedon's cavaliers strike you down with their lances.")
        print("GAME OVER")
        exit()

print("You made the right decision to flee. You are no coward, but you are also no madman.")
print("You secretly ride your horse to a port and quickly steal a ship.")
print("Your instincts override your promised code of chivalry. If you don't survive, who else will defeat Macedon?")
print("As you leave Arundel into the sea, you look back at the burning city.")
print("The city that has bested bandits for a thousand years. Now, it falls today.")
print("BOOM! Your ears pop as you see a million beams of light ascend from the heavens, raining on the city.")
print("They destroy everything in it completely, obliterating it to pieces. Now you understand.")
print("It was all Macedon's plan! He caused a distraction in Arundel to attract all the King's knights.")
print("And then his dark mages casted a powerful spell that would kill every soul in it.")
print("You realize with sorrow that Arundel was doomed from the start.")
print("You also realize that because of your selfish choice to flee, you are the only knight left.")
print("Even the King must think you're dead. Now you must make a decision.")
print("Continue your journey to the Rift of Heavens (Yes), or depressingly drift into the infinite sea? (No)")

adventure = input("(Yes or No) \n")
decisiontime = 0

while adventure != "yes" or adventure != "Yes" or adventure != "no" or adventure != "No":
    decisiontime += 1
    if adventure == "no" or adventure == "No":
        print("You sail endlessly without a purpose left in life.")
        print("Eventually, a kraken sinks your ship with a single tentacle and you sink into the bottomless depths.")
        print("GAME OVER")
        exit()
    elif adventure == "yes" or adventure == "Yes":
        break
    else:
        print("Okay, but yes or no?")
        adventure = input()
    if decisiontime > 1:
        print("Your decision-making skills are not present.")
        print("As you take your time thinking, a kraken appears out of nowhere and sinks your ship.")
        print("GAME OVER")
        exit()

print("To defeat Macedon, a powerful warlord, you need a powerful weapon.")
print("You need the legendary rapier sword Arianrhod, a sword so sharp they say it can cleave the heavens itself.")
print("Arianrhod rests in the ruins of a ghost city founded on floating islands, called Fgyrnogrm.")
print("The only way to Fgyrnogrm is a portal in the middle of the Driatic Sea, in the Thrysus Canal.")
print("The portal is called the Rift of Heavens. You sail towards it now.")
print("The winds blow viciously, and the waves aren't calm. Thunder booms in the distance.")
print("You also know the Thrysus Canal is teeming with pirates. You prepare for anything.")
print("BOOM! A cannonball strikes your ship. Go figure. A black-flagged ship had sneaked up behind you.")
print("Pirates swing on their ropes to capture you. They do so in minutes. You are bound in ropes.")
print('"Food for the rest of the week! Har har!" one says. The others cheer.')
print('You know pirates have too much pride. "If I can beat your captain, I will be extra juicy," you say.')
print("Fighting one captain is always better than an entire crew.")
print("The captain shows himself. He is a rotten-smelling old hunk, but looks tough.")
print('"Bring it on," he snarls.')
print("ENEMIES APPROACHING: 1 PIRATE CAPTAIN")

input("Press enter to continue. \n")

print("ENEMY ENCOUNTER! PIRATE CAPTAIN \n These are the weapon choices for the battle:")
print("SWORD: 5 - 7 damage, 80% strike chance, 40% dodge chance")
print("AXE: 1 - 20 damage, 70% strike chance, 5% dodge chance")
print("LANCE: 3 - 10 damage, 100% strike chance, 10% dodge chance")
print("BOW: 6 - 9 damage, 65% strike chance, 75% dodge chance")
print("MAGIC: 10 - 15 damage, 50% strike chance, 65% dodge chance")
print("\n 1. Sword \n 2. Axe \n 3. Lance \n 4. Bow \n 5. Magic \n")
print("Choose the number of the weapon you want for this fight:")

playerstats = [0, 0, 0, 30]
enemystats = [9, 11, 0, 60]
playercrit = 0
maxhealth = 30
enemymaxhealth = 60
playerdefending = False
defendturn = False

weaponsdmg = [[5, 7], [1, 20], [3, 10], [6, 9], [10, 15]]
weaponshit = [80, 70, 100, 65, 50]
weaponsavo = [40, 5, 10, 75, 65]

sword = weaponsdmg[0], weaponshit[0], weaponsavo[0]
axe = weaponsdmg[1], weaponshit[1], weaponsavo[1]
lance = weaponsdmg[2], weaponshit[2], weaponsavo[2]
bow = weaponsdmg[3], weaponshit[3], weaponsavo[3]
magic = weaponsdmg[4], weaponshit[4], weaponsavo[4]

playerweapon()

print("The enemy chose cutlass!")

print("\n FIGHT! \n")

while playerstats[3] > 0 and enemystats[3] > 0:
    print("Your HP:", playerstats[3])
    print("Enemy HP:", enemystats[3])
    print("It's your turn! Choose Attack, Defend, or Heal.")
    turnchoice = input()
    if turnchoice == "attack" or turnchoice == "Attack":
        print("You chose attack!")
        print('"' + bcry() + '" you say.')
        hit = r.randint(1, 100)
        if hit in range(playerstats[1]):
            dmg = r.randint(playerstats[0][0], playerstats[0][1])
            criticalstrike()
            enemystats[3] -= dmg
            print("You dealt", dmg, "damage!")
            if enemystats[3] <= 0:
                print("Victory!")
                break
        elif hit not in range(playerstats[1]):
            print(missmessage())
            print("Your HP:", playerstats[3])
            print("Enemy HP:", enemystats[3])
        else:
            print("Uh, something went wrong.")
        print("Your HP:", playerstats[3])
        print("Enemy HP:", enemystats[3])
    elif turnchoice == "defend" or turnchoice == "Defend":
        print("You are defending!")
        defend()
    elif turnchoice == "heal" or turnchoice == "Heal":
        print("You chose heal!")
        healoption("player")
        print("Your HP:", playerstats[3])
        print("Enemy HP:", enemystats[3])
    else:
        print("You didn't choose an option!")

    input("Press enter. \n")

    if playerdefending and not defendturn:
        playerstats[0][0] -= 10
        playerstats[0][1] -= 10
        playerstats[1] -= 20
        playercrit -= 35
        playerdefending = False
    print("It's the enemy's turn!")
    enemyturnchoice = r.randint(1, 15)
    if enemyturnchoice < 15:
        enemyhit = r.randint(1, 100)
        if enemyhit not in range(playerstats[2]):
            print("The enemy attacked!")
            enemydmg = r.randint(enemystats[0], enemystats[1])
            playerstats[3] -= enemydmg
            print("You took", enemydmg, "damage!")
            if playerstats[3] <= 0:
                print("You were defeated!")
                print("GAME OVER")
                exit()
        elif enemyhit in range(playerstats[2]):
            print("The enemy attacked!")
            print("You dodged!")
    elif enemyturnchoice == 15:
        if enemystats[3] < enemymaxhealth:
            print("The enemy chose heal!")
            healoption("enemy")
    else:
        print("Uh, something went wrong.")
    if defendturn:
        defendturn = False

input("Press enter to continue. \n")

print("The pirate crew is shocked at the defeat of their captain!")
print("They pledge their allegiance to you. However, you only want their loot.")
print("You fancy yourself a sturdy cutlass, some flintlock pistols, and expensive golden armour from their ship hold.")
print("You get back to your ship and continue sailing the Thrysus Canal.")
print("You safely make it to the Rift of Heavens. You arrive at the floating islands of Fgyrnogrm.")
print("You see a dark fortress in the distance, where Arianrhod lies.")
print("You can either get there by foot, on the rotting and old wooden bridges between islands...")
print("...or try to find Pagalion, the legendary pegasus that can get you there fast and easy.")
print("Go for Pagalion?")

adventure = input("(Yes or No) \n")
decisiontime = 0

while adventure != "yes" or adventure != "Yes" or adventure != "no" or adventure != "No":
    decisiontime += 1
    if adventure == "no" or adventure == "No":
        print("You make your way to the ominous fortress, passing long bridges suspended between floating rocks in the sky.")
        print("Unfortunately, centuries of weather has worn them down. One of your steps causes the planks to break.")
        print("You fall out of the sky, a meteor heading toward ground at terminal velocity.")
        print("Meeting your inevitable doom.")
        print("GAME OVER")
        exit()
    elif adventure == "yes" or adventure == "Yes":
        break
    else:
        print("Okay, but yes or no?")
        adventure = input()
    if decisiontime > 1:
        print("Due to your lack of decision-making skills, enough time has passed and Macedon has taken over Talonia.")
        print("GAME OVER")
        exit()

print("You find the pegasus resting in a blissful meadow.")
print("It is a challenge to tame the mighty steed, but you are a worthy hero. It accepts you.")
print("You fly to the dark fortress. You enter its gates. The sword is in the throne room.")
print("As you arrive there, you are met with a dark cult already performing a ritual to try to get it out of its rock.")
print("You recognize their robes. They are Macedon's dark mages.")
print("The same ones that must have casted the spell to destroy Arundel! You must end them here.")
print("ENEMIES APPROACHING: 3 DARK MAGES")

input("Press enter to continue. \n")

print("ENEMY ENCOUNTER! DARK MAGE #1 \n These are the weapon choices for the battle:")
print("GOLDEN CUTLASS: 8 - 12 damage, 85% strike chance, 45% dodge chance")
print("AXE: 1 - 20 damage, 70% strike chance, 5% dodge chance")
print("LANCE: 3 - 10 damage, 100% strike chance, 10% dodge chance")
print("FLINTLOCK PISTOLS: 7 - 9 damage, 70% strike chance, 70% dodge chance")
print("MAGIC: 1 - 2 damage, 50% strike chance, 65% dodge chance \n")
print("ENEMY RESISTANCE: Mages are experts at magic. They also know how to counter it.")
print("\n 1. Golden Cutlass \n 2. Axe \n 3. Lance \n 4. Flintlock Pistols \n 5. Magic \n")
print("Choose the number of the weapon you want for this fight:")

playerstats = [0, 0, 0, 50]
enemystats = [10, 11, 0, 50]
playercrit = 0
maxhealth = 50
enemymaxhealth = 50
playerdefending = False
defendturn = False

weaponsdmg = [[8, 12], [1, 20], [3, 10], [7, 9], [1, 2]]
weaponshit = [85, 70, 100, 70, 50]
weaponsavo = [45, 5, 10, 70, 65]

sword = weaponsdmg[0], weaponshit[0], weaponsavo[0]
axe = weaponsdmg[1], weaponshit[1], weaponsavo[1]
lance = weaponsdmg[2], weaponshit[2], weaponsavo[2]
bow = weaponsdmg[3], weaponshit[3], weaponsavo[3]
magic = weaponsdmg[4], weaponshit[4], weaponsavo[4]

for tries in range(5):
    choice = (input())
    if choice == "1":
        print("You chose Golden Cutlass!")
        playerstats = [sword[0], sword[1], sword[2], playerstats[3]]
        break
    elif choice == "2":
        print("You chose axe!")
        playerstats = [axe[0], axe[1], axe[2], playerstats[3]]
        break
    elif choice == "3":
        print("You chose lance!")
        playerstats = [lance[0], lance[1], lance[2], playerstats[3]]
        break
    elif choice == "4":
        print("You chose Flintlock Pistols!")
        playerstats = [bow[0], bow[1], bow[2], playerstats[3]]
        break
    elif choice == "5":
        print("You chose magic!")
        playerstats = [magic[0], magic[1], magic[2], playerstats[3]]
        break
    else:
        if tries != 4:
            print("Not a weapon option. Try again.")
    if tries == 4:
        print("You took too long to choose a weapon.")
        print("You stand there uselessly, and the enemies kill you on the spot.")
        print("GAME OVER")
        exit()

print("The enemy chose dark cultist magic! Such heresy!")

print("\n FIGHT! \n")

while playerstats[3] > 0 and enemystats[3] > 0:
    print("Your HP:", playerstats[3])
    print("Enemy HP:", enemystats[3])
    print("It's your turn! Choose Attack, Defend, or Heal.")
    turnchoice = input()
    if turnchoice == "attack" or turnchoice == "Attack":
        print("You chose attack!")
        print('"' + bcry() + '" you say.')
        hit = r.randint(1, 100)
        if hit in range(playerstats[1]):
            dmg = r.randint(playerstats[0][0], playerstats[0][1])
            criticalstrike()
            enemystats[3] -= dmg
            print("You dealt", dmg, "damage!")
            if enemystats[3] <= 0:
                print("Victory!")
                break
        elif hit not in range(playerstats[1]):
            print(missmessage())
            print("Your HP:", playerstats[3])
            print("Enemy HP:", enemystats[3])
        else:
            print("Uh, something went wrong.")
        print("Your HP:", playerstats[3])
        print("Enemy HP:", enemystats[3])
    elif turnchoice == "defend" or turnchoice == "Defend":
        print("You are defending!")
        defend()
    elif turnchoice == "heal" or turnchoice == "Heal":
        print("You chose heal!")
        healoption("player")
        print("Your HP:", playerstats[3])
        print("Enemy HP:", enemystats[3])
    else:
        print("You didn't choose an option!")

    input("Press enter. \n")

    if playerdefending and not defendturn:
        playerstats[0][0] -= 10
        playerstats[0][1] -= 10
        playerstats[1] -= 20
        playercrit -= 35
        playerdefending = False
    print("It's the enemy's turn!")
    enemyturnchoice = r.randint(1, 15)
    if enemyturnchoice < 15:
        enemyhit = r.randint(1, 100)
        if enemyhit not in range(playerstats[2]):
            print("The enemy attacked!")
            enemydmg = r.randint(enemystats[0], enemystats[1])
            playerstats[3] -= enemydmg
            print("You took", enemydmg, "damage!")
            if playerstats[3] <= 0:
                print("You were defeated!")
                print("GAME OVER")
                exit()
        elif enemyhit in range(playerstats[2]):
            print("The enemy attacked!")
            print("You dodged!")
    elif enemyturnchoice == 15:
        if enemystats[3] < enemymaxhealth:
            print("The enemy chose heal!")
            healoption("enemy")
    else:
        print("Uh, something went wrong.")
    if defendturn:
        defendturn = False

input("Press enter to continue. \n")

print("ENEMY ENCOUNTER! DARK MAGE #2 \n These are the weapon choices for the battle:")
print("GOLDEN CUTLASS: 8 - 12 damage, 85% strike chance, 45% dodge chance")
print("AXE: 1 - 20 damage, 70% strike chance, 5% dodge chance")
print("LANCE: 3 - 10 damage, 100% strike chance, 10% dodge chance")
print("FLINTLOCK PISTOLS: 7 - 9 damage, 70% strike chance, 70% dodge chance")
print("MAGIC: 1 - 2 damage, 50% strike chance, 65% dodge chance")
print("\n 1. Golden Cutlass \n 2. Axe \n 3. Lance \n 4. Flintlock Pistols \n 5. Magic \n")
print("Choose the number of the weapon you want for this fight:")

playerstats = [0, 0, 0, 50]
enemystats = [12, 13, 0, 55]
playercrit = 0
maxhealth = 50
enemymaxhealth = 55
playerdefending = False
defendturn = False

weaponsdmg = [[8, 12], [1, 20], [3, 10], [7, 9], [1, 2]]
weaponshit = [85, 70, 100, 70, 50]
weaponsavo = [45, 5, 10, 70, 65]

sword = weaponsdmg[0], weaponshit[0], weaponsavo[0]
axe = weaponsdmg[1], weaponshit[1], weaponsavo[1]
lance = weaponsdmg[2], weaponshit[2], weaponsavo[2]
bow = weaponsdmg[3], weaponshit[3], weaponsavo[3]
magic = weaponsdmg[4], weaponshit[4], weaponsavo[4]

for tries in range(5):
    choice = (input())
    if choice == "1":
        print("You chose Golden Cutlass!")
        playerstats = [sword[0], sword[1], sword[2], playerstats[3]]
        break
    elif choice == "2":
        print("You chose axe!")
        playerstats = [axe[0], axe[1], axe[2], playerstats[3]]
        break
    elif choice == "3":
        print("You chose lance!")
        playerstats = [lance[0], lance[1], lance[2], playerstats[3]]
        break
    elif choice == "4":
        print("You chose Flintlock Pistols!")
        playerstats = [bow[0], bow[1], bow[2], playerstats[3]]
        break
    elif choice == "5":
        print("You chose magic!")
        playerstats = [magic[0], magic[1], magic[2], playerstats[3]]
        break
    else:
        if tries != 4:
            print("Not a weapon option. Try again.")
    if tries == 4:
        print("You took too long to choose a weapon.")
        print("You stand there uselessly, and the enemies kill you on the spot.")
        print("GAME OVER")
        exit()

print("The enemy chose endless void magic! You feel warped and distorted.")

print("\n FIGHT! \n")

while playerstats[3] > 0 and enemystats[3] > 0:
    print("Your HP:", playerstats[3])
    print("Enemy HP:", enemystats[3])
    print("It's your turn! Choose Attack, Defend, or Heal.")
    turnchoice = input()
    if turnchoice == "attack" or turnchoice == "Attack":
        print("You chose attack!")
        print('"' + bcry() + '" you say.')
        hit = r.randint(1, 100)
        if hit in range(playerstats[1]):
            dmg = r.randint(playerstats[0][0], playerstats[0][1])
            criticalstrike()
            enemystats[3] -= dmg
            print("You dealt", dmg, "damage!")
            if enemystats[3] <= 0:
                print("Victory!")
                break
        elif hit not in range(playerstats[1]):
            print(missmessage())
            print("Your HP:", playerstats[3])
            print("Enemy HP:", enemystats[3])
        else:
            print("Uh, something went wrong.")
        print("Your HP:", playerstats[3])
        print("Enemy HP:", enemystats[3])
    elif turnchoice == "defend" or turnchoice == "Defend":
        print("You are defending!")
        defend()
    elif turnchoice == "heal" or turnchoice == "Heal":
        print("You chose heal!")
        healoption("player")
        print("Your HP:", playerstats[3])
        print("Enemy HP:", enemystats[3])
    else:
        print("You didn't choose an option!")

    input("Press enter. \n")

    if playerdefending and not defendturn:
        playerstats[0][0] -= 10
        playerstats[0][1] -= 10
        playerstats[1] -= 20
        playercrit -= 35
        playerdefending = False
    print("It's the enemy's turn!")
    enemyturnchoice = r.randint(1, 15)
    if enemyturnchoice < 15:
        enemyhit = r.randint(1, 100)
        if enemyhit not in range(playerstats[2]):
            print("The enemy attacked!")
            enemydmg = r.randint(enemystats[0], enemystats[1])
            playerstats[3] -= enemydmg
            print("You took", enemydmg, "damage!")
            if playerstats[3] <= 0:
                print("You were defeated!")
                print("GAME OVER")
                exit()
        elif enemyhit in range(playerstats[2]):
            print("The enemy attacked!")
            print("You dodged!")
    elif enemyturnchoice == 15:
        if enemystats[3] < enemymaxhealth:
            print("The enemy chose heal!")
            healoption("enemy")
    else:
        print("Uh, something went wrong.")
    if defendturn:
        defendturn = False

input("Press enter to continue. \n")

print("ENEMY ENCOUNTER! DARK MAGE #3 \n These are the weapon choices for the battle:")
print("GOLDEN CUTLASS: 8 - 12 damage, 85% strike chance, 45% dodge chance")
print("AXE: 1 - 20 damage, 70% strike chance, 5% dodge chance")
print("LANCE: 3 - 10 damage, 100% strike chance, 10% dodge chance")
print("FLINTLOCK PISTOLS: 7 - 9 damage, 70% strike chance, 70% dodge chance")
print("MAGIC: 1 - 2 damage, 50% strike chance, 65% dodge chance")
print("\n 1. Golden Cutlass \n 2. Axe \n 3. Lance \n 4. Flintlock Pistols \n 5. Magic \n")
print("Choose the number of the weapon you want for this fight:")

playerstats = [0, 0, 0, 50]
enemystats = [11, 15, 0, 60]
playercrit = 0
maxhealth = 50
enemymaxhealth = 60
playerdefending = False
defendturn = False

weaponsdmg = [[8, 12], [1, 20], [3, 10], [7, 9], [1, 2]]
weaponshit = [85, 70, 100, 70, 50]
weaponsavo = [45, 5, 10, 70, 65]

sword = weaponsdmg[0], weaponshit[0], weaponsavo[0]
axe = weaponsdmg[1], weaponshit[1], weaponsavo[1]
lance = weaponsdmg[2], weaponshit[2], weaponsavo[2]
bow = weaponsdmg[3], weaponshit[3], weaponsavo[3]
magic = weaponsdmg[4], weaponshit[4], weaponsavo[4]

for tries in range(5):
    choice = (input())
    if choice == "1":
        print("You chose Golden Cutlass!")
        playerstats = [sword[0], sword[1], sword[2], playerstats[3]]
        break
    elif choice == "2":
        print("You chose axe!")
        playerstats = [axe[0], axe[1], axe[2], playerstats[3]]
        break
    elif choice == "3":
        print("You chose lance!")
        playerstats = [lance[0], lance[1], lance[2], playerstats[3]]
        break
    elif choice == "4":
        print("You chose Flintlock Pistols!")
        playerstats = [bow[0], bow[1], bow[2], playerstats[3]]
        break
    elif choice == "5":
        print("You chose magic!")
        playerstats = [magic[0], magic[1], magic[2], playerstats[3]]
        break
    else:
        if tries != 4:
            print("Not a weapon option. Try again.")
    if tries == 4:
        print("You took too long to choose a weapon.")
        print("You stand there uselessly, and the enemies kill you on the spot.")
        print("GAME OVER")
        exit()

print("The enemy chose elemental magic! The elements of nature at his fingertips!")

print("\n FIGHT! \n")

while playerstats[3] > 0 and enemystats[3] > 0:
    print("Your HP:", playerstats[3])
    print("Enemy HP:", enemystats[3])
    print("It's your turn! Choose Attack, Defend, or Heal.")
    turnchoice = input()
    if turnchoice == "attack" or turnchoice == "Attack":
        print("You chose attack!")
        print('"' + bcry() + '" you say.')
        hit = r.randint(1, 100)
        if hit in range(playerstats[1]):
            dmg = r.randint(playerstats[0][0], playerstats[0][1])
            criticalstrike()
            enemystats[3] -= dmg
            print("You dealt", dmg, "damage!")
            if enemystats[3] <= 0:
                print("Victory!")
                break
        elif hit not in range(playerstats[1]):
            print(missmessage())
            print("Your HP:", playerstats[3])
            print("Enemy HP:", enemystats[3])
        else:
            print("Uh, something went wrong.")
        print("Your HP:", playerstats[3])
        print("Enemy HP:", enemystats[3])
    elif turnchoice == "defend" or turnchoice == "Defend":
        print("You are defending!")
        defend()
    elif turnchoice == "heal" or turnchoice == "Heal":
        print("You chose heal!")
        healoption("player")
        print("Your HP:", playerstats[3])
        print("Enemy HP:", enemystats[3])
    else:
        print("You didn't choose an option!")

    input("Press enter. \n")

    if playerdefending and not defendturn:
        playerstats[0][0] -= 10
        playerstats[0][1] -= 10
        playerstats[1] -= 20
        playercrit -= 35
        playerdefending = False
    print("It's the enemy's turn!")
    enemyturnchoice = r.randint(1, 15)
    if enemyturnchoice < 15:
        enemyhit = r.randint(1, 100)
        if enemyhit not in range(playerstats[2]):
            print("The enemy attacked!")
            enemydmg = r.randint(enemystats[0], enemystats[1])
            playerstats[3] -= enemydmg
            print("You took", enemydmg, "damage!")
            if playerstats[3] <= 0:
                print("You were defeated!")
                print("GAME OVER")
                exit()
        elif enemyhit in range(playerstats[2]):
            print("The enemy attacked!")
            print("You dodged!")
    elif enemyturnchoice == 15:
        if enemystats[3] < enemymaxhealth:
            print("The enemy chose heal!")
            healoption("enemy")
    else:
        print("Uh, something went wrong.")
    if defendturn:
        defendturn = False

input("Press enter to continue. \n")

print("The souls of the dead from the massacre of Arundel cheer your praises and glory, now avenged.")
print("The legendary sword Arianrhod is embedded in stone. You grab its hilt and pull.")
print("It takes nearly all your strength, but time relents. You are worthy!")
print("WIth Arianrhod and Pagalion, you fly to Macedon's castle.")
print("Soaring through the skies, you swipe Arianrhod, glowing with an aura of light, through the clouds.")
print("Its blessing rejuvenates and strengthens you. It radiates immense power.")
print("Finally, you and Pagalion fly to the highest tower in Macedon's castle.")
print("The powerful warlord, clad in dark and spiky armour, is massive on his throne.")
print("He takes up the entire room. You feel like an ant.")
print("He wields Dwrnmyr, a legendary double-edged axe which has tasted the blood of entire drowned civilizations.")
print('"A knight of the King survives," he says. "This will be fun."')
print("This will be a battle of the ages!")
print("ENEMIES APPROACHING: 1 MACEDON")

input("Press enter to continue. \n")

print("ENEMY ENCOUNTER! MACEDON \n These are the weapon choices for the battle:")
print("ARIANRHOD: 1000 - 1200 damage, 85% strike chance, 45% dodge chance")
print("AXE: 1 - 20 damage, 70% strike chance, 5% dodge chance")
print("LANCE: 3 - 10 damage, 100% strike chance, 10% dodge chance")
print("FLINTLOCK PISTOLS: 7 - 9 damage, 70% strike chance, 70% dodge chance")
print("MAGIC: 10 - 15 damage, 50% strike chance, 65% dodge chance")
print("\n 1. Arianrhod \n 2. Axe \n 3. Lance \n 4. Flintlock Pistols \n 5. Magic \n")
print("Choose the number of the weapon you want for this fight:")

playerstats = [0, 0, 0, 70]
enemystats = [20, 20, 0, 10000]
playercrit = 0
maxhealth = 70
enemymaxhealth = 10000
playerdefending = False
defendturn = False

weaponsdmg = [[1000, 1200], [1, 20], [3, 10], [7, 9], [10, 15]]
weaponshit = [85, 70, 100, 70, 50]
weaponsavo = [45, 5, 10, 70, 65]

sword = weaponsdmg[0], weaponshit[0], weaponsavo[0]
axe = weaponsdmg[1], weaponshit[1], weaponsavo[1]
lance = weaponsdmg[2], weaponshit[2], weaponsavo[2]
bow = weaponsdmg[3], weaponshit[3], weaponsavo[3]
magic = weaponsdmg[4], weaponshit[4], weaponsavo[4]

for tries in range(5):
    choice = (input())
    if choice == "1":
        print("You chose Arianrhod! The legendary sword of light that can cleave the heavens!")
        playerstats = [sword[0], sword[1], sword[2], playerstats[3]]
        break
    elif choice == "2":
        print("You chose axe! Ha, good luck.")
        playerstats = [axe[0], axe[1], axe[2], playerstats[3]]
        break
    elif choice == "3":
        print("You chose lance! Ha, good luck.")
        playerstats = [lance[0], lance[1], lance[2], playerstats[3]]
        break
    elif choice == "4":
        print("You chose Flintlock Pistols! Ha, good luck.")
        playerstats = [bow[0], bow[1], bow[2], playerstats[3]]
        break
    elif choice == "5":
        print("You chose magic! Ha, good luck.")
        playerstats = [magic[0], magic[1], magic[2], playerstats[3]]
        break
    else:
        if tries != 4:
            print("Not a weapon option. Try again.")
    if tries == 4:
        print("You took too long to choose a weapon.")
        print("You stand there uselessly, and Macedon slays you on the spot.")
        print("It wasn't such a legendary battle after all.")
        print("GAME OVER")
        exit()

print("The enemy chose Dwrnmyr! The legendary double-edged axe of darkness that gives its holder virtual immortality!")

print("\n FIGHT! \n")

while playerstats[3] > 0 and enemystats[3] > 0:
    print("Your HP:", playerstats[3])
    print("Enemy HP:", enemystats[3])
    print("It's your turn! Choose Attack, Defend, or Heal.")
    turnchoice = input()
    if turnchoice == "attack" or turnchoice == "Attack":
        print("You chose attack!")
        print('"' + bcry() + '" you say.')
        hit = r.randint(1, 100)
        if hit in range(playerstats[1]):
            dmg = r.randint(playerstats[0][0], playerstats[0][1])
            criticalstrike()
            enemystats[3] -= dmg
            print("You dealt", dmg, "damage!")
            if enemystats[3] <= 0:
                print("Victory!")
                break
        elif hit not in range(playerstats[1]):
            print(missmessage())
            print("Your HP:", playerstats[3])
            print("Enemy HP:", enemystats[3])
        else:
            print("Uh, something went wrong.")
        print("Your HP:", playerstats[3])
        print("Enemy HP:", enemystats[3])
    elif turnchoice == "defend" or turnchoice == "Defend":
        print("You are defending!")
        defend()
    elif turnchoice == "heal" or turnchoice == "Heal":
        print("You chose heal!")
        healoption("player")
        print("Your HP:", playerstats[3])
        print("Enemy HP:", enemystats[3])
    else:
        print("You didn't choose an option!")

    input("Press enter. \n")

    if playerdefending and not defendturn:
        playerstats[0][0] -= 10
        playerstats[0][1] -= 10
        playerstats[1] -= 20
        playercrit -= 35
        playerdefending = False
    print("It's the enemy's turn!")
    enemyturnchoice = r.randint(1, 15)
    if enemyturnchoice < 13:
        enemyhit = r.randint(1, 100)
        if enemyhit not in range(playerstats[2]):
            print("The enemy attacked!")
            enemydmg = r.randint(enemystats[0], enemystats[1])
            playerstats[3] -= enemydmg
            print("You took", enemydmg, "damage!")
            if playerstats[3] <= 0:
                print("You were defeated!")
                print("GAME OVER")
                exit()
        elif enemyhit in range(playerstats[2]):
            print("The enemy attacked!")
            print("You dodged!")
    elif enemyturnchoice == 13 or enemyturnchoice == 14 or enemyturnchoice == 15:
        if enemystats[3] < enemymaxhealth:
            print("The enemy chose heal!")
            healoption("boss")
    else:
        print("Uh, something went wrong.")
    if defendturn:
        defendturn = False

input("Press enter to continue. \n")

print("You pull out Arianrhod and pierce it into Macedon's heart. The warlord is defeated!")
print('"Please," Macedon pleads as he draws his last few breaths. "You do not understand."')
print('"The King is evil. Corrupt. He is holding my family hostage. I raided Arundel to save them."')
print('"Then he called his grand wizard to destroy the city with pillars of light, killing my family and everyone there."')
print('"You are deluded. You are deceived. He must be calling his grand wizard to destroy this place now. To kill you."')
print("There is no way you believe this malicious--")
print("BOOM! Pillars of light rain down on the palace. Chunks of rubble fall from the ceiling.")
print("You die from the weight of the palace collapsing...")
print("...as the King finishes off his Last Knight and erases the last witness to his crimes.")
print("GAME OVER")


