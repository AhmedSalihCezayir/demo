class Student():
  def __init__(self, name, age, id):
    super.__init__(name, age)
    self.id = id
    
  def say_name(self):
    print("My name is: ", self.name, " and my id is: ", self.id)
    print("Thats all")
    print("Thats all")
    
  def info_dump_different(self):
    self.say_name()
    self.say_age()
    print("Thats all")
