# Challenge1: Create a new Vampire subclass that's a subclass of Enemy.
# Vampyres have 3 lives, and take 12 hitpoints of damage
# You can create a new python file for vampyre if you like, but I'd
# suggest adding it to the existing enemy.py file.
# Test your class by creating one or two Vampyre instances and
# displaying their details. Also inflict some damage to make sure
# the take_damage method works ok.
# Also make sure that the trolls can also take damage, because we
# haven't tested that yet.

# Challenge2: The challenge is to create a VampyreKing subclass of Vampyre.
# A VampyreKing is going to be icredibly powerful, and any points of damage
# inflicted will be devided by 4. VampyreKing object will also start with 140 hit points.
# So extend Vampyre to create a VampyreKing class with those additional properties.
# Test the new class by creating a new VampyreKing object and checking that id does
# start with 140 hit points and only takes a quarter of the damage inflicted.

import random

#class Enemy(object):
class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True
    
    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("I took {} damage and have {} left".format(damage, self._hit_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life".format(self))
            else:
                print("{0._name} is dead".format(self))
                self._alive = False
    
    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)


class Troll(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)
        #super(Troll, self).__init__(name=name, lives=1, hit_points=23)
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)
    
    def grunt(self):
        print("Me {0._name}. {0._name} stomp you".format(self))

class Vampyre(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)
    
    def dodge(self):
        if random.randint(1, 3) == 3:
            print("***** {0._name} dodges *****".format(self))
            return True
        else:
            return False
    
    def take_damage(self, damage):
        if not self.dodge():
            super().take_damage(damage=damage)

class VampyreKing(Vampyre):
    
    def __init__(self, name):
        super().__init__(name)
        self._hit_points = 140
    
    def take_damage(self, damage):
        if not self.dodge():
            super().take_damage(damage // 4) # or damage=damage/4
