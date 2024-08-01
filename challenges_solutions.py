#challenges

#VARIABLES
#1. Create a variable called myName, and set it to your name. Print it out.
myName = "name"
print(myName)

#DATA TYPES
#2. Get the user to input 2 numbers. Then, print the sum of the two numbers.
number1 = input("Input a number!")
number2 = input("Input a number!")
print(int(number1) + int(number2)) # Turn the numbers into integers first, because input() returns strings.

#2.1. Have the user input their name. Then, print out a message saying "Hello, (INSERT NAME)"
name = input("What's your name?")
print("Hello, " + name)

#IF STATEMENTS AND OPERATORS
#3. Create a password checker: Get the user to input a password guess, and if it's equal to a phrase of your choice, print a welcome message.
password = "password123"
guess = input("Guess the password")
if guess == password:
    print("Welcome!")

#3.1. Get the user to input their name. If their name is in a list familyMembers (with your family members' names on it), print a welcome message.
name = input("What's your name?")
familyMembers = ["person1", "person2", "person3"] # Insert your own family's names here
if name in familyMembers:
    print("Welcome!")

#FOR AND WHILE LOOPS
#4. Print out all numbers from 1 to 10 using a for loop and a variable. (0,1,2,3,4,5,6...)
for i in range(10):
    print(i)

#4.1 Print out numbers from 1 to 10 but with increments of 2. (0,2,4,6,8)
for i in range(5):
    print(i*2)

#FUNCTIONS
#5. Create a function which takes in 1 parameter, n, and prints out all the numbers from 0 to n.
def myFunction(n):
    print(list(range(n)))

#5.1. Write a function that takes in a list, and returns the greatest value in said list.
def myFunction(n):
    greatest = -10000
    for i in n:
        if i > greatest:
            i = greatest
    return greatest

#Turtle Challenges
#1. Create a function that takes in 3 parameters: x, y, and length. Draw a square at the x,y coordinates with the provided side length.
import turtle

def draw_square(x, y, length):
    myTurtle = turtle.Turtle()
    myTurtle.penup()
    myTurtle.goto(x, y)
    myTurtle.pendown()
    for i in range(4):
        myTurtle.forward(length)
        myTurtle.right(90)

#2. 