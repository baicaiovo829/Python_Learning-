import math
from curses.textpad import rectangle
from http.client import responses
from logging import exception
from os import remove
from selectors import SelectSelector
from time import strftime

from numpy.ma.core import append
from scipy.constants import value

#x = 25.9
#result = math.ceil(x)
#result = math.floor(x)
#a = input("enter the length of side a(cm):")
#b = input("enter the length of side b(cm):")
#c = math.sqrt(pow(float(a), 2) + pow(float(b), 2))
"""
num = [1,2,3,4,-2,-4]
max_num = 0
for i in num:
    max_num = i if i > max_num else max_num
print(max_num)
"""

#print("even" if i % 2 == 0 else "odd")
#name = input("enter your name: ")
#result = len(name)
#result = name.find("a")
#result = name.rfind("f")
#result = name.capitalize()
#result = name.upper()
#result = name.lower()
#result = name.isdigit()
#result = name.isalpha()
#result = name.count("y", 0, 4)
"""
user_name = input("please enter your name: ")
if len(user_name) < 12 and user_name.isalpha() and user_name.isalpha():
    print(f"your name {user_name} is valid!")
else:
    print("your name is invalid! Try again!")

print()

#credit_card_number = "1234-2345-4546-46546"
#print(credit_card_number[::-2])

price1 = 123.232421
price2 = -123.234
price3 = 123.12
print(f"price1 is {price1:15}")
print(f"price2 is {price2:10}")

def get_positive_input(prompt):
    value = -1
    while value <= 0:
        value = float(input(prompt))
        if value <= 0:
            print(f"{prompt.split(':')[0]} cannot be negative or equal zero!")
    return value

priciple = get_positive_input("enter the priciple: ")
rate = get_positive_input("enter the interest rate: ")
time = get_positive_input("enter the time: ")

total = priciple * pow((1 + rate / 100), 2)
print(f"total is {total:.3f}")

for x in range(1, 11):
    if x == 6 or x == 7:
        break
    else:
        print(x)

import time
my_time = int(input("enter the time inseconds:"))
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = x // 60
    hours = x // 3600
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    time.sleep(1)
print("Hallo World !")

rows = int(input("enter the number of rows: "))
colums = int(input("enter the number of colums: "))
symbol = input("enter the symbol: ")

for x in range(rows):
    for y in range(colums):
        print(symbol, end="")
    print()

#quize python 
questions = [["what is the colour of chineses flag?"],
             ["how many bones are in human body?"],
             ["how many elements in the periodic table?"]]
options = [["A: red", "B: yellow", "C: blue"],
           ["A: 206", "B: 205", "C: 207"],
           ["A: 118", "B: 120", "C: 119"]]
answers = ["A", "A", "A"]
gusses = []
questions_num = 0
score = 0
for question in questions:
    print("-" * 30)
    print(question)
    for option in options[questions_num]:
        print(option)

    guss = input("what is your answer ? (A, B, C, D):").upper()
    gusses.append(guss)
    if guss == answers[questions_num]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print(f"the correct answer is {gusses[questions_num]}")
    questions_num += 1
print(f"your answers are {gusses}, the correct answers are {answers}, so your final score is {score}!")


captials ={"USA" : "Washington",
           "China": "Beijing",
           "Japan": "Tokyo",
           "Germany": "Berlin",}
print(captials.items())

print(captials)


menue = {"pizza": 10,
         "burger": 5,
         "soda": 2,
         "salad": 4}

cart = []
total = 0
print("welcome to our theather menue!")
while True:
    order = input("please enter your order (pizza, burger, soda, salad) or 'done' to finish: ").lower()
    cart.append(order)
    if order == "pizza":
        total += menue["pizza"]
    if order == "burger":
        total += menue["burger"]
    if order == "soda":
        total += menue["soda"]
    if order == "salad":
        total += menue["salad"]
    if order == "done":
        break
cart.remove("done")
print(f"your ordered {cart} and the total is {total}")


# random number
import random
options = ["rock", "paper", "scissors"]
#number = random.choice(options)
#options = ['1', '2', '3', '4', '5']
random.shuffle(options)
print(options)

import random
min_num = int(input("enter the minimum number:"))
max_num = int(input("enter the maximum number:"))
print(f"select a number between {min_num} and {max_num}")
answer = random_number = random.randint(min_num, max_num)
guess = 0
guesses = 0
is_running = True
while is_running:
    guess = input("guess a number:")
    guesses += 1
    if guess.isdigit() is False:
        print("please enter a number!")
        continue
    if int(guess) > max_num or int(guess) < min_num:
        print(f"your guess is out of range! please select a number between {min_num} and {max_num}")
    if int(guess) > answer:
        print("your guess is too high!")
    if int(guess) < answer:
        print("your guess is too low!")
    if int(guess) == answer:
        print("you guessed it!")
        is_running = False
print(f"you guessed the number {answer} in {guesses} guesses!")

# get function 
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("seconds", 456)

print(x)

# sum(): print(sum([1,2,3,4,5], 7))
# isinstance build-in function
def net_price(list_price, discount, tax):
  if isinstance(discount, (int,float)) and isinstance(tax, (int,float)):
      return f"the net price is {list_price * (1 - discount) * (1 + tax)}"
  else:
      raise TypeError("discount and tax must be numbers")

print(net_price(100, 0.7, 0.1))


word = "APPLE"
letter = input("enter a letter in a secret word:").upper()

if letter in word:
    print(f"Correct! {letter} is in the word!")
elif letter not in word:
    print(f"Wrong! {letter} is not in the word!")

grades = {"A" : 90,
          "B" : 80,
          "C" : 70,
          "D" : 60}
grade = input(f"what is your grade level? (A, B, C, D):").upper()

if grade in grades:
    print(f"your score is {grades[grade]}")
else:
    print(f"Sorry! Your level is too low, there is no score for {grade}!")


def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1, 2, 3, 4, 5))

def print_address(**kwargs):
    print(f"your adress is:")
    for key, value in kwargs.items():

        print(f"{key}: {value}, end = '----'")



print_address(country = "Germany", city = "Berlin", street = "Alexanderplatz", house_number = 12)



fruit = [fruit[0].upper() for fruit in ["banana", "apple", "orange"]]
print(fruit)



# banking system 
def creat_count():
      user_name = input("please enter your name:")
      print(f"your account {user_name} is created!")
def show_balance(balance):
      print(f"your balance is {balance:.2f} now!")
def deposit_money():
    amount = float(input("please enter your deposit amount:"))
    if amount <= 0:
        print("deposit amount cannot be negative!")
        return 0
    else:
        return amount

def withdraw_money(balance):
    withdraw = float(input("please enter your withdraw amount:"))
    if withdraw <= 0:
        print("withdraw amount cannot be negative!")
        return 0
    if withdraw > balance:
        print("withdraw amount cannot be greater than your balance!")
        return 0
    return withdraw

def main():

    balance = 0
    is_running = True
    while is_running:
         print("This is a banking system!")
         print("1. Create an account")
         print("2. show the balance")
         print("3. deposit money")
         print("4. withdraw money")
         choice = input("please enter your choice:")
         if choice == "1":
            creat_count()
         elif choice == "2":
              show_balance(balance)
         elif choice == "3":
              balance += deposit_money()
         elif choice == "4":
              balance -= withdraw_money(balance)
         elif choice == "5":
              is_running = False
         else:
              print("invalid option! please try again!")

         print(f"Thanks for using our banking system!\n Having a nice day!")

if __name__ == "__main__":
    main()


# slot machine
import random
def spin_row():
    symbols = ['🍌', '🍉', '🍋', '🍓', '🥥']
    result = []
    for symbol in range(3):
        result.append(random.choice(symbols))
    return result


def print_now(row):
    print("***********")
    print("|".join(row))
    print("***********")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍌':
            return bet * 10
        if row[0] == '🍉':
            return bet * 5
        if row[0] == '🍋':
            return bet * 3
        if row[0] == '🍓':
            return bet * 2
        if row[0] == ' 🥥':
            return bet * 1
    else:
        return 0

def main():
    balance = 100

    print("welcome to the slot machine!")
    print(f"symbols : 🍌 🍉 🍋 🍓 🥥")
    print(f"your balance is {balance:.2f}")
    while balance > 0:
        bet = input("please enter your bet amount:")
        if bet.isdigit() is False:
            print("please enter a valid number!")
            continue
        if int(bet) > balance:
            print("your bet amount is greater than your balance!")
            continue
        if int(bet) <= 0:
            print("your bet amount cannot be negative or zero!")
            continue

        bet = int(bet)
        balance -= bet
        row = spin_row()
        print("spinning ...\n")
        print_now(row)
        payout = get_payout(row, bet)
        if payout > 0:
            print("congratulation! you won!")
        else:
            print("sorry! you lost!")
        print(get_payout(row, bet))
        balance += get_payout(row, bet)
        print(f"now your balance is ${balance:.2f}!")
        play_again = input(f"do you want to play again? (yes/no):").lower()
        if play_again == "yes":
            if balance > 0:
                continue
            else:
                print("Sorry you got to charge your balance!")
        else:
            print("thanks for playing!")
            break

    print(f"GAME OVER!")
    print(f"your final balance is ${balance:.2f}!")
    


if __name__ == "__main__":
    main()



# message to encrypt
import random
import string
chars = "  " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
key = chars.copy()

random.shuffle(key)
print(chars)
print(key)
# encryption
plain_text = input("enter your message to encrypt:")
cipher_text = ""
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(f"your original message is: {plain_text}")
print(f"your encrypted message is: {cipher_text}")

# decryption
cipher_text = input("enter your message to dencrypt:")
plain_text = ""
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
print(f"your encrypted message is: {cipher_text}")
print(f"your original message is: {plain_text}")





# hangman game
import random
def get_word():
    words = ["apple", "banana", "orange", "grape", "watermelon"]
    return random.choice(words)
hangman_art = {0 :("   ",
                   "   ",
                   "   "),
               1 :(" o ",
                   "   ",
                   "   "),
               2 :(" o ",
                   " / "
                   "   "),
               3 :(" o ",
                   "/| ",
                   "   "),
               4 :(" o ",
                   "/|\\",
                   "   "),
               5 :(" o ",
                   "/|\\",
                   "/  "),
               6 :(" o ",
                   "/|\\",
                   "/ \\"),
               }
def display_hangman(tries):
    print("\n".join(hangman_art[tries]))

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = get_word()
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)
        guess = input("guess a letter:").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("please enter only one letter!")
            continue
        if guess in guessed_letters:
            print(f"you already guessed {guess}!")
            continue
        guessed_letters.add(guess)
        if guess in answer:
            print(f"correct! {guess} is in the word!")
            for index, letter in enumerate(answer):
                if letter == guess:
                    hint[index] = guess
        else:
            print(f"wrong! {guess} is not in the word!")
            wrong_guesses += 1
            guessed_letters.add(guess)
        if "_" not in hint:
            is_running = False
            print(f"congratulation! you guessed the word {answer}!")
        if wrong_guesses == 6:
            display_hangman(wrong_guesses)
            is_running = False
            print(f"you lost! the word was {answer}!")


if __name__ == "__main__":
    main()


# class
class Car:
    size = 5
    num_cars = 0
    def __init__(self, brand, model, year, for_sale):
        self.brand = brand
        self.model = model
        self.year = year
        self.for_sale = for_sale
        Car.num_cars += 1
    def drive(self):
        print(f"{self.brand} {self.model} is driving!")
    def stop(self):
        print(f"{self.brand} {self.model} is stopping!")
    def info(self):
        print(f"{self.brand} {self.model} is from {self.year} and is {'for sale' if self.for_sale else 'not for sale'}!")




car_1 = Car("BMW", "X5", 2020, False)
car_2 = Car("Ford", "Fusion", 2021, True)
car_3 = Car("Tesla", "Model S", 2022, True)
print(Car.num_cars)



# Inheritance
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating!")
    def sleep(self):
        print(f"{self.name} is sleeping!")

class Dog(Animal):
    def speak(self):
        print(f"Woof!")


class Cat(Animal):
    def speak(self):
        print(f"Meow!")
dog = Dog("Max", 5)
cat = Cat("Mia", 3)
dog.speak()
cat.speak()



# multiple inhertance
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating!")
    def sleep(self):
        print(f"{self.name} is sleeping!")

class Fleet(Animal):
    def fleet(self):
        print(f"{self.name} is fleeting!")
class Hunt(Animal):
    def hunt(self):
        print(f"{self.name} is hunting!")
class Rabit(Fleet):
    pass
class Tiger(Hunt):
    pass
class Fish(Fleet, Hunt):
    pass

rabit = Rabit("Bunny")
tiger = Tiger("Tiger")
fish = Fish("Goldfish")
tiger.sleep()



# super class

class Shape:
    def __init__(self, color, is_filed):
        self.color = color
        self.is_filed = is_filed
    def describe(self):
        print(f"this is a {self.color} shape and it is {'filled' if self.is_filed else 'not filled'}!")
class Circle(Shape):
    def __init__(self, color, is_filed, radius):
        super().__init__(color, is_filed)
        self.radius = radius
    def describe(self):
        super().describe() # if you want to call the super class method
        print(f"this is a circle with radius {self.radius}!") # the order of the method is important

class Square(Shape):
    def __init__(self, color, is_filed, width):
        super().__init__(color, is_filed)
        self.width = width
    def describe(self):
        super().describe()
        print(f"this is a square with width {self.width}!")

class Triangle(Shape):
    def __init__(self, color, is_filed, width, height):
        super().__init__(color, is_filed)
        self.width = width
        self.height = height
    def describe(self):
        super().describe()
        print(f"this is a triangle with width {self.width} and height {self.height} and the area is {self.width * self.height}cm^2!")

circle = Circle("red", True, 10)
square = Square("blue", False, 10)
triangle = Triangle("green", True, 10, 20)

triangle.describe()




#polymorphism

#static method : a method that belongs to the class and not to the instance of the class
# class method : all operations related to the class itself
class Employee:
    count = 0
    total_salary = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1
        Employee.total_salary += self.salary
    #def get_count(self):
        #return Employee.count
    @classmethod
    def get_count(cls):
        return cls.count
    @staticmethod
    def is_working():
        print("yes, I am working!")
    @classmethod
    def get_average_salary(cls):
        if cls.count == 0:
            return 0
        else:
            return cls.total_salary / cls.count
    @staticmethod
    def is_valid_position(position):
        if position in ["manager", "developer", "designer"]:
            return True
        else:
            return False
    @classmethod
    def from_string(cls, string):
        name, salary = string.split(",")
        return cls(name, float(salary))

    def __str__(self):
        return f"{self.name} is working for {self.salary}!"
employee1 = Employee("Kyle", 2000)
employee2 = Employee("John", 4000)
employee3 = Employee("Mike", 3000)
employee4 = Employee("Anna", 5000)
print(Employee.get_count())
print(Employee.get_average_salary())
print(employee1.from_string("John,4000"))


# Class methods: Instance methods and Static methods and Class methods

#magic method : build-in functions that are used to define the behavior of the class

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self): # without this print(book1) will return <__main__.Book object at 0x7f8c8c8c8c8>
        return f"the book {self.title} is written by {self.author} and has {self.pages} pages!"
    def __eq__(self, other):
     if self.title == other.title:
         return True
    def __lt__(self, other):
        return self.pages < other.pages
    def __add__(self, other):
        return f"{self.pages + other.pages} pages"
    def __contains__(self, item):
        return item == self.pages or item in self.title or item in self.author
    def __getitem__(self, key):
        if key == "title":
            return self.title
        if key == "author":
            return self.author
        if key == "pages":
            return f"{self.pages} pages"


book1 = Book("Harry Potter", "J.K. Rowling", 500)
book2 = Book("Harry Potter", "J.R.R. Tolkien", 300)
book3 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1000)
print(book3["title"])




# @property : a decorator that is used to define a method as a property
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"the width of rectangle is {self._width:.1f} cm"
    @property
    def height(self):
        return f"the height of the rectangle is {self._height:.1f} cm"
    @width.setter
    def width(self, new_width):
        if new_width < 0:
            raise ValueError("width cannot be negative!")
        else:
            self._width = new_width
    @height.setter
    def height(self, new_height):
        if new_height <= 0:
            print("height cannot be negative or zero!")
        else:
            self._height = new_height
    @width.deleter
    def width(self):
        del self._width
        print("width is deleted!")
    @height.deleter
    def height(self):
        del self._height
        print("height is deleted!")



rectangle1 = Rectangle(10, 20)
rectangle2 = Rectangle(5, 10)
rectangle1.width = 56
rectangle1.height = 100
del rectangle1.width

print(rectangle1.height)



#Decorator

def get_sprinkle(original_function):
    def wrapper_function(*args, **kwargs): # accept any numbers or types of arguments
        print("sprinkle")
        original_function(*args, **kwargs)
    return wrapper_function
def get_fudge(original_function):
    def wrapper_function(*args, **kwargs):
        print("you add a fudge🦀")
        original_function(*args, **kwargs)
    return wrapper_function #返回包装后的函数
@get_sprinkle# get_pizza is replaced by wrapper_function
@get_fudge
def get_pizza(flover):
    print(f"get pizza {flover}🍕!")

get_pizza("chocolate" )



#exception : interrupts the normal flow of the program 
try:
    x = int(input("enter a number:"))
    y = 100 / x
    print(f"the result is {y:.2f}")
except ValueError:
    print("please enter a valid number!")
except ZeroDivisionError:
    print("you cannot divide by zero!IDIOT!")
except TypeError:
    print("please enter a valid number!")
except Exception as e:
    print(f"an error occurred: {e}")
finally:
    print("thanks for using our program!")





# python file detection
import os
file_path = "/Users/welt/Downloads/Studying aboard "

if os.path.exists(file_path):
    print(f"the file {file_path} exists!")
    if os.path.isfile(file_path):
        print(f"the file {file_path} is a file!")
    elif os.path.isdir(file_path):
        print(f"the file {file_path} is a directory!")
else:
    print(f"the file {file_path} does not exist!")


# python writing files
#txt
text_date = "hello world!"
file_path = "/Users/welt/Downloads/output.text"
with open(file_path, "a") as file:
    file.write(f"{text_date}\n")
    file.write("床前明月光，疑是地上霜\n")
    file.write("举头望明月，低头思故乡\n")
    print(f"file is created!")

with open(file_path, "r") as file:
    print(file.read())

# jason
import json

employee = {"name": "John",
            "age": 30,
            "city": "New York",
            "salary": 5000,
            "is_married": False,
            "children": ["Anna", "Mike"],
            "address": {
                "street": "5th Avenue",
                "number": 10
            }}
file_path = "/Users/welt/Downloads/output.text"
with open(file_path, "w") as file:
    json.dump(employee, file, indent=6)
    print("json file is created!")

with open(file_path, "r") as file:
    data = json.load(file)
    print(data)




# csv
import csv

employmees = [["name", "age", "city", "salary"],
                ["John", 30, "New York", 5000],
                ["Anna", 25, "London", 6000],
                ["Mike", 35, "Berlin", 7000]]
file_path = "/Users/welt/Downloads/output.csv"
with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(employmees)
    print("csv file is created!")
with open(file_path, "r") as file:
    reader = csv.reader(file)#it will read the file as his memory location 
    for row in reader:
        print(row)



# python reading files

file_path = "/Users/welt/Downloads/output.text"
try:
    with open(file_path, "r") as file:
        print(file.read())
except FileNotFoundError:
    print(f"the file {file_path} does not exist!")



import datetime # allows you to work with dates and times
date = datetime.date(2025, 1, 2)
date_today = datetime.date.today()
time = datetime.time(23, 45, 23)
now = datetime.datetime.now()
#now = strftime("%Y-%m-%d %H:%M:%S")

target_datetime = datetime.datetime(2025, 1, 2, 23, 45, 23)
current_datetime = now
if target_datetime > current_datetime:
    print("the target date is in the future!")
else:
    print("the target date is in the past!")
    
    

# python Alarm clock
import time
import datetime
import pygame
def set_alarm(alarm_time):
    print(f"alarm set for {alarm_time}")
    sound_file = "Gneisenaustraße 21.m4a"
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("Wake UP 🤔!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False
        time.sleep(1)



if __name__ == "__main__":
    alarm_time = input("enter the alarm time in HH:MM:SS format:")
    set_alarm(alarm_time)



# python threading: doing multipal task concurrently
import threading
import time

def fuck_girl(name,name2):
    time.sleep(5)
    print(f"You have fucked {name} and {name2}brain out! Stop!")

def chock_her():
    time.sleep(3)
    print("You have reached her deep throat! Stop!")

def finger_ass():
    time.sleep(2)
    print("You have played her ass enough! Stop!")

chore1 = threading.Thread(target=fuck_girl, args=("Nelly","Irs"))
chore1.start()

chore2 = threading.Thread(target=chock_her)
chore2.start()

chore3= threading.Thread(target=finger_ass)
chore3.start()
chore1.join()
chore2.join()
chore3.join()
print("You have came ! Enough!")


# how to connect to an API with Python
import requests

url = "https://github.com/user"
headers = {"Authorization" : "token YOUR_PERSoNAL_ACCESS_TOKEN"}
response = requests.get("https://github.com/user")

if response.status_code == 200:
    print("The request was successful!")
    try:
        data = response.json()
        print(data)
    except ValueError:
        print("Response is not in JSON format.")
else:
    print(f"field to retrieve data {response.status_code}")



# Graphical User Interface; PyQt5 introduction
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        # self.setWindowIcon(QIcon("/Users/welt/Downloads/IMG_A6201A6477EA-1.jpeg"))
        self.setGeometry(1000, 100, 400, 300)

        # self.label = QLabel("Hello World!", self)
        # self.setFont(QFont("Arial", 20))
        # self.label.setGeometry(0, 0, 500, 200)
         self.label.setStyleSheet("color: #eb4034; "
                                 "background-color: white;"
                                 "font-weight: bold;"
                                 "font-size: 30px;"
                                 "font-style: italic;"
                                 "text-decoration: underline;")
        
        # self.label.setAlignment(Qt.AlignCenter) # center the text
        # self.label.setAlignment(Qt.AlignLeft) # left the text
        # self.label.setAlignment(Qt.AlignVCenter) # vertical center the text
        # self.label.setAlignment(Qt.AlignHCenter) # horizontal center the text
        # self.label.setAlignment(Qt.AlignBottom) # bottom the text
        # self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # center the text
        label_image = QLabel(self)
        label_image.setGeometry(0, 0, 300, 200)
        pixmap = QPixmap("/Users/welt/Downloads/IMG_A6201A6477EA-1.jpeg")
        label_image.setPixmap(pixmap)
        label_image.setScaledContents(True)
        label_image.setGeometry((self.width()-label_image.width())//2, (self.height()-label_image.height())//2, label_image.width(), label_image.height())









def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())




if __name__ == "__main__":
    main()




# PyQt5 layouts
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget, QPushButton)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry(1000, 100, 400, 300)
        self.setStyleSheet("background-color: #f0f0f0;")
        self.initUI()

    def initUI(self):
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Create a vertical layout
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        grid = QGridLayout()

        # Add widgets to the layout
        label1 = QLabel("Label 1")
        label2 = QLabel("Label 2")
        label3 = QLabel("Label 3")

        label1.setStyleSheet("background-color: #eb4034; ")
        label2.setStyleSheet("color: #34eb77; ")
        label3.setStyleSheet("background-color: #3434eb; ")

        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0, 2, 3) # row, column, row span, column span

        main_widget.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()





# PyQt5 widgets push button widgets
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,QPushButton,QLabel)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry(1000, 100, 400, 300)
        self.setStyleSheet("background-color: #f0f0f0;")
        self.label = QLabel("Fuck Me!", self)
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Click Me!", self)
        self.button.setGeometry(100, 100, 200, 100)
        self.button.setStyleSheet("background-color: #eb4034; ")
        self.button.setStyleSheet("color: black; font-size: 20px; font-weight: bold;")
        self.button.clicked.connect(self.click_me) # the widget is gonna take when the signal occurs


        self.label.setGeometry(100, 200, 200, 100)
        self.label.setStyleSheet("background-color: #eb4034; ")
        self.label.setStyleSheet("color: black; font-size: 15px; font-weight: bold;")

    def click_me(self):
        self.button.setText("You clicked me!")
        self.button.setDisabled(True)
        self.label.setText("Stop I can't take it anymore!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())




# PyQt5 Checkboxes

import sys
from  PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry(1000, 100, 400, 300)
        self.setStyleSheet("background-color: #f0f0f0;")
        self.checkbox = QCheckBox("I agree to the terms and conditions", self)
        self.initUI()

    def initUI(self):
        self.label = QLabel
        self.checkbox.setStyleSheet("front-size: 20px; font-weight: bold;"
                                    "front-family: Arial;")
        self.checkbox.setGeometry(10, 10, 200, 100)
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_state)
    def checkbox_state(self,state):
        if state == Qt.Checked:
            print("You just checked the checkbox!")
        else:
            print("You just unchecked the checkbox!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


#FPC 控制器简单演示代码
import numpy as np
from scipy.interpolate import RegularGridInterpolator


class FPCController:
    def __init__(self, lmbda_grid, torque_grid, delta_lut, pi_gains):
        # 插值器初始化
        self.lut_interp = RegularGridInterpolator((lmbda_grid, torque_grid), delta_lut)

        # PI 控制器参数
        self.kp_lambda, self.ki_lambda = pi_gains['lambda']
        self.kp_delta, self.ki_delta = pi_gains['delta']

        # 控制器积分项状态
        self.integrator_lambda = 0.0
        self.integrator_delta = 0.0

    def compute(self, T_star, lambda_meas, delta_meas, omega):
        """ """
        # ---------- Step 1: Flux & Torque Limiting ----------
        lambda_star = self.limit_flux(T_star)
        T_limited = self.limit_torque(T_star, lambda_star)

        # ---------- Step 2: 查询 LUT 得到 δ ----------
        delta_star = self.lookup_delta(lambda_star, T_limited)

        # ---------- Step 3: PI 控制 λ ----------
        error_lambda = lambda_star - lambda_meas
        self.integrator_lambda += error_lambda
        v_ds = self.kp_lambda * error_lambda + self.ki_lambda * self.integrator_lambda

        # ---------- Step 4: PI 控制 δ ----------
        error_delta = delta_star - delta_meas
        self.integrator_delta += error_delta
        v_qs = self.kp_delta * error_delta + self.ki_delta * self.integrator_delta + omega * lambda_meas

        # ---------- Step 5: Park^-1 反变换 ----------
        theta = lambda_meas  # 假设 stator flux angle ≈ λ
        v_alpha = v_ds * np.cos(theta) - v_qs * np.sin(theta)
        v_beta = v_ds * np.sin(theta) + v_qs * np.cos(theta)

        # Clarke^-1 -> v_abc（简化版本）
        v_abc = self.clarke_inverse(v_alpha, v_beta)

        return {
            "v_ds": v_ds,
            "v_qs": v_qs,
            "delta_star": delta_star,
            "lambda_star": lambda_star,
            "v_abc": v_abc
        }

    def lookup_delta(self, lambda_star, torque_star):
        point = np.array([[lambda_star, torque_star]])
        return self.lut_interp(point)[0]

    def limit_flux(self, T_star):
        return min(max(0.2, abs(T_star) * 0.8), 1.0)  # 示例限幅

    def limit_torque(self, T_star, lambda_star):
        return np.clip(T_star, -1.0 * lambda_star, 1.0 * lambda_star)

    def clarke_inverse(self, alpha, beta):
        a = alpha
        b = -0.5 * alpha + np.sqrt(3) / 2 * beta
        c = -0.5 * alpha - np.sqrt(3) / 2 * beta
        return np.array([a, b, c])
# 示例：生成 δ_LUT (λ*, T*) 网格（假设δ= arcsin(T/λ））
lambda_vals = np.linspace(0.2, 1.0, 20)
torque_vals = np.linspace(-1.0, 1.0, 20)
delta_grid = np.zeros((len(lambda_vals), len(torque_vals)))

for i, lmbda in enumerate(lambda_vals):
    for j, torque in enumerate(torque_vals):
        if abs(torque) < lmbda:
            delta_grid[i, j] = np.arcsin(torque / lmbda)
        else:
            delta_grid[i, j] = np.sign(torque) * np.pi/2

# PI 控制器参数
pi_gains = {
    "lambda": (1.0, 10.0),  # kp, ki
    "delta":  (1.0, 10.0)
}

# 创建控制器
fpc = FPCController(lambda_vals, torque_vals, delta_grid, pi_gains)

# 模拟一次控制计算
result = fpc.compute(
    T_star = 0.6,
    lambda_meas = 0.3,
    delta_meas = 0.9,
    omega = 70.0
)

print(result)


# Pqt5 radio buttons
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QLabel, QVBoxLayout, QWidget, QButtonGroup
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry(1000, 100, 400, 300)
        self.radio1 = QRadioButton("Porn movice", self)
        self.radio2 = QRadioButton("Masturbation", self)
        self.radio3 = QRadioButton("Sex", self)
        self.radio4 = QRadioButton("Deepthroat", self)
        self.radio5 = QRadioButton("Blowjob", self)
        self.setStyleSheet("background-color: #f0f0f0;")
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(0, 0, 200, 100)
        self.radio2.setGeometry(0, 100, 200, 100)
        self.radio3.setGeometry(0, 200, 200, 100)
        self.radio4.setGeometry(200, 0, 200, 100)
        self.radio5.setGeometry(200, 100, 200, 100)

        self.setStyleSheet("QRadioButton {"
                           "color: green;"
                           "font-size: 20px;"
                           "font-weight: bold;"
                           "font-family: Arial;}")

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_state)
        self.radio2.toggled.connect(self.radio_state)
        self.radio3.toggled.connect(self.radio_state)
        self.radio4.toggled.connect(self.radio_state)
        self.radio5.toggled.connect(self.radio_state)


    def radio_state(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"You selected: {radio_button.text()}")
        else:
            print(f"You unselected: {radio_button.text()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# Pqt5 Line Edit
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry(1000, 100, 400, 300)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Click Me!", self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 50)
        self.button.setGeometry(230, 10, 200, 50)
        self.line_edit.setStyleSheet(
                                    "color: black; "
                                    "font-size: 25px; "
                                    "font-weight: bold; "
                                    "font-family: Arial;")
        self.button.setStyleSheet("color: black; "
                                  "font-size: 25px;"
                                  "front-weight: bold; "
                                  "front-family: Arial;")
        self.line_edit.setPlaceholderText("Enter your text here...")
        self.button.clicked.connect(self.submit)
    def submit(self):
            text = self.line_edit.text()
            if text:
                print(f"You entered: {text}")

            else:
                print("Please enter some text!")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    


food = ["apple", "banana", "orange", "pineapple", "kiwi"]
vegetables = ["carrot", "cucumber", "paper", "onion"]

#food.remove(food[3])
#food.pop()
#food.sort(reverse=True)
food.insert(0, "watermelon")
food.extend(vegetables)
for x in food:
    print(x)

utensile ={"fork", "spoon", "knife"}
diches = {"plate", "bowl", "cup", "knife"}
#utensile.remove("fork")
#utensile.update(diches)

utensile.update(diches)
for i in utensile:
    print(i)


capitals = {'USA': 'Washington, D.C.',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia':'Moscow'}
capitals.update({'UK':'London',
                 'Germany': 'Berlin'})
capitals.pop('Russia')
capitals.clear()
for key, value in capitals.items():
    print("the capital of", key, "is", value)



name = "zhilin zhang!"
if name[0].islower():
    name = name.capitalize()
first_name = name[0:name.index('z')]
last_name = name[name.index('z'):name.index('!')]
print(first_name)
print(len(first_name))
print(last_name)



#keyword argument
def halle(first, middle, last):
    print("hallo "+ first + " "+ middle + " " + last + "!")

halle(middle="cod", first="bro", last="dudu")


number = float(input("Please enter a whole positive number:"))
num = int(number)
num = abs(num)
num = round(num)
print (f"the final value of {number} is {num}")


# L: local ; E: enclosing: G: global B : built-in

def add(*args):
    sum =  0
    sum_with_order = list(args)
    sum_with_order[0] = 20
    for i in sum_with_order:
        sum += i
    return sum
print(add(1,2,3,4))

def hallo(**name):
    print("Hallo", end=" ")
    for key,value in name.items():
        print(value, end=" ")

hallo(title='Hallo', first='zhilin', last='zhang', middle= 'dirty')



print("the {animal} jumped into the {item} !".format(animal="cow", item="moon"))

text = "the {} jumped into the {}!"
print(text.format("cow", "moon"))

name ="Zhilin"
print("Hallo, my name is {}".format(name))
print("Hallo my name is {:10}. nice to meet you!".format(name))
print("Hallo my name is {:^10}. nice to meet you!".format(name))
print("Hallo my name is {0:10}. nice to meet you!".format(name))

number = 3.1415926
print("the number is {:.4f}".format(number))
print("the number is {:E}".format(number))


import random
x = random.randint(1,89)
print(x)
y = random.random()
print(y)
z = random.randrange(1,10)
print(z)
Mylist =["rock", "paper", "scissors"]
x = random.choice(Mylist)
print(x)
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
random.shuffle(cards)
print(cards)

try:
   numerator = int(input("enter a number to divide:"))
   denominator = int(input("enter a number to divide by:"))
   result = numerator / denominator
   print(result)
except ZeroDivisionError as e:
    print(e)
    print("you cannot divide by zero! Idiot!")
except ValueError as e:
    print(e)
    print("Plaease enter a valid number!")
except Exception as e:
    print(e)
    print("Something went wrong")
else :
    print(result)

finally:
    print("This is the end of the program!")

import os
path ="/Users/welt/Downloads/Einladung Grillen.pdf"
if os.path.exists(path):
    print("the file exists!")
    if os.path.isfile(path):
        print("there is a file!")
    if os.path.isdir(path):
        print("there is a directory!")
else:
    print("the location dones not exist!")


with open("output.text" ) as file:
     print(file.read())
print(file.closed)

text = "Yooooooo\nThis is some text\nhave a good one\nDo not fuck anyone or stick in any holes\n"
words = "come on\nI want your big black dick stick in my pussy and stretch it out very open!"
with open("text.txt", "a") as file:
    file.write(words)
    
    

import shutil
shutil.copy("text.txt","copy_text.txt")

import os
source = "folder"
destination = "//Users//welt//115download//"

try:
    if os.path.exists(destination):
        print("this place is already a file there")
    else:
        os.replace(source, destination )
        print(source + "has already been removed")
except Exception as e:
    print(source+ " is not found!")

import os
import shutil

text = "folder"
try:
    #os.remove(text)
    #os.rmdir(text)
    shutil.rmtree(text)
except FileNotFoundError:
    print(text + " is not founded")
except PermissionError:
    print("you don't have permission to delete that")
except OSError:
    print("you can delete that using that function")
else:
    print(text + " is deleted")


import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)
player = input("what is your choice? (rock, paper, scissors):").lower()
if player == computer:
    print("it is a tie!")
elif player == "rock" and computer == "scissors":
    print("you win!")
elif player == "paper" and computer == "rock":
    print("you win!")
elif player == "scissors" and computer == "paper":
    print("you win!")
else:
    print("you lose!")


#输入一个整数，判断是奇数还是偶数
number = input("enter a number:")
try:
   if int(number)%2 == 0:
      print("the number is even!")
   else:
      print("the number is odd!")
except Exception as e:
    print("the number is not a valid integer!")



#输入一个列表 [1, 2, 3, 4, 5]，输出它的和与平均值
number_list = input("enter a list of number seperated by commas:")
try:
    number = [float(x) for x in number_list.split(',')]
    total = sum(number)
    average = total / len(number)
    print("the total is:", total, "the average is:", average)
except Exception as e:
    print("please enter a valid list of numbers!")


#给定一个列表 [1, 2, 2, 3, 4, 4, 5]，请去重并保持原有顺序
number_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_list = []
for x in number_list:
    if x not in unique_list:
        unique_list.append(x)
print("the nuique list is:", unique_list)

#写一个函数，接收一个字符串参数，返回该字符串中元音字母（a, e, i, o, u）的数量
letter_list = input("enter a string:")
letter_list= [x for x in letter_list]
result = 0
try:
   for letter in letter_list:
       if letter in ["a", "e", "i", "o", "u"]:
        result += 1
   print("the number of vowels in the string is:", result)
except Exception as e:
    print("please enter a valid string!")
"""
#写一个函数，接收一个整数参数，返回该整数的阶乘
def factorial_zhang(n):
    if n <0:
        raise ValueError("please enter a positive number!")
    elif n ==0 or n==1:
        return 1
    else:
        return n*factorial_zhang(n-1)

