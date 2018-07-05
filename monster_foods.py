

class MonsterFood(object):

    eats = 'food'

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' speaks')

    def eat(self, meal):
        if meal == self.eats:
            print('yum!')
        else:
            print('blech!')

# my_monster = MonsterFood('Spooky Snack')
# my_monster.speak()
# my_monster.eat('food')



class FrankenBurger(MonsterFood):

    eats = 'hamburger patties'

    def speak(self):
        print('My name is ' + self.name + 'Burger')


class CrummyMummy(MonsterFood):

    eats = 'chocolate chips'

    def speak(self):
        print('My name is ' + self.name + 'Mummy')

class WereWatermelon(MonsterFood):

    eats = 'watermelon juice'

    def speak(self):
        print('My name is Were' + self.name)

# my_monster = FrankenBurger('Veggiesaurus')
# my_monster.speak()
# my_monster.eat('pickles')


monster_selection = input('What kind of monster food do you want to create? Select: frankenburger, crummymummy, or werewatermelon')
monster_name = input('What do you want to name your monnster?')
monster_meal = input('What will you feed your monster?')


if monster_selection == 'frankenburger':
    monster_type = FrankenBurger
elif monster_selection == 'crummymummy':
    monster_type = CrummyMummy
elif monster_selection == 'werewatermelon':
    monster_type = WereWatermelon
else:
    monster_type = MonsterFood


my_monster = monster_type(monster_name)
my_monster.speak()
my_monster.eat(monster_meal)


