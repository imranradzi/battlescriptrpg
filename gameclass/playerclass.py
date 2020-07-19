


class player:
    def __init__(self, name, hp, mp, dmg, skills):
        self.name = name
        self.maxhp = hp
        self.hp = hp                # two hp, this one's for taking damage
        self.maxmp = mp
        self.mp = mp                # same concept as hp
        self.dmg = dmg
        self.skills = skills        # we'll use a list/dictionary to store skills

    def statsbar(self):
        # function to print out name, hp and mp of whichever player
        print(str(self.name) + "| HP:", str(self.hp) + "/" + str(self.maxhp), "| MP:",
              str(self.mp) + "/" + str(self.maxmp) +"\n")

    def actions(self):
        # prints out list of actions player can do
        print("actions:\n 1. attack\n 2. skills\n 3. do nothing")

    def dmgreceive(self, damagetaken):
        self.hp -= damagetaken
        if self.hp < 0:
            self.hp = 0
            
    def dmgheal(self, damageheal):
        self.hp += damageheal
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def manalose(self, manaloss):
        self.mp -= manaloss
        if self.mp < 0:
            self.mp = 0
            
    def skillindex(self):
        for skill in self.skills:
            print(str((self.skills.index(skill) + 1)) + ':', skill['name'])

