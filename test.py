import sys
import random
tot=0
while(tot<16):
    raw_input('Roll the dice?')
    number_on_dice=random.randint(1,6)
    #print('Number on the dice=')
    sys.stdout.write('Number on the dice=')
    print(number_on_dice)
    tot+=number_on_dice
    #print("Dice on: ")
    sys.stdout.write("Dice on: ")
    print(tot)
if(tot>16):
    print('Better luck next time')
else:
    print('You\'ve won!')
    
    
    
    