#写一个函数，接收一个整数参数，返回该整数的斐波那契数列
def fibonacci_zhang(n):
    if n <0:
        raise ValueError("please enter a positive number!")
    result_list =[]
    if n ==0:
        result_list.append(0)
    elif n == 1:
        result_list.append(0)
        result_list.append(1)
    else:
        result_list =[0, 1]
        for x in range(2, n):
           result_list.append(result_list[-1]+result_list[-2])
    return result_list

#写一个函数，接收一个字符串参数，返回该字符串中每个字符出现的次数
def count_characters_zhang(string):
    if not isinstance(string, str):
        raise ValueError("please enter a valid string!")
    result={}
    for char in string:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return result
#print(count_characters_zhang("fuck you! i love your body! i love your holes! i love your legs!"))
#写一个函数，接收一个整数参数，返回该整数的质因数分解
def prime_factorization(n):
    result_list = []
    d =2
    while d*d<n:
        if n%d == 0:
            result_list.append(d)
            n //= d
        d += 1
    if n > 1:
        result_list.append(n)
    return result_list
#找出两个整数之间的最大公约数
def found_GCD(a, b):
    list_a = []
    for i in range(1,a):
        if a % i == 0:
            list_a.append(i)
            i += 1
    print(list_a)
    for x in range(len(list_a)):
        max_number = max(list_a)
        if b % max_number == 0:
            result = max_number
            break
        else:
            list_a.remove(max_number)
    return result
