from random import randint
from character import Character
from player import Player,Commands
 
if __name__=="__main__":
	p = Player()
	p.name = input("Tur character tur nam ki? ")
	print("(type help to get a list of actions)\n")
	print("%s enters a dark cave, searching for GOLD." % p.name)
	 
	while(p.health > 0):
		line = input("> ")
		args = line.split()
		if len(args)> 0:
			commandFound = False
			for c in list(Commands.keys()):
				if args[0] == c[:len(args[0])]:
					Commands[c](p)
					commandFound = True
					break
			if not commandFound:
				print("%s doesn't understand the suggestion." % p.name)
 

