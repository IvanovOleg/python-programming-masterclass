from player import Player
from enemy import Enemy, Troll, Vampyre, VampyreKing

# tim = Player("Tim")
# random_monster = Enemy("Basic enemy", 12, 1)
# print(random_monster)

# random_monster.take_damage(4)
# print(random_monster)

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)
brother.take_damage(18)
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

dracula = Vampyre("Dracula")
print(dracula)
dracula.take_damage(4)
print(dracula)

print("-" * 40)
another_troll.take_damage(30)
print(another_troll)

while dracula._alive:
    dracula.take_damage(1)
    #print(dracula)

vlad = VampyreKing("Vlad")
print(vlad)

while vlad._alive:
    vlad.take_damage(4)


# print(tim.name)
# print(tim.lives)


# tim.lives -= 1
# print(tim.lives)

# print(tim)

# tim._set_level(3)
# print(tim)

# tim._set_level(2)
# print(tim)

# tim._set_level(0)
# print(tim)

# print(tim.get_name()) # getter
# tim.set_lives(300) # setter

# tim.score = 500
# print(tim)


