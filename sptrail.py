import time
import os
from rich.console import Console
import random
import json
c = Console()
os.system('cls')


money = 300000
o2  = 0
water = 0
food = 0
year = 100
weapons = ["super misile" , 0 , "lazer blaster" , 0 ]
sp1 = ["normal" ,  15 , 100000  ]
sp2 = ["extra" , 30 , 150000]
sp3 = ["extra plus" , 50 ,200000 ]
csp = ""
medkits = 0 


def sickness():
    os.system('cls')
    global medkits

    c.print("[red] you are sick[red/]")
    
    if medkits == 0:
        c.print("[red] no medkits remaning buing medkit [red]")
        if money < 800:
            print("not enough money")
            time.sleep('cls')
            gameOver()
        else:
            money = money - 800
            c.print("[green] you are healed [green/]")
            time.sleep(2)
            os.system('cls')
    else:
        print("using med kit")
        time.sleep(2)
        os.system('cls')
        medkits = medkits - 1
        c.print("[green] you are healed [green/]")
        time.sleep(2)
        os.system('cls')


            
        


def gameOver():
    os.system('cls')
    c.print("[red] GAME OVER [red/]")
    exit()



def store(ft):
    global o2
    global water
    global food
    global weapons
    global csp
    global medkits
    


    print ("welcome to my shop")
    time.sleep(2)
    os.system('cls')


    if ft == True:
        print("you will need a space ship to go to uranus")
        time.sleep(2)
        os.system('cls')
       
        print("lucky for you I have a few")
        time.sleep(2)
        os.system('cls')




        while ft == True:
            os.system('cls')


            c.print("""
            [red]
                _________________________________________
                | 1. normal has 15 years suply of o2    |
                |  © 100,000                            |
                |                                       |
                | 2. luxry has 30 years suply of o2     |
                |   © 150,000                           |
                |                                       |
                | 3.extra luxry has 30 years suply of 02|
                |   © 200,000                           |
                |                                       |
                |   type 1 or 2 or 3                    |
                |_______________________________________|




                [red/]
        """)
           


            global money


           


            i = input(">")


            if i == "1":
                csp = sp1
                money = money - csp[2]
                o2 = csp[1]
                print("you have ©", money , " left" )
                ft = False




            elif i == "2":
                csp = sp2
                money = money - csp[2]
                o2 = csp[1]
                print("you have ©", money , " left" )
                ft = False




            elif i == "3":
                csp = sp3
                money = money - csp[2]
                o2 = csp[1]
                print("you have ©", money , " left" )
                ft = False


            else:
                print("invalid input")
                time.sleep(1)
   
    q = 0


    while q == 0:


        os.system('cls')




        c.print(f"""
           
            [green]
                        money remaining: {money}            
                    _________________________________________
                    |                 STORE                 |
                    |                                       |
                    |  1 lazer blaster - ©50 per 10 rounds  |
                    |                                       |
                    |  2 super misile - ©1000               |
                    |                                       |
                    |  3 food - ©800 per year               |
                    |                                       |
                    |  4 water - ©600 per year              |
                    |                                       |
                    |  5. extra o2 - ©800 per year          |
                    |                                       |
                    |  6. medkits -   ©800                  |
                    |                                       |
                    |  7 exit                               |
                    |_______________________________________|
           
           
            [green/]
           
            """)
       
        i = int(c.input("[red] > [red/]"))





        if i == 1:
            c.print("[red] how many lazer blaster [red/]")
            i1 = c.input("[red]>[red/]")
            if  i1.isnumeric()  == True:
                money1 = money - (50 *  float(i1))
                if money1 < 0:
                    print("not enough money")
                    time.sleep(1)
                else:
                    money= money1
                    weapons[1]  = weapons[1]+ float(i1)
                    print("you have ©" , money , "left")
                    time.sleep(1)
            else:
                print("not a integer")
                time.sleep(2)
                os.system('cls')




        elif i == 2:
            c.print("[red] how many super misiles [red/]")
            i1 = c.input("[red]>[red/]")
            if i1.isnumeric()  == True:
                money1 = money - (1000 *  float(i1))
                if money1 < 0:
                    print("not enough money")
                    time.sleep(1)
                else:
                    money= money1
                    weapons[3]  =  weapons[3] + float(i1)
                    print("you have ©" , money , "left")
                    time.sleep(1)
            else:
                print("not a integer")
                time.sleep(2)
                os.system('cls')







        elif i == 3:
            c.print("[red] how much food [red/]")
            i1 = c.input("[red]>[red/]")
            if i1.isnumeric()  == True:
                money1 = money - (800 *  float(i1))
                if money1 < 0:
                    print("not enough money")
                    time.sleep(1)
                else:
                    money= money1
                    food  = food+ float(i1)
                    print("you have ©" , money , "left")
                    time.sleep(1)     
            else:
                print("not a integer")
                time.sleep(2)
                os.system('cls')






        elif i == 4:
            c.print("[red] how much water [red/]")
            i1 = c.input("[red]>[red/]")
            if i1.isnumeric()  == True:
                money1 = money - (600 *  float(i1))
                if money1 < 0:
                    print("not enough money")
                    time.sleep(1)
                else:
                    money= money1
                    water  = water +float(i1)
                    print("you have ©" , money , "left")
                    time.sleep(1)
            else:
                print("not a integer")
                time.sleep(2)
                os.system('cls')


        elif i == 5:
            c.print("[red] how much o2 [red/]")
            i1 = c.input("[red]>[red/]")
            if i1.isnumeric()  == True:
                money1 = money - (800 *  float(i1))
                if money1 < 0:
                    print("not enough money")
                    time.sleep(1)
                else:
                    money= money1
                    o2  = o2+ float(i1)
                    print("you have ©" , money , "left")
                    time.sleep(1)  
            else:
                print("not a integer")
                time.sleep(2)
                os.system('cls')




        elif i == 6:
            c.print("[red] how much medkits [red/]")
            i1 = c.input("[red]>[red/]")
            if i1.isnumeric()  == True:
                money1 = money - (800 *  float(i1))
                if money1 < 0:
                    print("not enough money")
                    time.sleep(1)
                else:
                    money= money1
                    medkits  = medkits+ float(i1)
                    print("you have ©" , money , "left")
                    time.sleep(1)  
            else:
                print("not a integer")
                time.sleep(2)
                os.system('cls')



        elif i == 7:
            print("see you later")
            time.sleep(1)
            os.system('cls')
            q = 1


        else:
            print("invalid response")
            time.sleep(1)



