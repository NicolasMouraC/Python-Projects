import random
import time
import sys


dic = {"luc":0, "agi":0, "intl":0}
points = 5
optAtk = random.randint(1, 3)
optHp = random.randint(1, 3)
optIntl = random.randint(1, 3)        
myHp = 1
myAtk = 1
myIntl = 0
turn = 0
gender = ''
nam = ''
txtSpeed = 1

class Engine():
    def ShowStats(Dluc, Dagi, Dintl):
        print("Atk points: " + str(Dluc))
        print("Health points: " + str(Dagi))
        print("Intelligence: " + str(Dintl))
    def Stats(dict, pts):
        global dic
        flag = True
        test = [1, 2, 3]
        points = pts
        Engine.ShowStats(dic["luc"], dic["agi"], dic["intl"])
        print("You have " + str(points) + " points to spend")
        time.sleep(2)
        while points > 0:
            p = int(input("1 = luck, 2 = agility, 3 = intelligence: \n"))
            if p == 1:
                print("One point added to Luck!")
                time.sleep(0.5)
                dic["luc"] += 1
                points -= 1
            elif p == 2:
                print("One point added to agility!")
                time.sleep(0.5)
                dic["agi"] += 1
                points -= 1
            elif p == 3:
                print("One point added to intelligence!")
                dic["intl"] += 1
                points -= 1
            elif p not in test:
                while flag:
                    p = int(input("1 = luc, 2 = agi, 3 = intl: \n"))
                    if p in test:
                        if p == 1:
                            dic["luc"] += 1
                            points -= 1
                            flag = False
                        elif p == 2:
                            dic["agi"] += 1
                            points -= 1
                            flag = False
                        elif p == 3:
                            dic["intl"] += 1
                            points -= 1
                            flag = False
        Engine.ShowStats(dic["luc"], dic["agi"], dic["intl"])
        print("-")
        time.sleep(2)
        Levels.Sit1()

    def Settings(dic, points):
        global txtSpeed
        opt = str(input("G for game, S for settings \n"))
        if opt.upper() == "G":
            Engine.Stats(dic, points)
        elif opt.upper() == "S":
            print("You can choose the speed of the txt")
            time.sleep(txtSpeed)
            txtSpeed = float(input("Please, enter a number to be set as txt speed:\n"))
            time.sleep(txtSpeed)
            print("{} is now the txt speed".format(txtSpeed))
            time.sleep(txtSpeed)
            Engine.Stats(dic, points)

