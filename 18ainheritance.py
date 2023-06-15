#Inheritance
class Person:
      def __init__(self, firstname='John', lastname='Paul', age=25, country='India', city='Hyderabad'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('Tom', 'Jerry', 30, 'India', 'Banglore')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

class Student(Person):
    pass
s1 = Student('Emm', 'Wha', 30, 'India', 'Pune')
s2 = Student('Bob', 'Trudy', 28, 'India', 'Mumbai')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
#Overriding parent method

class Student(Person):
    def __init__ (self, firstname='John', lastname='Paul', age=25, country='India', city='Hyderabad', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)

    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Alice', 'Smiley', 30, 'India', 'Pune','female')
s2 = Student('Bob', 'Trudy', 28, 'India', 'Mumbai','male')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
