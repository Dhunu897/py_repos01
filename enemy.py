from character import Character
from random import randint

class Enemy(Character):
  def __init__(self, player):
    Character.__init__(self)
    self.name = 'Gold Smuggler'
    self.health = randint(1, player.health)
    self.wealth=randint(1,player.wealth)

