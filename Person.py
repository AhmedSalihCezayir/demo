class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def say_name(self):
    print("My name is: ", self.name)
    
  def say_age(self):
    print("My age is: ", self.age)
    
  def info_dump(self):
    self.say_name()
    self.say_age()
    print("Thats all")
