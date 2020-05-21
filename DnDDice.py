#DnD Dice Rolling program

import random


# This while loop will ensure the user inputs an integer 
while True:
    flag = True  # Assigning True to the variable flag removes confusion and allows the bool values to be contained here
    while flag: # while 'TRUE'
        dice = input('Which dice would you like to roll? ')  # 
        if dice.isdigit():
            dice = int(dice)
            flag = False  # while FALSE Once the flag returns false the loop will break and move on
        else:
            print('Whoops. It looks like you did not enter a number.')


# This while loop allows the user to continue rolling dice without a break in the program 
    while True:
        print('You rolled ' )

        if dice == 20:
            d20 = random.randint(1, 20)
            print(str(d20) + '!')
            if d20 == 20:               # If the user rolls a 20 or 1 the program will return text
                print('CRITICAL HIT!')  #
            elif d20 == 1:              #
                print('CRITICAL FAIL!') #

        elif dice == 10:
            d10 = random.randint(1, 10)
            print(str(d10) + '!')
                
        elif dice == 8:
            d8 = random.randint(1,8) 
            print(str(d8) + '!')

        elif dice == 6:
            d6 = random.randint(1,6)
            print(str(d6) + '!')
            
        elif dice == 4:
            d4 = random.randint(1,4)
            print(str(d4) + '!')
            
        else:
            print('Please type either a 20, 10, 8, 6 or 4') # if the user types anything other than the programmed dice rolls the program will prompt to try again
        break                                               # This break point moves the loop back to the first while loop that asks for an input
        

        





        