#
def fizzbuzz(n):
    for i in range(0, n):
        i += 1
        if i % 3 == 0:
            print("Fizz")
        if i % 5 == 0:
            print ("Buzz")
        else:
            print(i)

#写一个函数，接收一个字符串参数，返回该字符串是否是回文字符串
def is_palindrome(string):
    if not isinstance(string, str):
        raise ValueError("please enter a valid string!")
    string = string.lower()
    string = string.replace(" ", "")
    if string == string[::-1]:
        return True
    else:
        return False



# 写一个类，表示一个员工，包含姓名、年龄、职位等属性，以及计算工资的方法
class Employee:
    number_of_employee = 0
    base_salary = 0
    def __init__(self, name, age, position, base_salary):
        self.name = name
        self.age = age
        self.position = position
        self.base_salary = base_salary
    def display(self):
        return f"the employee {self.name} is {self.salary} years old and works as a {self.position}"
    def calculate_salary(self, bonus=0):
        return self.base_salary + bonus
    def __str__(self):
        return f"the salary of {self.name} is {self.base_salary} pre month!"
emp1 = Employee("Kyle",30, "sector manager", 5000)
emp2 = Employee("Stain", 32, "product engineer", 9000)


# 写一个类，表示一本书，包含书名、作者、页数等属性，以及比较两本书页数的方法
class Book:
    def __init__(self, title, autor, pages):
        self.title = title
        self.autor = autor
        self.pages = pages
    def comparion(self, other_book):
        if self.pages < other_book.pages:
            return f"the book {self.title} is shorter than {other_book.title}"
        if self.pages > other_book.pages:
            return f"the book {self.title} is longer than {other_book.title}"
        else:
            return f"the book {self.title} is equal to {other_book.title}"
    def __str__(self):
        return f"the book {self.title} is written by {self.autor} and has {self.pages} pages!"

