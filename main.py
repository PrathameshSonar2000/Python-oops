# oops
class A():  # class is a keyword
  name1 = "class variable"  #class instance variable
  def __init__(self,name2):  # __init__ is a constructor (magic/dundor method)
    self.name2 = name2  #instance variable
  
  def __str__(self):
    return "I am inside magic method str."

obj = A('instance variable')
print(obj)
print(obj.name1)
print(obj.name2)
obj.name1 = "class can change"
obj.name2 = "instance can change"
print(obj.name1)
print(obj.name2)
A.name1 = "class change again"
#A.name2 = "instance change again"  # it is not possible
print(obj.name1)
print(obj.name2)