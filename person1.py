class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def my_func(abc):
    print("Hello my name is " + abc.name )

p1 = Person("Josh", 36)
p1.my_func()