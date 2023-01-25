from random import randint
print("1.Rock\n 2.paper\n 3.scissor")
choice=int(input())
while choice>3 or choice<1:
           print("Enter your choice again")
           choice=int(input('enter your choice:'))
if choice==1:
    choice_name='rock'
elif choice==2:
    choice_name='paper'
else:
    choice_name='scissor'
print('Now computers choice')
print("Computer choice is \n", comp_choice)

comp_choice=randint(1,3)
if choice == comp_choice:
        print('Its a Draw',end="")
        result="DRAW"

if (choice==1 and comp_choice==2):
        print('paper wins ',end="")
        result='papeR'
elif (choice==2 and comp_choice==1):
        print('paper wins ',end="")
        result='Paper'
        
        
if (choice==1 and comp_choice==3):
        print('Rock wins \n',end= "")
        result='Rock'
elif (choice==3 and comp_choice==1):
        print('Rock wins \n',end= "")
        result='rocK'
         
if (choice==2 and comp_choice==3):
        print('Scissors wins ',end="")
        result='scissoR'
elif (choice==3 and comp_choice==2):
        print('Scissors wins ',end="")
        result='Rock'

if result == 'DRAW':
        print(" tie ")
if result == choice_name:
        print(" User wins ")
else:
    print(" Computer wins ")
    print("Do you want to play again? (Y/N)")

    ans = input().lower
if ans =='n':
    break

