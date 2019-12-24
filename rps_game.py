print('Welcome to Rock|Paper|Sccissor game...')
while 1:
    #Getting players' names
    p1=input('Enter player1\'s name :')
    p2=input('Enter player2\'s name :')
    while 1:
        #Obtaining whether rock/paper/sccissor
        #Here, 'r' stands for rock; 'p' stands for paper and 's' stands for sccissor
        choice1=input('What\'s your choice, %s? (r/p/s)'%p1)
        choice2=input('What\'s your choice, %s? (r/p/s)'%p2)
        if choice1!=choice2:
            break
        else:
            print('Draw!!! Kindly replay...')
    if choice1=='p' and choice2=='r':
        print(p1,'wins')
    elif choice1=='r' and choice2=='s':
        print(p1,'wins')
    elif choice1=='s' and choice2=='p':
        print(p1,'wins')
    else:
        print(p2,'wins')
    con=input('Do you want to continue? (y/n)')
    if con!='y':
        break
print('Thanks for playing %s and %s. Have a nice day'%(p1,p2))
