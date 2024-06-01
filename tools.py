from main import tools

class weapons(tools):
  def __init__(self, type = "", use = "", name = [], damage = 0):
    super().__init__(type, use, name, damage)
    self.type = "Weapon"
    self.use = "Attack"
    self.damage = damage
    self.name = name
class armor(tools):
  def __init__(self, type = "", use = "", name = [], damage = 0):
    super().__init__(type, use, name, damage)
    self.type = "Armor"
    self.use = "Defense"
    self.damage = damage
    self.name = name
