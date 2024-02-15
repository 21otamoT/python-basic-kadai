class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def check_adult(self,age):
    if age >=20:
      print(f"{self.age}歳なので、大人です。")
    else:
      print(f"{self.age}歳なので、大人ではありません。")

user1 = Human("一郎",10)
user2 = Human("二郎",20)
user3 = Human("三郎",30)
users = [user1, user2, user3]

for user in users:
  user.check_adult(user.age)