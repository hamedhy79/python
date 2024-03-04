#1
# list_1= {"reza":50,"ali": 45,"hamed":54,"milad":45}

# list_1.items()

# for name, list_1 in list(list_1.items()):
#     print(f"name is {name} and weight is {list_1}")
    
    
#2  
# names_age = {"ali": 15, "hasan": 17, "reza": 18, "hamed":20}

# names_age.items()

# for name , names_age in list(names_age.items()):
#     print(f"hello mr.{name} your score is {names_age}")
    
    

#3
# std = "hamed7@email.com"

# (username ,domain) = std.split('@')
# print("username is %s and domain is %s" % (username, domain))


#4
# leters = ("a", "d", "s", "h", "w", "q")

# message = input("write your message: ")
# new_message = ""

# for letter in message:
#     if letter not in leters:
#         new_message = new_message+letter
        
# print("your message %s" % (new_message))


#5
# msg_dict = {"A":"Q", "Q:":"S", "G":"F", "T":"G", "J":"T", "B":"W", "H":"M"}


# message = input("enter your message: ").upper()
# msg_encrypted = ""

# for letter in message:
#     if letter in msg_dict:
#         msg_encrypted += msg_dict[letter]
#     else:
#         msg_encrypted += letter

# print(msg_encrypted.lower())

#6
# msg_dict = {"Q":"A", "S:":"Q", "F":"G", "G":"T", "T":"G", "W":"B", "M":"H"}
# msg_crypted = input("enter your crypted message: ").upper()

# msg_decrypted = ""

# for letters in msg_crypted:
#     if letters in msg_dict:
#         msg_decrypted += msg_dict[letters]
#     else:
#         msg_decrypted += letters
        
# print(msg_decrypted.lower())

#7
# def add(a,b):
#     return(a+b)
# def zarb(a,b):
#     return(a*b)
# def divide(a,b):
#     return(a/b)
# def tafrig(a,b):
#     return(a-b)

# print("1 : add")
# print("2 : zarb")
# print("3 : divide")
# print("4 : tafrig")

# choice_num = input("please choice once number 1/2/3/4: ")

# num_1 = int(input("please select your first num: "))
# num_2 = int(input("please select your second num: "))


# if choice_num == "1":
#     print(num_1, "+" ,num_2, "=", add(num_1,num_2))
# elif choice_num == "2":
#     print(num_1, "*" ,num_2, "=", zarb(num_1,num_2))
# elif choice_num == "3":
#     print(num_1, "/" ,num_2, "=", divide(num_1,num_2))
# elif choice_num == "4":
#     print(num_1, "-" ,num_2, "=", tafrig(num_1,num_2))

# else:
#     print("not valid")

#8
# import re
# p = input("Enter Your Password: ")

# x = True
# while x:
#     if (len(p)<6 or len(p)>16):
#         break
#     elif not re.search("[a-z]", p):
#         break
#     elif not re.search("[A-Z]", p):
#         break
#     elif not re.search("[0-9]", p):
#         break
#     elif not re.search("[!@#$]", p):
#         break
#     else:
#         print("Your Password Is Valid")
#         x = False
#         break
# if x:
#     print("invalid Password")



#9
# myfanc = lambda x : x * 2
# print(myfanc)

# listA = [1, 10, 15, 50, 68, 23, 18]

# # print(list(map(lambda x : 'big' if x>15 else 'small', listA)))
# print(list(filter(lambda x : x%2 == 0, listA)))

# safe = [1, 15, 40, 25, 60, 44, 95, 64]

# print(list(map(lambda x : x** 2, safe)))


# number10
# def first(n):
#     num = 0
#     while(num<n):
#         yield num
#         num += 1
    
# for i in first(10):
#     print(i * 2)

#number11
# x = 5
# my_func = lambda x : x * 2
# print(my_func(x))  
# __________________________________
# lista = [2, 3, 10, 14]
# print(list(map(lambda a : a ** 2 + 5, lista)))
# __________________________________


#replace char in str
# x = 'hello'
# print(x.replace('h', 'm'))


#binary decimal hex
# from decimal import Decimal
# #for divide
# from fractions import Fraction
# print(Decimal('0.1') + Decimal('0.3'))
# # print(Decimal(0.1) + Decimal(0.3))
# print(Fraction(0.75))


#-------method in python-------
#complexNo Numberic
#muhomi&real
# x = 2 + 3j
# print(x.real)
# print(x.imag)

x = 'ali\'s dad'
y = {'ali', 'hasan'}
# print(x not in y)
# print(x.startswith('a'))#start with a char -->True
# print(x.endswith('i'))#end with i char -->False
# print(x.find('l'))#search in str 
# print(x.index('l'))
# print(x.isnumeric())#sign str exists number string inside it
# print(x.split('a'))#delete char from list
# print(x.strip('a'))#delete char from list
# print(x.strip(r'i'))#delete char from list right side. for left (l'')
# print(x.capitalize())#upper first char

#unicode ascii
# a = 'i'
# b = ("char:\u03C0")#unicode
# print(ord(a))#this func for ascii char
# print(b)


#types of format
name = 'hasan'
age = 23
degree = 'bachelor'
print('your name is %s and age is %i years old also your degree is %s' %(name,age, degree))
print('your name is {} and age is {} years old also your degree is {}'.format(name,age, degree))
print(f'your name is {name} and age is {age} years old also your degree is {degree}')

