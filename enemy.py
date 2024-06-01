from main import enemy

class Boss(enemy):
  def __init__(self, name = "", health = 0, attack = 0, defense = 0):
    super().__init__(name, health, attack, defense)
    self.name = "Boss"
    self.health = 100
    self.attack = 10
    self.defense = 10
class Minion(enemy):
  def __init__(self, name = "", health = 0, attack = 0, defense = 0):
    super().__init__(name, health, attack, defense)
    self.name = "Minion"
    self.health = 10
    self.attack = 1
    self.defense = 1
    
