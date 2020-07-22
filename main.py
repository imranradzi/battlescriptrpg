import random
import math
import gameclass.skills as gs

from gameclass.playerclass import player


player1 = player('player1', 100, 50, 10, 30, [gs.skill1])
player2 = player('player2', 100, 80, 10, 15, [gs.heal1])
playerlist = [player1, player2]                    

enemy1 = player('enemy1', 100, 50, 10, 30, [])
enemy2 = player('enemy2', 100, 50, 10, 30, [])
enemylist = [enemy1, enemy2]

running = 0
while running == 0:
    zerohpplayers = 0          # counts how many of our players are dead
    
    for player in playerlist:
        player.statsbar()
    for enemy in enemylist:
        enemy.statsbar()

    playerrun = 0
    while playerrun == 0:
        for player in playerlist:
            if player.hp > 0: # player can only choose actions if they're alive
                player.actions()
                actioninput = input('choose action\n')
                enmatkl = []
                for enemy in enemylist:
                    # at the start of every player's attack, create a list of enemies still alive
                    if enemy.hp > 0:
                        enmatkl.append(enemy)
                if int(actioninput) == 1:
                    # basic attack
                    playerdamage = random.randrange(math.floor(0.9 * player.dmg), math.ceil(1.1 * player.dmg))
                    # generate damage 0.9 - 1.1 of our player's
                    for enemy in enmatkl:
                        print(str(enmatkl.index(enemy) + 1) + ':' + enemy.name) # print list of enemies player can attack
                    enmatkind = int(input('choose an enemy to attack')) - 1
                    enmatkl[enmatkind].dmgreceive(playerdamage)                                              
                    print(player.name, 'dealt', playerdamage, 'damage')
                    playerrun = 1   # player's action stops after performing an attack
                elif int(actioninput) == 2:
                    player.skillindex()
                    sklinput = int(input('choose skill\n')) - 1
                    if player.mp > player.skills[sklinput]['mpcost']:
                        if player.skills[sklinput]['type'] == 'attack':
                            # check to see if our skill is an attack type or heal type
                            player.manalose(player.skills[sklinput]['mpcost'])
                            for enemy in enmatkl:
                                print(str(enmatkl.index(enemy) + 1) + ':' + enemy.name)
                            enmatkind = int(input('choose an enemy to attack')) - 1
                            enmatkl[enmatkind].dmgreceive(player.skills[sklinput]['dmg'])
                            print(player.name, 'dealt', player.skills[sklinput]['dmg'], 'damage')
                        elif player.skills[sklinput]['type'] == 'heal':
                            player.manalose(player.skills[sklinput]['mpcost'])
                            player.dmgheal(player.skills[sklinput]['dmg'])
                            print(player.name, 'healed for', player.skills[sklinput]['dmg'], 'hp')
                        playerrun = 1
                    else:
                        print('not enough mp, back to action list')
                        # playerrun isn't set to 1, so loop continues and player keeps selecting action
                else:
                    # when player doesn't want to do anything
                    playerrun = 1
                for enemy in enemylist:
                    # we check if there is any enemy with positive hp, if not, then players win
                    if enemy.hp > 0:
                        enmatkl.append(enemy)
                if enmatkl == []:           # if there are no enemies to attack, players have won
                        print('you won')
                        running = 1  # code stops when enemy1 reaches 0 hp first
                        break             
        
    for enemy in enemylist:
        attacklist = []
        for player in playerlist:
            # some players might have 0 hp, so we create a list of attackable players for the enemy
            # which consists of players with hp greater than 0
            if player.hp > 0:
                attacklist.append(player)
        if enemy.hp > 0:
             targetplayerindex = random.randrange(0, len(attacklist))       # targets random player in playerlist
             attacklist[targetplayerindex].dmgreceive(enemy.dmg)   
     
    for player in playerlist:
        # checks how many of our party members are dead every loop
        if player.hp == 0:
            zerohpplayers += 1
     
    if zerohpplayers == len(playerlist):
        # set running to 1 which breaks the loop, when everyone in our party is dead
        running = 1
        print('you lost')                       



