import sys, time
def intro():
    print 'Welcome to ...'
    time.sleep(3)
    print 'A game about exploding bananas with guns!' #WIP line there
    print 'Press enter to continue.',
    raw_input()

def s_q(banana_ate, can_eat, location, times_first_move):
    banana_ate = banana_ate
    can_eat = can_eat
    location = location
    times_first_move = times_first_move
    input = raw_input('>')
    if input == '?':
        print 'You put on a quizzical look, before deciding to shout for help. Use \'help\' without the speech marks'
        can_eat = 0
    elif input == 'look':
        print 'You suddeny notice that you can see your nose, but it is a bit blurry. How odd that you never noticed it before.'
        can_eat = 0
    elif input == 'help':
        print '? or help: Display help'
        print 'look or look around: Get a description of your surrounds'
        print 'go: Move about in the world.'
        print 'quit or exit: Exit the game'
        can_eat = 0
    elif input == 'look around':
        if location == 0:
            if banana_ate == 0:
                print 'You are in a computer. A banana runs at you'
                can_eat = 1
            elif banana_ate == 1:
                print 'You are in a computer. A banana does most definatly not run at you.'
                can_eat = 0
        elif location == 1:
            print 'You are in a computer, north of where you were. There is a wall of fire just in front of you.' 
    elif input == 'exit':
        print 'Now exiting!'
        sys.exit()
        can_eat = 0
    elif input == 'quit':
        print 'Now exiting!'
        sys.exit()
        can_eat = 0
    elif input == 'eat banana' and can_eat == 1:
        print 'You eat the banana. You think that it disagreed you by exploding in your throat.'
        banana_ate = 1
        can_eat = 0
    elif input == 'eat it' and can_eat == 1:
        print 'You eat the banana. You think that it disagreed you by exploding in your throat.'
        banana_ate = 1
        can_eat = 0
    elif input == 'eat':
        print 'Eat what?'
        can_eat = 0
    elif input == 'go west':
        print 'Woo!'
        can_eat = 0
    elif input == 'go w':
        print 'Woo!'
        can_eat = 0
    elif input == 'go':
        print 'Go where?'
        can_eat = 0
    elif input == 'go north' and location == 0:
        if times_first_move == 0:
            print 'You cannot move there.'
            times_first_move = 1
        elif times_first_move == 1:
            print 'Are you sure? It looks dangorous.'
            times_first_move = 2
        elif times_first_move == 2:
            print 'It\'s dangorous to go alone! Don\'t go!'
            times_first_move = 3
        elif times_first_move == 3:
            print 'It looks just the same, and too much moving to an identical place is bad for you!'
            times_first_move = 4
        elif times_first_move == 4:
            print 'Fine, go.'
            location = 1
            times_first_move = 5
        elif times_first_move == 5:
            print 'You already went north! You practally hit a wall! As a matter of fact, why not look around again?'
        can_eat = 0
    elif input == 'go n' and location == 0:
        if times_first_move == 0:
            print 'You cannot move there.'
            times_first_move = 1
        elif times_first_move == 1:
            print 'Are you sure? It looks dangorous.'
            times_first_move = 2
        elif times_first_move == 2:
            print 'It\'s dangorous to go alone! Don\'t go!'
            times_first_move = 3
        elif times_first_move == 3:
            print 'It looks just the same, and too much moving to an identical place is bad for you!'
            times_first_move = 4
        elif times_first_move == 4:
            print 'Fine, go.'
            location = 1
            times_first_move = 5
        elif times_first_move == 5:
            print 'You already went north! You practally hit a wall! As a matter of fact, why not look around again?'
        #Buggy code 1 line above.
        can_eat = 0
    elif input == 'go east':
        print 'You cannot move there'
        can_eat = 0
    elif input == 'go e':
        print 'You cannot move there'
        can_eat = 0
    elif input == 'go west':
        print 'You cannot move there'
        can_eat = 0
    elif input == 'go w':
        print 'You cannot move there'
        can_eat = 0
    else:
        print 'INVALID QUERY!'
        can_eat = 0
    s_q(banana_ate, can_eat, location, times_first_move)