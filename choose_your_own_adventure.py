name = input('Type your name: ')
print('Welcome', name, 'to this adventure!')

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way do you want to go? ").lower()

if answer == 'left':
    answer = input('You come to a river, you can walk around it or swim across. Type walk to walk around it or swim to swim across: ')

    if answer == 'swim':
        print('You swam across and were eaten by an alligator.')
    elif answer == 'walk':
        print('You walked for many miles, ran out of water and you died')
    else:
        print('Not a valid option. you lose')

elif answer == 'right':
    answer = input('You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ')

    if answer == 'cross':
        answer = input(
            'You start crossing the bridge. It begins to shake more and more until the ropes break and you fall. You wake up in a cave. You see gold and an exit. Do you take the gold or go to the exit (gold/exit)? ')

        if answer == 'gold':
            print('You grab the gold and walk out the cave becoming a multi-billionaire')
        elif answer == 'exit':
            print(
                'You exit the cave and see a Hummer filled with models. you flag them down and they pick you up. You go to the club to party and the next day you won the lottery and became a multi-billionaire')
    elif answer == 'back':
        print('You go back and get picked up by a Hummer full of models.')
    else:
        print('Not a valid option. you lose')

else:
    print('Not a valid option. You lose.')

print('Thank you for playing', name)