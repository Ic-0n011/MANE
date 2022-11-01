import os
import game
def show_menu():
    """
    показывает главное меню
    из него начинается игра 
    или заканчивается програма.
    TODO:
        настройки:цвет игры,
        сохранение/загрузка
    """
    # главный цикл меню завершается выбором.
    while True:
        os.system("cls")
        print("новая игра-1")
        print("выйти-2")
        answer = input("введите номер ответа и нажмите ENTER: ")
        if answer == "1":
            print("запуск игры ")
            game.start_game()
            break
        elif answer == "2":
            print("выход из игры ")
            break
    print("выходим из меню!")

show_menu()

