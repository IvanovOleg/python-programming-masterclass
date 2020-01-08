# Challenge: Modify the Player class so that the player's scores
# are increased by one thousand every time their level increased by one.
# So if they jump two levels, they'll get a bonus of two thousand added to their score.
# If the player drops back a level, they'll lose one thousand for each level they drop back.
# They can't go below Level One, so your solution should prevent that from happening.

# The aim of this challenge is to practice properties, so although it may make more sense
# to add methods to increase and decrease the level, please don't do it that way - use a property. 

class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives
    
    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cann't be negative")
            self._lives = 0
        self._lives = lives
    
    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level < 1:
            print("Level value can't be less than 1")
            self._level = 1
        else:
            self._score += (level - self._level) * 1000
            self._level = level

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    @property
    def score(self):
        return self.score
    
    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self): # this method allows to print object data
        return "Name: {0.name}, Lives: {0.lives}, Level: {0._level}, Score: {0._score}".format(self)
