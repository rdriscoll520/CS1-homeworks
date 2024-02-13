#Chapter 10 Homework 

#Question 1: Pet class
def main():
    name = input("Enter the name of your pet: ")
    animal_type = input("Enter the type of animal you have: ")
    age = input("Enter your pet's age: ")
    
    pet_info = Pet(name, animal_type, age)
    print(pet_info)
class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        
    def __str__(self):
        return f'Pet({self.__name}, {self.__animal_type}, {self.__age})'
    
    def set_name(self, name):
        self.__name = name
    
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
        
    def set_age(self, age):
        self.__age = age
    
    def get_name(self):
        return self.__name 
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age
    
main()

#Question 2: Car Class
def main():
    year_model = input("Enter the model year: ")
    make = input("Enter the make of the car: ")
    speed = 0
    car = Car(year_model, make, speed)
    
    for i in range(5):
        speed += car.accelerate()
    print(speed)
    
    for i in range (5):
        speed += car.brake()
    print(speed)
    
    print(car.get_speed())

class Car:
    def __init__(self, year_model, make, speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed
        
    def __str__(self):
        return f'Car({self.__year_model}, {self.__make}, {self.__get_speed})'
    
    def accelerate(self):
        return 5+self.__speed
        
    def brake(self):
        return self.__speed-5
    
    def get_speed(self):
        return self.__speed
    
    
main()

#Question 3 Personal Information Class
def main():
    me = Employee('rory', 'my house', 20, '999-999')
    brother = Employee('evan', 'my house', 21, '999-888')
    sister = Employee('darien', 'my house', 18, '988-988')
    print(me)
    print(brother)
    print(sister)

class Employee:
    
    def __init__(self, name, address, age, number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__number = number
        
    def __str__(self):
        return f'Employee({self.__name}, {self.__address}, {self.__age}, {self.__number})'

    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_age(self, age):
        self.__age = age
    def set_number(self, number):
        self.__number = number
    
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_age(self):
        return self.__age
    def get_number(self):
        return self.__number
main()
'''
def main():
    Susan = Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
    Mark = Employee('Mark Jones', 39119, 'IT', 'Programmer')
    Joy = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')
   
    print(Susan)
    print(Mark)
    print(Joy)
    
class Employee:
    def __init__(self, name, ID, department, job):
        self.__name = name
        self.__ID = ID
        self.__department = department
        self.__job = job
    def __str__(self):
        return f'Employee({self.__name}, {self.__ID}, {self.__department}, {self.__job})'
        
    def set_name(self, name):
        self.__name = name
    def set_ID(self, ID):
        self.__ID = ID
    def set_department(self, department):
        self.__department = department
    def set_job(self, job):
        self.__job = job
    
    def get_name(self):
        return self.__name
    def get_ID(self):
        return self.__ID
    def get_department(self):
        return self.__department
    def get_job(self):
        return self.__job
main()
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

