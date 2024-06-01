from main import food
class rottenApple(food):
  def __init__(self, poison = False, name = "", heal = 0):
    super().__init__(poison, name, heal)
    self.poison = True
    self.name = "Rotten Apple"
    self.heal = -1
class apple(food):
  def __init__(self, poison = False, name = "", heal = 0):
    super().__init__(poison, name, heal)
    self.poison = False
    self.name = "Apple"
    self.heal = 1
class banana(food):
  def __init__(self, poison = False, name = "", heal = 0):
    super().__init__(poison, name, heal)
    self.poison = False
    self.name = "Banana"
    self.heal = 2
class rottenBanana(food):
  def __init__(self, poison = False, name = "", heal = 0):
    super().__init__(poison, name, heal)
    self.poison = True
    self.name = "Rotten Banana"
    self.heal = -2
class bread(food):
  def __init__(self, poison = False, name = "", heal = 0):
    super().__init__(poison, name, heal)
    self.poison = False
    self.name = "Bread"
    self.heal = 3
class moldyBread(food):
  def __init__(self, poison = False, name = "", heal = 0):
    super().__init__(poison, name, heal)
    self.poison = True
    self.name = "Moldy Bread"
    self.heal = -3
class peach(food):
  def __init__(self, poison = False, name = "", heal = 0):
    super().__init__(poison, name, heal)
    self.poison = False
    self.name = "Peach"
    self.heal = 4
class rottenPeach(food):
  def __init__(self, poison = False, name = "", heal = 0):
    super().__init__(poison, name, heal)
    self.poison = True
    self.name = "Rotten Peach"
    self.heal = -4
class steak(food):
  def __init__(self, poison = False, name = "", heal = 0):
    super().__init__(poison, name, heal)
    self.poison = False
    self.name = "Steak"
    self.heal = 5
class spoiledSteak(food):
  def __init__(self, poison = False, name = "", heal = 0):
    super().__init__(poison, name, heal)
    self.poison = True
    self.name = "Spoiled Steak"
    self.heal = -5
class superSteak(food):
  def __init__(self, poison = False, name = "", heal = 0):
    super().__init__(poison, name, heal)
    self.poison = False
    self.name = "Super Steak"
    self.heal = 10