book1 = Book("Little Prince", "Antoine de Saint-Exupéry", 96)
book2 = Book("Harry Potter", "J.K. Rowling", 223)


# 写一个类，表示一个矩形，包含宽度和高度属性，以及计算面积和周长的方法
class Tangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def __str__(self):
        return f"the rectangle has a width of {self.width} and a height of {self.height}"

class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposite(self, amount):
        if amount < 0:
            raise ValueError("please enter a positive amount!")
        else:
            self.balance += amount
            return f"Hi, {self.owner}, your new balance is {self.balance}"
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("please enter a positive amount!")
        elif amount > self.balance:
            raise ValueError("insufficient funds!")
        else:
            self.balance -= amount
            return f"Hi, {self.owner}, your new balance is {self.balance}"
    def __str__(self):
        return f"Good day, {self.owner}, your balance is {self.balance}"

#写一个程序计算第二大的数字

def second_largest(*args):
    if len(args)< 2:
        raise ValueError("please enter at least two numbers!")
    max_number = 0
    num = list(args)
    for i in list(num):
        if i > max_number:
            max_number = i
    num.remove(max_number)
    second_largest = 0
    for j in list(num):
        if j > second_largest:
            second_largest = j
    return second_largest

# 写一个函数，接收一个整数参数，返回该整数以内的所有质数
def find_primes(n):
    if n <2:
        return []
    primes = [2]
    for num in range(2, n):
        if num % 2 != 0:
            primes.append(num)
    return primes

