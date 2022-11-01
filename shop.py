import os
import game
def buy_potion(player_potions_hp):
    player_potions_hp += 1
    return player_potions_hp
def buy_potion_money(player_money):
    player_money -= 5
    return player_money

def shop(player_name, player_money, player_xp, player_hp, player_potions_hp):
    while True:
        os.system("cls")
        print(f"{player_name} приезжает в лавку")
        print(f"имя: {player_name}")
        print(f"камней: {player_money}")
        print(f"опыт: {player_xp}")
        print(f"жизни: {player_hp}")
        print(f"зелья жизни: {player_potions_hp}")
        print("1 - купить зелье ")
        print("2 - Уехать к развилке")
        answer = input("введите номер ответа и нажмите ENTER: ")
        if answer == "1":
                print("вы смотрите зелья  ")
                print("на полке оказалось всего несколько зелий жизни по 5 монет")
                print("1 - купить?")
                print("2 - отказаться")
                answer = input("введите номер ответа и нажмите ENTER: ")
                if answer == "1":
                    if player_money >= 5:
                        print("вы купили одно зелье жизни")
                        player_money = buy_potion_money(player_money)
                        player_potions_hp = buy_potion(player_potions_hp) 
                        input("нажмите ENTER")
                    else:
                        print("у вас не осталось денег...")
                        input("нажмите ENTER")


                elif answer == "2":
                    print("вы отказались")
                    input("нажмите ENTER")
                

        elif answer == "2":
            print("вы уехали к развилке")
            break
            rvilka_1()
    return
print("выходим из меню!")