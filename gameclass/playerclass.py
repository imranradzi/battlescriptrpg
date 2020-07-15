


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
        print(str(self.name) + "| HP:", str(self.hp) + "/" + str(self.maxhp), "| MP:",
              str(self.mp) + "/" + str(self.maxmp) +"\n")

    def actions(self):
        print("actions:\n 1. attack\n 2. do nothing")

    def dmgreceive(self, damagetaken):
        self.hp -= damagetaken
        if self.hp < 0:
            self.hp = 0