# 写一个函数，接收一个字符串参数，返回该字符串中最长的单词
def longest_word(string):
    if not isinstance(string, str):
        raise ValueError("please enter a valid string!")
    words = string.split()
    longest = ""
    for word in words:
         if len(word) > len(longest):
             longest = word
    return longest


# word_count
def word_count(string):
    if not isinstance(string, str):
        raise ValueError("please enter a valid string!")
    words = string.split()
    word_dict= {}
    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict


# 判断是否是armstrong number
def is_armstrong_number(n):
    if n < 0:
        raise ValueError("Please enter a positive integer!")
    num_str = str(n)
    num_square = len(num_str)
    sum = 0
    for i in num_str:
        sum += int(i) ** num_square
    if sum == n:
        return True
    else:
        return False

#
def find_missing_number(*num_list):
    n = max(list(num_list))
    print(n)
    missing_number = []
    for i in range(1, n):
        if i not in num_list:
            missing_number.append(i)
    return missing_number

# 判断两个字符串是否是变位词
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in str1:
        if i not in str2:
            return False
    return True

def factorial(n):
    if n < 0:
        raise ValueError("please enter a positive integer!")
    elif n ==0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)

def remove_duplicates(lis):
    unique_list = []
    for i in lis:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


def find_longest_word(string):
    if not isinstance(string, str):
        raise ValueError("Please enter a valid string!")
    words = string.split(" ")
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def count_even_odd(*lis):
    num_even = 0
    num_odd = 0
    for i in list(lis):
        if i % 2 ==0:
            num_even += 1
        else:
            num_odd += 1
    return list([num_even, num_odd])


