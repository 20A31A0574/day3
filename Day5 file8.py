from random import randint
choice=['rock','paper','scissor']
p_score=0
c_score=0
limit=3
while p_score!=limit and c_score!=limit:
    print('choose among the following:',choice)
    my_ch=input("player choice:").lower()
    if my_ch not in choice:
        print("Invalid input")
        continue
    comp_ch=choice[int(randint(0,2))]
    print(f"system choice:{comp_ch}")
    if my_ch==comp_ch:
        print("---DRAW---")
        continue
    if my_ch=='rock' and comp_ch=="scissor":
        p_score+=1
    elif my_ch=='paper' and comp_ch=='rock':
        p_score+=1
    elif my_ch=='scissor' and comp_ch=='paper':
        p_score+=1
    else:
        c_score+=1
    print(f'your score : {p_score},system score:{c_score}')
if p_score>c_score:
    print('you win')
else:
    print('system win')
