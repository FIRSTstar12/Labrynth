class player():
  def __init__(self, name = "", health = 0, attack = 0, defense = 0):
    self.name = name
    self.heath = health
    self.attack = attack
    self.defense = defense
class enemy():
  def __init__(self, name = "", health = 0, attack = 0, defense = 0):
    self.name = name
    self.health = health
    self.attack = attack
    self.deffense = defense
class tools():
  def __init__(self, type = "", use = "", damage = 0):
    self.type = type
    self.use = use
    self.damage = damage