def sum_of_digits(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

#
def find_pairs(lis, target):
    pairs = []
    lis = list(lis)
    for i in range(len(lis)):
        for j in range(i+1, len(lis)):
            if lis[i] + lis[j] == target:
                pairs.append((lis[i], lis[j]))
    return pairs

def first_unique_character(string):
    char = {}
    for i in list(string):
        char[i] = char.get(i, 0) + 1
    for j in string:
        if char[j] == 1:
            return j
    return None

def is_pangram(st):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string= st.lower()
    new_string = string.replace(" ", "")
    new_string = new_string.lower()
    new_string = set(new_string)
    if len(new_string) == 26:
        return True
    else:
        return False


def is_palindrome_number(n):
    n = str(n)
    reversed_n = int(n[::-1])
    if int(n) == reversed_n:
        return True
    else:
        return False

def rotate_list(lst, k):
    if k > len(lst):
        raise ValueError("please enter a number less than the length of the list!")
    cut_list = lst[-k::1] + lst[:len(lst) - k:1]
    return cut_list


def fibonacci_up_to(n):
    fib_list = [0, 1]
    while max(fib_list) <= n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    fib_list.remove(fib_list[-1])
    return fib_list




def is_valid_parentheses(string):
    mapping_pair={'）':"（",']':"[",'}':"{"}
    stack = []
    for ch in string:
        if ch in mapping_pair.values():
            stack.append(ch)
        elif ch in mapping_pair:
            if not stack or stack[-1] != mapping_pair[ch]:
                return False
            stack.pop()
    return len(stack) == 0


def is_isomorphic(s,t):
    if len(s) != len(t):
        return False
    map_st = {}
    map_ts = {}
    for cs, ts in zip(s, t):
        if cs in map_st and map_st[cs] != ts:
            return False
        if ts in map_ts and map_ts[ts] != cs:
            return False
        map_st[cs] = ts
        map_ts[ts] = cs
    return True
def first_unique_char(s):
    count_char = {}
    for i in s:
        if i in count_char:
            count_char[i] += 1
        else:
            count_char[i] = 1
    print(count_char)
    result = []
    for char in s:
        if count_char[char] == 1:
            result.append(char)
    return result or None

def is_prime(n):
    if n <= 1:
        return False
    for i in range (2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_all_primes(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

def two_sum(nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append([i, j])
    return result

def is_palidrome_string(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalnum())
    return s == s[::-1]
#滑动窗口解法
def longest_unique_substring(s):
    seen = set()
    left = 0
    max_length = 0
    start = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        if right - left + 1 > max_length:
            max_length = right - left + 1
            start = left
    return s[start:start+max_length]

def majority_element(*nums): #投票算法，假设一定有众数，即出现次数超过n/2
    count = 0
    candidate = None
    for num in nums:
        if count ==0:
            candidate = num
        if num ==  candidate:
            count += 1
        else:
            count -= 1
    return candidate

#投票算法
def majority_element_n3(nums):

    candidate1, count1  = None, 0
    candidate2, count2 = None, 0
    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 ==0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1
    result = []
    if nums.count(candidate1) > len(nums)//3:
        result.append(candidate1)
    if nums.count(candidate2) is not None and nums.count(candidate2) > len(nums)//3:
        result.append(candidate2)
    return result or None

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1 #如果char在字典中，值加1，否则赋值为1，默认值为0
    for char in t:
        if char not in count:
            return False
        if char in count:
            count[char] -= 1
            if count[char] < 0:
                return False
    return True

def simplify_path(path):
    stack = []
    parts = path.split('/')
    print(parts)
    for part in parts:
        if part == '':
            continue
        elif part == '.':
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return '/' + '/'.join(stack) # 注意这里的join用法，第一个参数是分隔符，第二个参数是可迭代对象

def reverse_words(s):
    words = s.split()# 默认按空格分割，并自动去除多余空格
    words.reverse()
    return ' '.join(words)

def longest_palindrome(s):
    n = len(s)
    if len(s) <= 1:
        return s
    def expand_around_center(l, r):#从中心向两边扩展
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        return l+1, r-1
    best_start = 0
    best_end = 0
    for i in range(n):# 枚举中心位置，分为奇数和偶数两种情况，偶数时注意考虑i+1是否越界
        l1, r1 = expand_around_center(i, i)
        if r1-l1 > best_end- best_start:
            best_start = l1
            best_end = r1
        if i +1 < n:
            l2, r2 = expand_around_center(i, i+1)
            if r2 - l2 > best_end - best_start:
                best_start = l2
                best_end = r2
    return s[best_start:best_end +1] #注意这里的切片是包含best_end的，所以要+1, 因为python切片是不包含右边界的
def container_with_most_water(height): # 双指针法
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        area = (right - left) * min(height[left], height[right])
        if area > max_area:
            max_area = area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

def subarray_sum_brute_force(nums, k): #暴力解法，时间复杂度O(n^2),列举所有子数组
    count = 0
    n = len(nums)
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if sum == k:
                count += 1
    return count
def subarray_sum_prefix_hashmap(nums, k): #前缀和+哈希表，时间复杂度O(n)
    count = 0
    prefix = 0
    seen = {0: 1}
    for num in nums:
        prefix += num
        need = prefix - k
        if need in seen:
            count += 1
        seen[prefix] = seen.get(prefix, 0) + 1
    return count

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.available = True

    def display_info(self):
        return f"the book title: {self.title}, is written by author: {self.author}, with pages: {self.pages}!"
    def borrow(self):
        if self.available:
            self.available = False
            return f"the book {self.title} has been borrowed!"
        else:
            return f"the book {self.title} was not borrowed!"
    def return_book(self):
        if not self.available:
            return f"the book {self.title} was returned, it's available now!"
        else:
            return f"the bok {self.title} was not borrowed!"
class Library:
    def __init__(self):
        self.books = []
    def add_book(self,book):
        self.books.append(book)
        return f"the book {book.title} was added to the library!"
    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book)
            return f"the book {book.title} was removed from the library!"
        else:
            return f"the book {book.title} was not found in the library!"
    def show_books(self):
        if not self.books:
            return f"there is no book in the library! Now"
        else:
            return [book.display_info() for book in self.books]

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount < 0:
            raise ValueError ("please enter a positive amount!")
        else:
            self.balance += amount
            return f"hi, {self.owner}, your new balance is {self.balance}"
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError ("Please enter a positive amount!")
        elif amount > self.balance:
            raise ValueError ("You have insufficient funds!")
        else:
            self.balance -= amount
            return f"HI, {self.owner}, your new balance is {self.balance}"
    def display(self):
        return f"Hi, {self.owner}, your balance is {self.balance}"
class Bank:
    def __init__(self,accounts=None):
        self.accounts =[]
    def add_account(self,account):
        self.accounts.append(account)
        return f"the account of {account.owner} was added to the bank!"
    def remove_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account.owner)
            return f"the account of {account.owner} was removed from the bank!"
        else:
            return f"the account of {self.accounts} was not found in the bank!"
    def transform(self, from_account, to_account, amount):
        if from_account in self.accounts and to_account in self.accounts:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            return f"{amount} euro has been transformed from {from_account.owner} to {to_account.owner}!"
        else:
            return f"PLEASE CHECK THE ACCOUNTS!"
def valid_parentheses(s):
    mapping = {")":"(", "]" : "[", "}":"{"}
    stack = []
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '*'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return len(stack) == 0


def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return f"there is no common prefix!"
    return prefix
print(longest_common_prefix(["flower","low","flight"]))


def count_tripples(arr):
    n = len(arr)
    if n < 1 or n > 30000:
        return f"Please enter a valid number array! The length of array must stay in the range (1, 30000)"
    if min(arr) < 1 or max(arr) > 100000:
        return f"the number of array can not too small or too large! Please remain them in the range (1, 100000)"
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]<arr[j]:
                for k in range(j+1, n):
                    if arr[j]<arr[k]:
                        ans += 1

    return ans


def count_tripples(n,arr):
    if n != len(arr):
        return f"Please enter a valid array which length is n!"
    if n < 1 or n > 30000:
        return f"Please enter a valid number array! The length of array must stay in the range (1, 30000)"
    if min(arr) < 1 or max(arr) > 100000:
        return f"the number of array can not too small or too large! Please remain them in the range (1, 100000)"
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                for k in range(j + 1, n):
                    if arr[j] < arr[k]:
                        ans += 1

    return ans
print(count_tripples(5, [11, 22, 66, 100, 400]))
def character_number(s):
    if not isinstance(s, str):
        return f"please enter a valid string!"
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1 # 如果char在字典中，值加1，否则赋值为1，默认值为0
    return count
print(character_number("hello world!"))










