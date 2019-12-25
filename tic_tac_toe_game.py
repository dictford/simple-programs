tab=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
def tabprint(table):
    print('   ',1,2,3,sep='|',end='\n   ______\n')
    for i in range(3):
        print('\n',i+1,end=' |')
        for j in range(3):
            print(table[i][j],end='|')
def win_check(a):
    #row  and column checks
    for i in range(3):
        #row
        if a[i][0] == a[i][1] and a[i][0]==a[i][2] and a[i][0]!=' ':
            return 1
        #columns
        if a[0][i] == a[1][i] and a[0][i]==a[2][i] and a[0][i]!=' ':
            return 1
    #diagonal check
    if a[0][0]==a[1][1] and a[0][0]==a[2][2] and a[0][0]!=' ':
        return 1
    if a[0][2]==a[1][1] and a[0][2]==a[2][0] and a[0][2]!=' ':
        return 1
    return 0
print('Welcome to the classic TicTacToe Game...\n'+'*'*40)
#p1-player1 ; p2-player2
p1=input('Enter player1\'s name...   ')
p2=input('Enter player2\'s name...   ')
print('\n'+'*'*40)
tabprint(tab)
draw=0
loc=0 #loc stands for location (i.e. 11,13,21,32) in the matrix
used_locations=[]    #To prevent re-writing on the same location
for i in range(2,11):
    #To declare match draw
    if i>9:
        draw=1
        break
    
    if i%2==0:
        temp_choice,temp_player='x',p1 #Since Player1 starts the game always
    else:
        temp_choice,temp_player='o',p2
        
    print('\nIt\'s your turn now, %s'%temp_player)
    #Getting the location 
    if i==2:
        print('''The location is simply the index of the matrix shown above
    \tEx: '11' is the location of first cell in first row
    \t    '23' is the location of third cell in second row and vice versa''')
    print('Enter the location...',sep='',end='   ')
    loc=int(input())
    while loc in used_locations:
        print('****Sorry, you can\'t use that place. It\'s already taken****')
        loc=int(input('Re-enter the location, %s...'%temp_player))
    used_locations.append(loc)
    
    tab[loc//10-1][loc%10-1]=temp_choice
    tabprint(tab)
    if win_check(tab):
        break
    else:
        continue
print('\n\n','*'*30)
if draw:
    print('Match Draw!!!')
else:
    print('Congrats %s! You are the winner!'%temp_player)
print('\n\n','*'*30)