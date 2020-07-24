import math


class player:
    def __init__(self, name, hp, mp, dmg, dfs, skills, dotlist):
        self.name = name
        self.maxhp = hp
        self.hp = hp                # two hp, this one's for taking damage
        self.maxmp = mp
        self.mp = mp                # same concept as hp
        self.maxdmg = dmg
        self.dmg = dmg
        self.maxdfs = dmg
        self.dfs = dfs              # player defense which mitigates damage
        self.skills = skills        # we'll use a list/dictionary to store skills
        self.dotlist = []

    def statsbar(self):
        # function to print out name, hp and mp of whichever player
        # percentage of player's hp and mp left
        hppercent = math.ceil((self.hp/self.maxhp) * 100)   
        mppercent = math.ceil((self.mp / self.maxmp) * 100)
        # the number of bars representing how much more hp and mp our player has
        hpbarsquantity = int((hppercent/100 * 20))
        mpbarsquantity = int((mppercent/100 * 10))
        print(str(self.name) + ((10-(len(str(self.name)))) * ' ') +
              '| HP:', (' ' * (3 - (len(str(self.hp))))) + str(self.hp) + '/' + str(self.maxhp),       
              ('█' * hpbarsquantity) + (' ' * (20 - hpbarsquantity)),                                  
              '| MP:', (' ' * (2 - (len(str(self.mp))))) + str(self.mp) + '/' + str(self.maxmp),       
              ('█' * mpbarsquantity) + (' ' * (10 - mpbarsquantity)))
        ''' the blank bars are for formatting, since the statsbar might look messy, say if hp 100/100 turns
            to hp 90/100, the whole text shifts to the left so we want to avoid that '''
            
    def actions(self):
        # prints out list of actions player can do
        print('actions:\n 1. attack\n 2. skills\n 3. guard\n 4. do nothing')

    def dmgreceive(self, damagetaken):
        self.hp -= damagetaken
        if self.hp < 0:
            self.hp = 0
        print(self.name, 'has taken', damagetaken, 'damage, current hp is', self.hp)
            
    def dmgheal(self, damageheal):
        self.hp += damageheal
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        print(self.name, 'has healed for', damageheal, 'hp, current hp is', self.hp)

    def manalose(self, manaloss):
        self.mp -= manaloss
        if self.mp < 0:
            self.mp = 0
            
    def skillindex(self):
        for skill in self.skills:
            print(str((self.skills.index(skill) + 1)) + ':', skill['name'])

