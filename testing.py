import os
import shop

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
		answer = input("введите номер ответа и нажмите ENTER ")
		if answer == "1":
			print("запуск игры ")
			start_game()
			break
		elif answer == "2":
			print("выход из игры ")
			break
	print("выходим из меню!")

def start_game():
	"""
	запуск игры
	игра контролируется переменной 
	"""
	player_name = "Пустобрех"
	player_money = 5
	player_xp = 0
	player_hp = 100
	player_potions_hp = 0
	is_game = True
	while is_game:
		os.system("cls")
		print(f"имя: {player_name}")
		print(f"камней: {player_money}")
		print(f"опыт: {player_xp}")
		print(f"жизни: {player_hp}")
		print(f"зелья жизни: {player_potions_hp}")
		print(f"{player_name} родъехал к развилке")
		print("1 - Поехать на гладиаторские бои")
		print("2 - Поехать играть в кости")
		print("3 - Поехать в лавку алхимика")
		answer = input("введите номер ответа и нажмите ENTER ")
		if answer == "1":
		 	print("вы поехали на гладиаторские бои")

		elif answer == "2":
		 	print("вы поехали играть в кости")

		elif answer == "3":
		 	shop.shop(player_name, player_money, player_xp, player_hp, player_potions_hp)

		input("нажмите ENTER")


show_menu()

