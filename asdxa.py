from random import choice, randint


first_name = ("Жран","Дрын", "Жлыг")
last_name = ("Кривой", "Злопаметный", "Дикий")



def make_hero(
        name=None,
        hp_max=None,
        hp_now=None,
        lvl=1,
        xp_next=1000,
        xp_now=0,
        attack=1,
        defence=0,
        weapon=None,
        shield=None,
        luck=1,
        money=None,
        inventary=None,
) -> list:
    if not name:
        name = f"{choice(first_name)} {choice(last_name)}"
        hp_max = hp_now

    if not hp_now:
        hp_now = randint(1, 100)

    if money is None:
        money = randint(1, 100)

    if not inventary:
        inventary = []
    """
    Герой это список
    [0] name - имя персонажа
    [1] hp_max - жизнь максимум
    [2] hp_now - текущее кол во жизней
    [3] lvl - уровень персонажа
    [4] xp_nex - опыта для след уровня
    [5] xp_now - текущий опыт
    [6] attack - сила атаки
    [7] defence - защита
    [8] weapon - оружие
    [9] shield - щит
    [10] luck - удача
    [11] money - деньги
    [12] inventary - инвентарь список

    """
    return [name,
        hp_max,
        hp_now,
        lvl,
        xp_next,
        xp_now,
        attack,
        defence,
        weapon,
        shield,
        luck,
        money,
        inventary
    ]
def show_hero(hero: str) -> None:

    print("имя персонажа",hero[0] )
    print("жизни",hero[1], "/",hero[2])
    print("уровень персонажа",hero[3])
    print("текущий опыт",hero[5], "/",hero[4] )
    print("сила атаки",hero[6] )
    print("защита",hero[7] )
    print("оружие",hero[8] )
    print("щит",hero[9] )
    print("удача",hero[10] )
    print("деньги",hero[11] )
    print("инвентарь список",hero[12] )
    print("")

def levelup(hero):
    if hero[5] >= hero [4]:
        hero[3] += 1
        hero[4] (lvl*(lvl-1)/2)*1000
        print(f"{hero[0]} получил {hero[3]} уровень\n")



show_hero(p1)
show_hero(p2)


show_hero(p1)
show_hero(p2)

p2[5] += 1000
levelup(p2)

for i in p1:
    print(i) 
for i in p2:
    print(i) 