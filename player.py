from random import randint
from character import Character
from enemy import Enemy


class Player(Character):
  def __init__(self):
    Character.__init__(self)
    self.state = 'normal'
    self.health = 10
    self.health_max = 10
    self.wealth= 0
    #self.wealth_max=100
  def quit(self):
    print("%s .\nR.I.P... toi morili ses!!" % self.name)
    self.health = 0
  def help(self): print(list(Commands.keys()))
  def status(self): print("%s's health: %d/%d\n%s's wealth: %d gold bar" % (self.name, self.health, self.health_max,self.name,self.wealth))
  
  def tired(self):
    print("%s feels tired." % self.name)
    self.health = max(1, self.health - 1)
    
  def rest(self):
    if self.state != 'normal': print("%s can't rest now!" % self.name); self.enemy_attacks()
    else:
      print("%s rests." % self.name)
      if randint(0, 1):
        self.enemy = Enemy(self)
        print("%s is rudely awakened by a %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks()
      else:
        if self.health < self.health_max:
          self.health = self.health + 1
        else: print("%s slept too much." % self.name); self.health = self.health - 1

  def explore(self):
    if self.state != 'normal':
      print("%s is too busy right now!!" % self.name)
      self.enemy_attacks()
    else:
      print("%s explores an abandoned Lion Cave and finds a gold bar" % self.name)
      self.wealth+=1
      if randint(0, 1):
        self.enemy = Enemy(self)
        print("%s encounters %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
      else:
        if randint(0, 1): self.tired()
  def flee(self):
    if self.state != 'fight': print("%s flies in air for a while." % self.name); self.tired()
    else:
      if randint(1, self.health + 5) > randint(1, self.enemy.health):
        print("%s flees from %s." % (self.name, self.enemy.name))
        self.enemy = None
        self.state = 'normal'
      else: print("%s couldn't escape from %s!" % (self.name, self.enemy.name)); self.enemy_attacks()
  def attack(self):
    if self.state != 'fight': print("%s cuts off of few trees in a swing." % self.name); self.tired()
    else:
      if self.do_damage(self.enemy):
        print("%s executes %s and looots %s's gold !" % (self.name, self.enemy.name,self.enemy.name))
        self.enemy = None
        self.state = 'normal'
	self.wealth+=1
        if randint(0, self.health) < 10:
          self.health = self.health + 1
          self.health_max = self.health_max + 1
          if self.wealth<0:self.wealth=0
          print("%s feels tired." % self.name)
      else: self.enemy_attacks()
  def enemy_attacks(self):
    if self.enemy.do_damage(self): print("%s was slaughtered by %s!!!\nR.I.P...toi morili ses..tur khel khotom.!!!!" %(self.name, self.enemy.name))

Commands = {
  'quit': Player.quit,
  'help': Player.help,
  'status': Player.status,
  'rest': Player.rest,
  'explore': Player.explore,
  'flee': Player.flee,
  'attack': Player.attack,
  }



