import sys
import random

print("""

Welcome to tic-tac-toe 1 player game!

First of all choose 'x' or 'o'!
""")

person_choice = input("Here  -->   ")
print()

if person_choice == 'o':
    computer_choice = 'x'
elif person_choice == 'x':
    computer_choice = 'o'
else:
    print("""
Wrong input dude
    """)
    sys.exit()


game = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}

def printik(game):
  game1 = ''

  for i in list(game.values()):
    if len(game1) == 6 or len(game1) == 13:
      game1 += '\n'
    game1 += i+' '
  print(game1)


printik(game)
print("""
Now choose numbers from 1 to 9 to play!
""")

unused_num = [1,2,3,4,5,6,7,8,9]
used_num = []

for i in range(1,10):
  game[i] = '-'

while True:

  position = int(input())
  print()
  if not 1<= position <= 9 or position in used_num:
     print("""
Wrong input dude
     """)
     sys.exit()
     

  game[position] = person_choice
  
  if game[1] == game[2] == game[3] == person_choice or\
     game[4] == game[5] == game[6] == person_choice or\
     game[7] == game[8] == game[9] == person_choice or\
     game[1] == game[4] == game[7] == person_choice or\
     game[2] == game[5] == game[8] == person_choice or\
     game[3] == game[6] == game[9] == person_choice or\
     game[1] == game[5] == game[9] == person_choice or\
     game[3] == game[5] == game[7] == person_choice :
    printik(game)
    print("""
You Won, Congrats!
    """)
    break
  

  if not '-' in list(game.values()):
     printik(game)
     print("""
It\'s a draw
     """)
     break
  

  used_num.append(position)

  unused_num.remove(position)
  comp_num_random = random.choice(unused_num)
  unused_num.remove(comp_num_random)
  game[comp_num_random] = computer_choice
  printik(game)

  
  used_num.append(comp_num_random)
  #print(used_num)
  #print(unused_num)
  
  if game[1] == game[2] == game[3] == computer_choice or\
     game[4] == game[5] == game[6] == computer_choice or\
     game[7] == game[8] == game[9] == computer_choice or\
     game[1] == game[4] == game[7] == computer_choice or\
     game[2] == game[5] == game[8] == computer_choice or\
     game[3] == game[6] == game[9] == computer_choice or\
     game[1] == game[5] == game[9] == computer_choice or\
     game[3] == game[5] == game[7] == computer_choice :
    print("""
gg! Try your luck next time!
    """)
    break
  

print("""Thanks for playing yo
""")