class Combat():
    def CombatStats(dict):
        global dic 
        global optAtk
        global optHp         
        global myHp
        global myAtk
        global myIntl
        myAtk = dic["luc"]
        if myAtk < 1:
            myAtk = 1
        myHp = dic["agi"]
        if myHp < 1:
            myHp = 1
        myIntl = dic["intl"]
        if myIntl >= optIntl:
            print("Your stats are:")
            time.sleep(txtSpeed)
            print("Attack points: {}".format(myAtk))
            print("Health points: {}".format(myHp))
            print("Intelligence points: {}".format(myIntl))
            time.sleep(txtSpeed)
            print("Your opponent stats are:")
            time.sleep(txtSpeed)
            print("Attack points: {}".format(optAtk))
            print("Health points: {}".format(optHp))
            print("Intelligence points: {}".format(optIntl))
            time.sleep(txtSpeed)
            print("It's your turn!")
            time.sleep(txtSpeed)
        elif optIntl > myIntl:
            print("Your stats are:")
            time.sleep(txtSpeed)
            print("Attack points: {}".format(myAtk))
            print("Health points: {}".format(myHp))
            print("Intelligence points: {}".format(myIntl))
            time.sleep(txtSpeed)
            print("Your opponent stats are:")
            time.sleep(txtSpeed)
            print("Attack points: {}".format(optAtk))
            print("Health points: {}".format(optHp))
            print("Intelligence points: {}".format(optIntl))
            time.sleep(txtSpeed)
            print("It's your opponent's turn.")
            time.sleep(txtSpeed)
            turn = 1
        Combat.ChooseAction(turn)
    def ChooseAction(whoTurnIs):
        Shield1 = False
        Shield2 = False
        global optAtk
        global optHp         
        global myHp
        global myAtk
        while True:
            if myHp < 1:
                print("You died...")
                time.sleep(txtSpeed)
                print("Ending...")
                time.sleep(txtSpeed)
                sys.exit()
            elif optHp < 1:
                print("The opponent was defeated. You did it!")
                time.sleep(txtSpeed)
                print("Now you are heading towards the forest.")
                time.sleep(txtSpeed)
                Levels.Sit3()
            print("-")
            print("You have {}HP".format(myHp))
            print("Your opponent have {}HP".format(optHp))
            print("-")
            time.sleep(txtSpeed)
            if whoTurnIs == 0:
                move = int(input("Select a move: 1 (for Attack ) or 2 (for Defense)"))
                Shield1 = False
                if move == 1:
                    if Shield2:
                        print("The opponent is in defense position. So the attack did no damage.")
                        whoTurnIs = 1
                        time.sleep(txtSpeed)
                    else:    
                        print("Your attack did {} dmg to the opponents hp".format(myAtk))
                        optHp -= myAtk
                        print("The opponent now has {} hp".format(optHp))
                        whoTurnIs = 1
                        time.sleep(txtSpeed)
                elif move == 2:
                    print("You are now in defense position. If the opponent tries to attack you, it won't have any effect.")
                    Shield1 = True
                    whoTurnIs = 1
                    time.sleep(txtSpeed)
            elif whoTurnIs == 1:
                move = random.randint(1,2)
                Shield2 = False
                if move == 1:
                    if Shield1:
                        print("The opponent tried to attack. Since you are in defense position, the attack won't had any effect")
                        whoTurnIs = 0
                        time.sleep(txtSpeed)
                    else:
                        print("The opponent Attacked you and did {} damage to your hp".format(optAtk))
                        myHp -= optAtk
                        print("You now have {} hp".format(myHp))
                        whoTurnIs = 0
                        time.sleep(txtSpeed)
                elif move == 2:
                    print("The opponent is now in defense position.")
                    Shield2 = True
                    whoTurnIs = 0
                    time.sleep(txtSpeed)

class Levels():
    def Sit1():
        global gender
        global nam
        print("This is the beginning of this game")
        time.sleep(txtSpeed)
        print("You Can choice a gender for your character\n")
        time.sleep(txtSpeed)
        opt = str(input("Type B to see the gender options or N to continue\n"))
        if opt.upper() == "N":
            print("Aparently, your character doesn't have a gender")
            gender = "doesn't have a gender"
        elif opt.upper() == "B":
            print("Good you have two option of gender\n")
            print("1 - Your character is a man")
            print("2 - Your character is a female")
            time.sleep(1)
            gender_opt = int(input("Enter a option: "))
            if gender_opt == 1:
                print("You character is a man")
                gender = "man"
            elif gender_opt == 2:
                print("You character is a female")
                gender = "female"
            else:
                print("Ok, your gender is " + str(opt))
                gender = opt
        else:
            print("Ok, your gender is " + str(opt))
            gender = opt
        nam = str(input("Enter a name for your character: \n"))
        time.sleep(txtSpeed)
        print("Ok so your name is {} and you are a {}".format(nam, gender))
        time.sleep(txtSpeed)
        Levels.Sit2()
        
    def Sit2():
        print("Imagine that there is a epic story about a monster you'll have to defeat here")
        time.sleep(txtSpeed)
        Combat.CombatStats(dic)
    def Sit3(agi):
        pass

for a in range(5): print("-")

Engine.Settings(dic, points)
print("End....")
time.sleep(txtSpeed)
sys.exit()