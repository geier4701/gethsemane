import os

from BLL.ShipFactory import ShipFactory
from UI.Loaders import load_ship
from UI.ValidUserInput import validate_list_input


def main():
	running = True
	
	while running:
		valid = False
		user_choice: str
		
		while not valid:
			print("1) Create ship")
			print("2) Load ship")
			print("3) Exit")
			user_choice = input()
			valid = validate_list_input(3, user_choice)
		
		if user_choice is "1":
			os.system('cls')
			ship_factory = ShipFactory()
			ship_factory.create_ship()
		elif user_choice is "2":
			os.system('cls')
			ship = load_ship()
		elif user_choice is "3":
			running = False


if __name__ == '__main__':
	main()
