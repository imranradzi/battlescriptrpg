from gameclass.playerclass import player


player1 = player("player1", 100, 50, 30, [])
enemy1 = player("enemy1", 100, 50, 30, [])
running = 0
while running == 0:
    player1.statsbar()
    enemy1.statsbar()

    player1.actions()
    actioninput = input("choose action\n")
    if int(actioninput) == 1:
        enemy1.dmgreceive(player1.dmg)
        if enemy1.hp == 0:
            print("you won")
            break                               # code stops when enemy1 reaches 0 hp first
    player1.dmgreceive(enemy1.dmg)
    if player1.hp == 0:
        running = 1
        print("you lost")                       # same as above, except while loop stops since running != 0



