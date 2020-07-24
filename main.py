import random
import math
import gameclass.skills as gs

from gameclass.playerclass import player


player1 = player('player1', 100, 50, 30, 15, [gs.skill1, gs.dotdmg1], [], 0)
player2 = player('player2', 100, 80, 15, 10, [gs.heal1, gs.dotheal1], [], 0)
player3 = player('player3', 100, 80, 25, 25, [gs.fulldfs1, gs.stun1], [], 0)
playerlist = [player1, player2, player3]                    

enemy1 = player('enemy1', 100, 50, 30, 10, [], [], 0)
enemy2 = player('enemy2', 100, 50, 30, 10, [], [], 0)
enemylist = [enemy1, enemy2]

running = 0
while running == 0:
    zerohpplayers = 0          # counts how many of our players are dead
    
    for player in playerlist:
        player.statsbar()
    for enemy in enemylist:
        enemy.statsbar()

    
    for player in playerlist:
        if player.hp > 0: # player can only choose actions if they're alive
            playerrun = 0
            while playerrun == 0:
                player.actions()
                actioninput = input('choose action\n')
                enmatkl = []
                for enemy in enemylist:
                    # at the start of every player's attack, create a list of enemies still alive
                    if enemy.hp > 0:
                        enmatkl.append(enemy)
                if int(actioninput) == 1:
                    # basic attack
                    basedamage = random.randrange(math.floor(0.9 * player.dmg), math.ceil(1.1 * player.dmg))
                    for enemy in enmatkl:
                        print(str(enmatkl.index(enemy) + 1) + ':' + enemy.name) # print list of enemies player can attack
                    enmatkind = int(input('choose an enemy to attack\n')) - 1
                    playerdamage = basedamage - enmatkl[enmatkind].dfs
                    if playerdamage <= 0:
                        playerdamage = 0
                    # generate damage 0.9 - 1.1 of our player's
                    print(player.name, 'dealt', playerdamage, 'damage')
                    enmatkl[enmatkind].dmgreceive(playerdamage)
                    playerrun = 1   # player's action stops after performing an attack
                elif int(actioninput) == 2:
                    player.skillindex()
                    sklinput = int(input('choose skill\n')) - 1
                    if player.mp > player.skills[sklinput]['mpcost']:
                        player.manalose(player.skills[sklinput]['mpcost'])
                        if player.skills[sklinput]['type'] == 'attack':
                            # check to see if our skill is an attack type or heal type
                            for enemy in enmatkl:
                                print(str(enmatkl.index(enemy) + 1) + ':' + enemy.name)
                            enmatkind = int(input('choose an enemy to attack\n')) - 1
                            playerdamage = player.skills[sklinput]['dmg'] - enmatkl[enmatkind].dfs
                            if playerdamage <= 0:
                                playerdamage = 0
                            print(player.name, 'dealt', playerdamage, 'damage')
                            enmatkl[enmatkind].dmgreceive(playerdamage)
                        elif player.skills[sklinput]['type'] == 'heal':
                            heallist = []
                            # list of healable players
                            healindex = 1
                            for ply in playerlist:
                                if ply.hp > 0:
                                    heallist.append(ply)
                                    print(str(healindex) + ':' + ply.name)
                                    healindex += 1
                            healchoose = int(input('choose a player to heal\n')) - 1
                            heallist[healchoose].dmgheal(player.skills[sklinput]['dmg'])
                        elif player.skills[sklinput]['type'] == 'dotdmg':
                            # for when dps class does DOT damage to enemies
                            for enemy in enmatkl:
                                print(str(enmatkl.index(enemy) + 1) + ':' + enemy.name)
                            enmatkind = int(input('choose an enemy to attack\n')) - 1
                            enmatkl[enmatkind].dotlist.append(player.skills[sklinput])
                            print(player.name, 'casted', player.skills[sklinput]['name'],
                                  'on', enmatkl[enmatkind].name)
                        elif player.skills[sklinput]['type'] == 'dotheal':
                            # for when healer class heals, but per turn
                            heallist = []
                            # list of healable players
                            healindex = 1
                            for ply in playerlist:
                                if ply.hp > 0:
                                    heallist.append(ply)
                                    print(str(healindex) + ':' + ply.name)
                                    healindex += 1
                            healchoose = int(input('choose a player to heal\n')) - 1
                            heallist[healchoose].dotlist.append(player.skills[sklinput])
                            print(player.name, 'casted', player.skills[sklinput]['name'], 'on',
                                 heallist[healchoose].name)
                        elif player.skills[sklinput]['type'] == 'alldefense':
                            # for when tanker class casts his defense type on all party members
                            for p in playerlist:
                                if p.hp > 0:
                                    p.dotlist.append(player.skills[sklinput])
                                    p.dfs += player.skills[sklinput]['dmg']
                            print(player.name, 'casted', player.skills[sklinput]['name'], 'on all party members')
                        elif player.skills[sklinput]['type'] == 'stun':
                            # for when dps class does DOT damage to enemies
                            for enemy in enmatkl:
                                print(str(enmatkl.index(enemy) + 1) + ':' + enemy.name)
                            enmatkind = int(input('choose an enemy to attack\n')) - 1
                            if enmatkl[enmatkind].stuncounter < player.skills[sklinput]['stun duration']:
                                # if a previous stun skill during the same turn by another player
                                # stuns for more than the current's skill stun duration,
                                # then we don't change the stun duration
                                # since we don't want stuns to stack
                                enmatkl[enmatkind].stuncounter = player.skills[sklinput]['stun duration']
                            playerdamage = player.skills[sklinput]['dmg'] - enmatkl[enmatkind].dfs
                            if playerdamage <= 0:
                                playerdamage = 0
                            print(player.name, 'dealt', playerdamage, 'damage and stunned', enmatkl[enmatkind].name)
                            enmatkl[enmatkind].dmgreceive(playerdamage)
                        playerrun = 1
                    else:
                        print('not enough mp, back to action list')
                        # playerrun isn't set to 1, so loop continues and player keeps selecting action
                elif int(actioninput) == 3:
                    player.dfs *= 2
                    player.dotlist.append({'type': 'block'})
                    playerrun = 1
                else:
                    # when player doesn't want to do anything
                    playerrun = 1
                enmatkl = []
                for enemy in enemylist:
                    # we check if there is any enemy with positive hp, if not, then players win
                    if enemy.hp > 0:
                        enmatkl.append(enemy)
                if enmatkl == []:           # if there are no enemies to attack, players have won
                    running = 1  # code stops when enemy1 reaches 0 hp first
                    break
        if running == 1:
            # if at a player's turn all enemies are dead, we break the loop that cycles through all players
            break
        
    for enemy in enemylist:
        attacklist = []
        for player in playerlist:
            # some players might have 0 hp, so we create a list of attackable players for the enemy
            # which consists of players with hp greater than 0
            if player.hp > 0:
                attacklist.append(player)
        if enemy.hp > 0 and attacklist != [] and enemy.stuncounter == 0:
             # enemy can only attack if they're alive, at least a player is alive, and if they're not stunned
             targplyindex = random.randrange(0, len(attacklist))       # targets random player in playerlist
             enemydamage = enemy.dmg - attacklist[targplyindex].dfs
             if enemydamage < 0:
                    # sometimes player defense might fully mitigate enemy damage into negatives,
                    # in which case it might actually heal players, which we don't want
                    # so we set the damage to zero
                    enemydamage = 0
             print(enemy.name, 'attacks')
             attacklist[targplyindex].dmgreceive(enemydamage)
        elif enemy.hp > 0 and enemy.stuncounter > 0:
            enemy.stuncounter -= 1 # if enemy is stunned, then for next turn, we reduce the stuncounter by 1
    
    print('\n--------')
    # at the end of the turn, we deal all the damage over time skills (and heals) to players and enemies
    
    for player in playerlist:
        if player.hp > 0 and player.dotlist != []:
            for i in player.dotlist:
                if i['type'] == 'dotheal' and i['turns'] > 0:
                    player.dmgheal(i['dmg'])
                    i['turns'] -= 1
                    if i['turns'] == 0:
                        player.dotlist.pop(player.dotlist.index(i))
                elif i['type'] == 'block':
                    # if player blocks for the turn, then this returns their defense back to normal
                    # for the next turn
                    player.dfs = player.maxdfs
                    player.dotlist.pop(player.dotlist.index(i))
                elif i['type'] == 'alldefense':
                    # same concept as above
                    player.dfs = player.maxdfs
                    player.dotlist.pop(player.dotlist.index(i))
                    
    for enemy in enemylist:
        if enemy.hp > 0 and enemy.dotlist != []:
            for i in enemy.dotlist:
                if i['type'] == 'dotdmg' and i['turns'] > 0:
                    enemy.dmgreceive(i['dmg'])
                    i['turns'] -= 1
                    if i['turns'] == 0:
                        enemy.dotlist.pop(enemy.dotlist.index(i))
    
    enmatkl = []
    for enemy in enemylist:
        # we check if there is any enemy with positive hp, if not, then players win
        if enemy.hp > 0:
            enmatkl.append(enemy)
        if enmatkl == []:           # if there are no enemies to attack, players have won
            print('you won')
            break         

    for player in playerlist:
        # checks how many of our party members are dead every loop
        if player.hp == 0:
            zerohpplayers += 1
     
    if zerohpplayers == len(playerlist):
        # set running to 1 which breaks the loop, when everyone in our party is dead
        running = 1
        print('you lost')                       