def loot():
    global food
    global water
    global weapons
    global money
    os.system('cls')
    choice1 = 'yes'
    weight1 = 1  # More likely to happen, weight is higher
    choice2 = 'no'
    weight2 = 2
    choices = [choice1, choice2]
    weights = [weight1, weight2]
    random_choice = random.choices(choices, weights)[0]


    c.print(" [yellow] looking for ships to loot [yellow/] ")
    time.sleep(3)
    os.system('cls')
    if random_choice == 'yes':
        c.print(" [green]ship found [green/]")
        weight1 = 2
        weight2 = 1
        random_choice = random.choices(choices, weights)[0]
        c.print("[yellow] checking for wepons on ship ")
        time.sleep(3)
        os.system('cls')
        if random_choice == 'yes':
            we = True
            c.print("[red] the ship has wepons [red/]")
            c.print("you have" , weapons , "remaining ")
            time.sleep(4)
            os.system('cls')
            
        else:
            c.print("[green] there are no wepons on the the ship [green/]")
            we = False
            time.sleep(3)
            os.system('cls')
       


        q = 0
       
        while q == 0:
            c.print(" type a to attack the ship or b to back out")
            inp = c.input("[red] > [red/]")


            if inp == "a":
                attack = True
                q = 1


            elif inp == "b":
                attack = False
                q =1


            else:
                c .print(" [red ]invalid input [red/]")
                time.sleep(1)
                os.system('cls')


        if attack == True:
            c.print("[red] comencing attack [red/]")
            time.sleep(3)
            os.system('cls')
            choice1 = 'win'
            weight1 = 1  # More likely to happen, weight is higher
            choice2 = 'loss'
            weight2 = 2
            choices = [choice1, choice2]
            weights = [weight1, weight2]
            #random_choice = random.choices(choices, weights)[0]
            q = 0
            if we == False and weapons[1] > 2 or weapons[3] > 1:
                print("the ship has given up")
                time.sleep(3)
                os.system('cls')
                food1 = random.randint(1 , 10)
                food = food + food1
                water1 = random.randint(1,10)
                water = water + water1
                print("you recive " , water1 , " water and " , food1 , " food")
                time.sleep(3)
                os.system('cls')
            elif weapons[1]  > 10 or weapons[3] > 5:
                c.print("[red] not enough weopns remaining [red/]")
                time.sleep(3)
                os.system('cls')
            else:
                if weapons[1] > 10:
                    weight1 = weight1 + 1
                if weapons[3] > 2:
                    weight1 = weight1 + 1
                ammoe = random.randint(1 , 20)
                weight2 = weight2 + ammoe
                ammod = random.randint(1,15)
                ammoda = random.randint(1,5)
                weight1 = weight1 + ((ammod + ammoda)/2)
                weapons[1] = weapons[1] - ammod
                weapons[3] = weapons[3] - ammoda
                random_choice = random.choices(choices, weights)[0]
                if random_choice == 'win':
                    c.print("[green] you have won [green/]")
                    food1 = random.randint(1 , 10)
                    food = food + food1
                    money1 = random.randint(1000,100000)
                    money = money + money1
                    water1 = random.randint(1,10)
                    water = water + water1
                    print("you recive " , water1 , " water and " , food1 , " food and" , money1,  "money")
                    time.sleep(3)
                    os.system('cls')
                else:
                    c.print("[red] you lost[red/]")
                    food1 = random.randint(1 , 10)
                    food = food - food1
                    water1 = random.randint(1,10)
                    water = water - water1
                    money1 = random.randint(1000,100000)
                    money = money - money1
                    if food < 0 or water < 0 or money < 0 :
                        gameOver() #change line to function
                    else:
                        print("you lose " , water1 , " water and " , food1 , " food and " , money1 , "money")
                        time.sleep(3)
                        os.system('cls')
    else:
        c.print("[red] no ships found to loot [red/]")
        time.sleep(3)
        os.system('cls')


