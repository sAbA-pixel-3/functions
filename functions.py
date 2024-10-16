# functions
# def nums(f_num, s_num):
#     print(f_num + s_num)
# nums(3, 2) 



# arguments
# def hello(name, age, male):  # it is an argument
#     print(f"hello {name}, {age}, {male}") 
# hello("alikhan", 12, "M") 

# def hello(name, age, male='m'): 
#     print(f"hello {name}, {age}, {male}")
# hello("Ali", 12, "W") # is prioratized 



# POSITIONAL and NAME arguments
# def hello(name, age, male): 
#     print(f"hello {name}, {age}, {male}")
# hello("Ali", 12, male="W") #POSITIONALS go First and then NAME  

# def nums(f_num, s_num):
#     print("Sum: ", f_num + s_num)
# nums(3, 2) 



# ARGS and KWARGS
# def nums(*args, **kwargs): # args - arguments (infinit number of POSITIONAL args) 
#     print(args)
#     print(kwargs) # key words args - (infinit number of NAME args)
# nums(1,2,3,4,5,6,7,8,9,10, name="Ali", age=12, male="W")  



# Возвращаемые значения фун-ии
# def hello(name, age, male):
#     return f"Hello {name}, {male}"
# print(hello("ali", 12, "w")) 

# def hello():
#     n = 5+9
#     return n # returns function
# print(hello() + 6) 



# Область видимости

# def hello(name):
#     name = "bob"
#     return f"hello {name}"
# print(hello()) 



# LAMBDA (анонимная) 

# num = lambda a, b: a + b
# print(num(5, 6)) 



# вложенные фун-ии

# def hello(name):
#     def inner():
#         print(f"hello {name}")
#     inner() # вызов вложенной фун-ии
# hello("Ali") 



# замыкание

# def hello(msg):
#     def n():
#         print(msg)
#     return n 
# g = hello("hi bro") 
# g() 



# рекурсия 

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1) 
# print(factorial(5))




# def contamination(text, char):
#     print(text) 
#     print(char * len(text))  
# contamination("Hello World!", input("enter any char: "))


# name1 = input("Enter first name: ")
# name2 = input("Enter last name: ")
# n1 = name1[0].capitalize()
# n2 = name2[0].capitalize()
# print(f"{n1}. {n2}")


# point_a = int(input("enter 'point a' num from -50 to 50: "))
# point_b = int(input("enter 'point b' num from -50 to 50: "))
# calc1 = (-50) - point_a
# calc2 = (-50) - point_b
# res = calc1 - calc2
# print(f"The distance between 'a' and 'b' is '{res}'") 


def multiplication_table(size):
    return [[(i + 1) * (j + 1) for j in range(size)] for i in range(size)]
size = 3
table = multiplication_table(size)
print(table) 