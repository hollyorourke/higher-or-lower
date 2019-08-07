rand = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
guess = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i = 0
while i < 22:

    from random import randrange
    rand[i] =((randrange(13))+2)
    i = i+1

#print (rand)        
j = i+1
i = 0
    


while i < 20:




    if rand[i] < 11:
        print(rand[i])
    elif rand[i] == 11:
        print ('J')
    elif rand[i] == 12:
        print ('Q')
    elif rand[i] == 13:
        print ('K')
    elif rand[i] == 14:
        print ('A')    

    while True:
            
        guess[i] = input('Type H or L ')
        if guess[i].lower() not in ('h','l'):
            print ('Try again')
        else:
            break


        
    if guess[i] == 'h':
        if rand[i+1] <= rand[i]:
            print ('You lose')
            break
        if rand[i+1] > rand[i]:
            print ('Correct!')

    if guess[i] == 'l':
        if rand[i+1] >= rand[i]:
            print ('You lose')
            break
        if rand[i+1] < rand[i]:
            print ('Correct!')
    i = i+1

if i < 20:
    if rand[i+1] < 11:
        print('Sorry the next card was ' + str(rand[i+1]))
    elif rand[i+1] == 11:
        print ('Sorry the next card was J')
    elif rand[i+1] == 12:
        print ('Sorry the next card was Q')
    elif rand[i+1] == 13:
        print ('Sorry the next card was K')
    elif rand[i+1] == 14:
        print ('Sorry the next card was A')
else:
    
    if rand[i] < 11:
        print(rand[i])
    elif rand[i] == 11:
        print ('J')
    elif rand[i] == 12:
        print ('Q')
    elif rand[i] == 13:
        print ('K')
    elif rand[i] == 14:
        print ('A')    
    print('You made it to the end!')
    
print('Your score is ' + str(i))


