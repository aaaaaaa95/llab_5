from collections import namedtuple
#Define Student using namedtuple
Student = namedtuple("Student", ["name", "age", "marks"])
s1 = Student("Anita", 21, 85)
print(s1)                           #Student(name='Anita', age='21', marks="85")
print(s1.name)                      #Access 
print(s1[2])