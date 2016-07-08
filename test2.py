import sys
import random
tot=1
matrix_x=6
matrix_y=4
matrix_x=input('No. of columns: ')
matrix_y=input('No. of rows: ')
while(tot!=matrix_x*matrix_y):
    raw_input('\nRoll the dice?')
    number_on_dice=random.randint(1,6)
    
    sys.stdout.write('Number on the dice=')
    print(number_on_dice)
    
    
    x=(tot-1)%matrix_x+1
    y=(tot-1)/matrix_x+1
    
    if(y%2==0):
        x=matrix_x+1-x
    
    
    if tot+number_on_dice<=matrix_x*matrix_y:
        tot+=number_on_dice
    if(matrix_x*matrix_y-tot<6 and matrix_x*matrix_y-tot>0):
        print 'You need ',matrix_x*matrix_y-tot,' or less to win'
    print "Dice on: ",tot
    print "X: ",x
    print "Y: ",y
    
if(tot>matrix_x*matrix_y):
    print('Better luck next time')
else:
    print('You\'ve won!')
    
    
    
    
