from random import randint


class Human():
    def __init__(self, name,  hp1, hp2, damage1, damage2):
        self.hp = randint(hp1, hp2)
        self.damage = randint(damage1, damage2)
        self.name = name

b = 0
while(b != 1 and b != 2):
   # if b != 1 and b !=2:
    print("1  чи 2 ")
    b = int(input('  Виберіть тип героя: Archer - натисніть 1 далі enter  Swordsman -  натисніть 2 далі enter     ' ))


if b == 1:
    warrior = Human("Archer", 30, 80, 1, 5)
if b == 2:
    warrior = Human("Swordsman", 60, 120, 3, 8)
print(f"Створено воїна  {warrior.name}, HP {warrior.hp}, Damage {warrior.damage}")
bandit = Human("Bandit", 30, warrior.hp, 1, warrior.damage)
print(f"Створено Bandit  {bandit.name}, HP {bandit.hp}, Damage {bandit.damage}")




#while (warrior.hp > 0):

c = int(input(f'  Виберіть послідовність бою: перший б"є {warrior.name} - натисніть 1 далі enter  {bandit.name} -  натисніть 2 далі enter     ' ))
#print(warrior.name)


while(warrior.hp > 0 and bandit.hp > 0):


    if c % 2 == 1:

        warrior.hp = warrior.hp - bandit.damage
        print(f'{warrior.name} {warrior.hp}')
        print(f'{bandit.name} {bandit.hp}')

        #g = input("натисніть Enter для продовження   ")
    if c % 2 == 0:
        bandit.hp = bandit.hp - warrior.damage
        print(f'{warrior.name} {warrior.hp}')
        print(f'{bandit.name} {bandit.hp}')
    g = input("натисніть Enter для продовження   ")
    c +=1
if warrior.hp <= 0:
    print(f"vinner {bandit.name}")

if bandit.hp <= 0:
    print(f"vinner  {warrior.name}")