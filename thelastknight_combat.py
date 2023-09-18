
import random as r

# for the player: the first stat is dmg, the second stat is hit, the third stat is avo, the fourth stat is HP
# recap: dmg = damage, hit = strike chance, avo = avoidance rate, HP = health points
# *note* since there is no need for duplicate stats, the player's hit stat will act as the enemy's avo stat
# and the enemy's hit stat will act as the player's avo stat
# for the enemy: the first stat is minimum dmg, second stat is maximum dmg, third stat is placeholder so the
# fourth stat, health, can both be [3] and I won't get confused
playerstats = [0, 0, 0, 30]
enemystats = [0, 0, 0, 30]
# playercrit = critical strike chance. Only accessible during the 'Defend' option in combat. Only the player has it.
playercrit = 0
playerdefending = False
defendturn = False

# Telling the user the stats of each weapon and giving them an option to pick one.
print("ENEMY ENCOUNTER! \n These are the weapon choices for the battle:")
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

print("\n FIGHT! \n")
print("Battle Tactics:")
print("Attack: Deal damage with your weapon if it connects.")
print("Defend: Wait a turn. On your next turn, gain 10 dmg, 20 hit, 10 avo, 35 crit.")
print("Heal: Randomly choose a concoction elixir, healing magic, or bandage to treat your wounds. \n")


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
# worse healing options for the enemy is increased. ALso, it is a rarity for the enemy to heal.

def healoption(user):
    healoptionchoice = r.randint(1, 4)
    if playerstats[3] < 30 or enemystats[3] < 30:
        if user == "player":
            if healoptionchoice == 1:
                print("You chose concoction elixir!")
                if playerstats[3] + 5 > 30:
                    playerstats[3] = 30
                else:
                    playerstats[3] += 5
            elif healoptionchoice == 2 or healoptionchoice == 3:
                print("You chose healing magic!")
                if playerstats[3] + 10 > 30:
                    playerstats[3] = 30
                else:
                    playerstats[3] += 10
            elif healoptionchoice == 4:
                print("You chose bandage!")
                if playerstats[3] + 1 > 30:
                    playerstats[3] = 30
                else:
                    playerstats[3] += 1
        elif user == "enemy":
            if healoptionchoice == 1:
                print("The enemy chose concoction elixir!")
                if enemystats[3] + 5 > 30:
                    enemystats[3] = 30
                else:
                    enemystats[3] += 5
            elif healoptionchoice == 2:
                print("The enemy chose healing magic!")
                if enemystats[3] + 10 > 30:
                    enemystats[3] = 30
                else:
                    enemystats[3] += 10
            elif healoptionchoice == 3 or healoptionchoice == 4:
                print("The enemy chose bandage!")
                if enemystats[3] + 1 > 30:
                    enemystats[3] = 30
                else:
                    enemystats[3] += 1
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
    playerstats[2] += 10
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
            print("Your HP:", playerstats[3])
            print("Enemy HP:", enemystats[3])
            if enemystats[3] <= 0:
                print("Victory!")
                break
        elif hit not in range(playerstats[1]):
            print(missmessage())
            print("Your HP:", playerstats[3])
            print("Enemy HP:", enemystats[3])
        else:
            print("Uh, something went wrong.")
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
        playerstats[2] -= 10
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