def looted():
    global money
    global food
    global weapons
    global water

    c.print("[red] you are being looted [red/]")
    time.sleep(2)
    if weapons[1] < 0 and weapons[3] < 0:
        c.print("[red] you lost[red/]")
        food1 = random.randint(1 , 10)
        food = food - food1
        water1 = random.randint(1,10)
        water = water - water1
        money1 = random.randint(1000,100000)
        money = money - money1
        if food < 0 or water < 0 or money < 0 :
            gameOver() #change line to function
        else:
            print("you lose " , water1 , " water and " , food1 , " food and " , money1)
            time.sleep(3)
            os.system('cls')
    
    else:
        q = 0 
        while q == 0:
            os.system('cls')
            c.print("[yellow] do you want to defend or give up pres g to give up and d to defend")
            inpu = c.input("[red] > [red/]")
            if inpu == "d":
                defend = True
                q = 1
            elif inpu == "g":
                defend = False
                q =1
            else:
                print("invalid response")
                time.sleep(2)
                os.system('cls')

        if defend == False:
            c.print("[red] you give up[red/]")
            time.sleep(2)
            os.system('cls')
            food1 = random.randint(1 , 10)
            food = food - food1
            water1 = random.randint(1,10)
            water = water - water1
            money1 = random.randint(1000,100000)
            money = money - money1
            if food < 0 or water < 0 or money < 0 :
                gameOver() #change line to function
            else:
                print("you lose " , water1 , " water and " , food1 , " food and " , money1 , "money")
                time.sleep(3)
                os.system('cls')




        elif defend == True:
            if weapons[1] < 21  and weapons[3] < 6:
                c.print(" [red] not enough wepons remainig [red/]")
                time.sleep(3)
                os.system('cls')
            else:

                c.print("[yellow] preparing to attack [yellow/]")
                time.sleep(3)
                os.system('cls')
                choice1 = 'win'
                weight1 = 1  # More likely to happen, weight is higher
                choice2 = 'loss'
                weight2 = 2
                choices = [choice1, choice2]
                weights = [weight1, weight2]
                ammoe = random.randint(1 , 20)
                weight2 = weight2 + ammoe
                ammod = random.randint(1,15)
                ammoda = random.randint(1,5)
                weight1 = weight1 + ((ammod + ammoda)/2)
                weapons[1] = weapons[1] - ammod
                weapons[3] = weapons[3] - ammoda
                random_choice = random.choices(choices, weights)[0]
                if random_choice == 'win':
                    c.print("[green] you have won [green/]")
                    time.sleep(3)
                    os.system('cls')
                    food1 = random.randint(1 , 10)
                    food = food + food1
                    money1 = random.randint(1000,100000)
                    money = money + money1
                    water1 = random.randint(1,10)
                    water = water + water1
                    money1 = random.randint(1000,100000)
                    money = money + money1
                    print("you recive " , water1 , " water and " , food1 , " food and " , money1 , "money")
                    time.sleep(3)
                    os.system('cls')
                else:
                    c.print("[red] you lost[red/]")
                    time.sleep(3)
                    os.system('cls')
                    food1 = random.randint(1 , 10)
                    food = food - food1
                    water1 = random.randint(1,10)
                    water = water - water1
                    money1 = random.randint(1000,100000)
                    money = money - money1
                    if food < 0 or water < 0 or money < 0 :
                        gameOver() #change line to function
                    else:
                        print("you lose " , water1 , " water and " , food1 , " food and " , money1 , "money")
                        time.sleep(3)

