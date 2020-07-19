import random

from gameclass.playerclass import player
from gameclass.skills import skill1


player1 = player('player1', 100, 50, 30, [skill1])
playerlist = [player1]                          # planning on including many players in the future

enemy1 = player('enemy1', 100, 50, 30, [])

running = 0
while running == 0:
    zerohpplayers = 0          # counts how many of our players are dead
    
    for player in playerlist:
        player.statsbar()
    enemy1.statsbar()

    for player in playerlist:
        player.actions()
        actioninput = input('choose action\n')
        if int(actioninput) == 1:
            # basic attack
            playerdamage = random.randrange(0.9 * player.dmg, 1.1 * player.dmg)          # generate damage 0.9 - 1.1 of our player's 
            enemy1.dmgreceive(playerdamage)                                                # base damage
            print('player1 dealt', playerdamage, 'damage')
        elif int(actioninput) == 2:
            player.skillindex()
            skillinput = int(input('choose skill\n')) - 1
            for i in player.skills:
                runnableskills = 0 # counter of how many skills we can do considering our mp
                if player.mp > i['mpcost']:
                    runnableskills += 1
            if runnableskills > 0:
                player.manalose(player.skills[skillinput]['mpcost'])
                enemy1.dmgreceive(player.skills[skillinput]['dmg'])
                print('player1 dealt', player.skills[skillinput]['dmg'], 'damage')
            else:
                print('not enough mp, proceeding to do nothing')
    if enemy1.hp == 0:
                print('you won')
                running = 1  # code stops when enemy1 reaches 0 hp first
                
                
    if enemy1.hp > 0:
         targetplayerindex = random.randrange(0, len(playerlist))       # targets random player in playerlist
         playerlist[targetplayerindex].dmgreceive(enemy1.dmg)   
     
    for player in playerlist:
        # checks how many of our party members are dead every loop
        if player.hp == 0:
            zerohpplayers += 1
     
    if zerohpplayers == len(playerlist):
        # set running to 1 which breaks the loop, when everyone in our party is dead
        running = 1
        print('you lost')                       



