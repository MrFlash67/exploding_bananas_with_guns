import sys, time, string, os, time, pickle as pck
os.chdir('Saves')
def intro():
    print 'ZORG. (os) presents:'
    time.sleep(3)
    print 'DOES NOT COMPUTE'
    print 'Press enter to continue.',
    raw_input()
    print 'You can now enter commands. Type \'help\' without the quotation marks and press \'enter\' for help'

def s_q(banana_ate, can_eat, location, times_first_move, eat_bug):
    banana_ate = banana_ate
    can_eat = can_eat
    location = location
    times_first_move = times_first_move
    eat_bug = eat_bug
    input = string.lower(raw_input('>'))
    if input == '?':
        print 'You put on a quizzical look, before deciding to shout for help. Use \'help\' without the speech marks'
        can_eat = 0
        eat_bug = 0
    elif input == 'look':
        print 'You suddeny notice that you can see your nose, but it is a bit blurry. How odd that you never noticed it before.'
        can_eat = 0
        eat_bug = 0
    elif input == 'help':
        print 'All commands are case-insensitive.'
        print '? or help: Display help'
        print 'look or look around: Get a description of your surrounds'
        print 'go: Move about in the world.'
        print 'save: Saves and exits your game'
        print 'quit or exit: Exit the game'
        can_eat = 0
        eat_bug = 0
    elif input == 'look around':
        if location == 0:
            if banana_ate == 0:
                print 'You are in a computer. A banana runs at you'
                can_eat = 1
            elif banana_ate == 1:
                print 'You are in a computer. A banana does most definatly not run at you.'
                can_eat = 0
                eat_bug = 0
        elif location == 1:
            print 'You are in a computer, north of where you were. There is a wall of fire just in front of you.'
        elif location == 2:
            print 'You are in a supply room. You see a TELNET FIRE EXTINGLISHER and a APPLE PLOT TOKEN. Better take both.'
    elif input == 'exit':
        print 'Now exiting!'
        sys.exit()
        can_eat = 0
        eat_bug = 0
    elif input == 'quit':
        print 'Now quitting!'
        sys.exit()
        can_eat = 0
        eat_bug = 0
    elif input == 'abort':
        print 'Abandon thread! Abandon ship! Red alert!'
        sys.exit()
        can_eat = 0
        eat_bug = 0
    elif input == 'eat banana' and can_eat == 1:
        print 'You eat the banana. You think that it disagreed you by exploding in your throat.'
        banana_ate = 1
        can_eat = 0
        eat_bug = 0
    elif input == 'eat it' and can_eat == 1:
        print 'You eat the banana. You think that it disagreed you by exploding in your throat.'
        banana_ate = 1
        can_eat = 0
        eat_bug = 0
    elif input == 'eat':
        print 'Eat what?'
        can_eat = 0
        eat_bug = 0
    elif input == 'go west' or input == 'go w':
        if location == 0 or location == 1:
            print 'You cannot move there.'
        elif location == 2:
            print 'Going back to the firewall!'
            location = 1
        can_eat = 0
        eat_bug = 0
    elif input == 'go':
        print 'Go where?'
        can_eat = 0
        eat_bug = 0
    elif input == 'go north' and location == 0:
        if times_first_move == 0 and location == 0:
            print 'You cannot move there.'
            times_first_move = 1
        elif times_first_move == 1 and location == 0:
            print 'Are you sure? It looks dangorous.'
            times_first_move = 2
        elif times_first_move == 2 and location == 0:
            print 'It\'s dangorous to go alone! Don\'t go!'
            times_first_move = 3
        elif times_first_move == 3 and location == 0:
            print 'It looks just the same, and too much moving to an identical place is bad for you!'
            times_first_move = 4
        elif times_first_move == 4 and location == 0:
            print 'Fine, go.'
            location = 1
            times_first_move = 5
        elif times_first_move == 5 and location == 1:
            print 'You already went north! You practally hit a wall! As a matter of fact, why not look around again?'
        elif times_first_move == 5 and location == 0:
            print 'Feel free to go back and get burned to a crisp on the firewall!'
            location = 1
        can_eat = 0
        eat_bug = 0
    elif input == 'go n' and location == 0:
        if times_first_move == 0 and location == 0:
            print 'You cannot move there.'
            times_first_move = 1
        elif times_first_move == 1 and location == 0:
            print 'Are you sure? It looks dangorous.'
            times_first_move = 2
        elif times_first_move == 2 and location == 0:
            print 'It\'s dangorous to go alone! Don\'t go!'
            times_first_move = 3
        elif times_first_move == 3 and location == 0:
            print 'It looks just the same, and too much moving to an identical place is bad for you!'
            times_first_move = 4
        elif times_first_move == 4 and location == 0:
            print 'Fine, go.'
            location = 1
            times_first_move = 5
        elif times_first_move == 5 and location == 1:
            print 'You already went north! You practally hit a wall! As a matter of fact, why not look around again?'
        #Buggy code 1 line above.
        elif times_first_move == 5 and location == 0:
            print 'Feel free to go back and get burned to a crisp on the firewall!'
            location = 1
        can_eat = 0
        eat_bug = 0
    elif input == 'go east' or input == 'go e':
        if location == 0:
            print 'You cannot move there'
        elif location == 1:
            print 'Going to the Emergency Inventory Room!'
            location = 2
        can_eat = 0
        eat_bug = 0
    elif input == 'go south' or input == 'go s':
        if location == 0:
            print 'You cannot move there'
        elif location == 1:
            print 'Do you really want to go back? It\'s boring back there.'
            go_back = raw_input('y [yes] or n [no]? \n')
            if go_back == 'y':
                location = 0
        else:
            s_q(banana_ate, can_eat, location, times_first_move, eat_bug)   
        can_eat = 0
        eat_bug = 0
    elif input == 'go through the fire' and location == 1:
        print 'You try, but it is too hot. A bug skuttles at you and you suddeny feel a bit sick for a second.'
        eat_bug = 1
        can_eat = 0
    #elif input == 'eat bug' and location == 1 and eat_bug == 1:
        #print 'You take a byte from the bug. It fizzles out halfway down your throat.'
        #can_eat = 0
        #eat_bug = 0
        #else:
            #print 'There is no bug, for better or for worse.'
    elif input == 'take':
        print 'Take what?'
        can_eat = 0
        eat_bug = 0
    elif input == 'steal':
        print 'I won\'t stop you, but what is there to steal?'
        can_eat = 0
        eat_bug = 0
    elif input == 'save':
        print 'Saving....'
        with open('save.txt', 'w') as f:
            saveData = {'banana_ate':int(banana_ate), 'can_eat':int(can_eat), 'location':int(location), 'times_first_move':int(times_first_move), 'eat_bug':int(eat_bug)}
            pck.dump( saveData, f)
            
        time.sleep(2)
        print 'Save complete!'
    elif input == 'load':
        print 'Loading...'
        with open('save.txt', 'r') as r:
            loadData = pck.load(open('save.txt', 'rb'))
        print str(loadData)
        banana_ate = loadData['banana_ate']
        eat_bug = loadData['eat_bug']
        location = loadData['location']
        times_first_move = loadData['times_first_move']
        eat_bug = loadData['eat_bug']
        time.sleep(2)
        print 'Loaded!'
        print 'Loading WIP!'
    else:
        print 'INVALID QUERY!'
        can_eat = 0
        eat_bug = 0
    s_q(banana_ate, can_eat, location, times_first_move, eat_bug)