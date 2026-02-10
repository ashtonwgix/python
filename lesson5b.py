# functions with parameters 
# example 1
def greeting(name) :
    print("Good Afternoon" , name)

# call the function 
greeting("Brown")

# example 2
def addition (num1 , num2) :
    answer=num1 + num2
    print("the sum is" , answer)

# call the function 
addition(40,60)

# NB// a function is a reusable block of code that has one specific job

# example 3 

addition(150 , 900)


addition(800 , 3200)


addition(-1500 , -40)

# assignment 
def interest (principle , time , rate) :
    answer=principle * rate/100 * time 
    print("the interest is" , answer)

# call the function 
interest(30000 , 40 , 3)


def BMI (weight , height) :
    answer=weight / height**height 
    print("the BMI is" , answer)

# call the function 
BMI(69 , 1.6)

def area (height , base) :
    answer=height * base / 0.5
    print("the area is" , answer)

# call the function 
area(20 , 15)