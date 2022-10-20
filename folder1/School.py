import folder1.objectXX as Student1
import folder1.objectX as Student2

class School(object):
  
  def __init__(self):
    self.studentA = Student1.Student("Ayse", 18)
    self.studentB = Student2.StudentX("Mert", 20)

  def big_func(self):
    print("hello")
    self.studentA.say_name()
    self.studentA.say_age()
    self.studentA.info_dump()

    self.studentB.say_name()
    self.studentB.say_age()
    self.studentB.info_dump()
    self.studentB.info_dump_different()
