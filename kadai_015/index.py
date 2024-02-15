class Human:
  def __init__(self):
    self.name = "一郎"
    self.age = 20

  def printinfo(self):
    print(f"名前は{self.name}で、{self.age}歳です。")

user = Human()
user.printinfo()