def tut ():
    q = 0 
    while q == 0:
        os.system('cls')
        c.print("""
[red]


__________________________________________
|                 RULES                  |
|                                        |
|  Elon musk has made uranus habitlble   |
|                                        |
|  it will take 1 hundred years          |
|                                        |
|  you are trying to get to uranus       |
|                                        |
|  this will be a dangurous journey      |
|                                        |
|  you will start out with 300,000 coins |
|                                        |
|  there will be looters                 |
|                                        |
|  and and you can loot too              |
|                                        |
|  there are also alien stores           |
|                                        |
|             GOOD LUCK                  |
|                                        |
|     press p to play or e to exit       |
|________________________________________|

[red/]



        """)
        inp = c.input("[red] > [red]")

        if inp == "p":
            q = 1 
        elif inp == "e":
            exit()
        else:
            print("invalid response")
            time.sleep(2)


def save_file():
    global money
    global food
    global weapons
    global water
    global o2
    global year
    global csp
    global medkits 

    data = {

        "money" : money,
        "food" : food,
        "weapons": weapons,
        "water": water,
        "o2": o2,
        "year" : year,
        "csp": csp
    }    
    print("what do you want to name your save file")
    name = c.input("[red] > [red/]")
    with open(f"{name}.json", "w") as g:
        json.dump(data, g)
        os.system('cls')


def load_file():
    global money
    global food
    global weapons
    global water
    global o2
    global year
    global csp

    print("what is the name of the save file")
    inp = c.input("[red] > [red/]")


    with open(f"{inp}.json", "r") as f:
        data = json.load(f)
    
    money = data["money"]
    food = data["food"]
    weapons = data["weapons"]
    water = data["water"]
    o2 = data["o2"]
    year = data["year"]
    csp = data["csp"]


def main():
    os.system('cls')
    global money
    global food
    global weapons
    global water
    global o2
    global year
    global a
    lo = False
    ac = 0 

    if year < 0:
        c.print("[green] you have arrived to uranus [green/]")
    else:
            food = float(food) - 1 
            water = water - 1
            o2 = o2 - 1
            year = year - 1
            a = 0 

            if food < 0 or water < 0 or o2 <0:
                gameOver()

            choice1 = 'looted'
            weight1 = 1  # More likely to happen, weight is higher
            choice2 = 'unlooted'
            weight2 = 2
            choices = [choice1, choice2]
            weights = [weight1, weight2]
            random_choice = random.choices(choices, weights)[0]
            if random_choice == 'looted':
                looted()
            

            choice1 = 'sick'
            weight1 = 1  # More likely to happen, weight is higher
            choice2 = 'unsick'
            weight2 = 2
            choices = [choice1, choice2]
            weights = [weight1, weight2]
            random_choice = random.choices(choices, weights)[0]

            if random_choice == 'sick':
                sickness()




            while a == 0:
                os.system('cls')
                c.print(f"""


                [green]
                        ____________________________________________________________________________
                        |money remaining: {money}         
                        |___________________________________________________________________________
                        |                                       | lazer ammo: {weapons[1]}           
                        |  1. vist store                        |                             
                        |                                       | misile ammo: {weapons[3]}          
                        |  2. look for for ships to loot        |                             
                        |                                       | years remaining: {year}        
                        |  3. watch tutorial                    |                             
                        |                                       | food remaining: {food}          
                        |  4. go to next year                   |                             
                        |                                       | water remaining: {water}       
                        |  5. exit game                         |                                           
                        |                                       | o2 remaining: {o2}  
                        |  6. create a save file                |
                        |                                       |        
                        |_______________________________________|____________________________________


            [green/]

            """)
                inp = (c.input("[red] > [red/]"))
                if inp == "1":
                    store(ft = False)
                elif inp == "2":
                    
                    if ac ==0:
                        loot()
                        ac = 1
                    else:
                        c.print("[red] you already have looted [red/]")
                        time.sleep(2)
                elif inp == "3":
                    tut()
                elif inp == "4":
                    a = 1 

                elif inp == "5":
                    exit()
                
                elif inp == "6":
                    save_file()

                else:
                    c.print("[red] invalid input! [red/]")
                



asdf = 0 
while asdf == 0:

    os.system('cls')
    print("do you want to load a save file  y/n")
    svf = c.input("[red] > [red/]")
    if svf == "y":
        load_file()
        asdf = 2
    elif svf == "n":
        asdf = 1
    else:
        c.print("[red] invalid input [red/]")
        time.sleep(2)


if asdf == 2:
    while True:
        main()
else:
    tut()
    store(ft = True)

    while True:
        main()


