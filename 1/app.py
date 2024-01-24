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
import re
p = input("Enter Your Password: ")

x = True
while x:
    if (len(p)<6 or len(p)>16):
        break
    elif not re.search("[a-z]", p):
        break
    elif not re.search("[A-Z]", p):
        break
    elif not re.search("[0-9]", p):
        break
    elif not re.search("[!@#$]", p):
        break
    else:
        print("Not Valid")
        x = False
        break
if x:
    print("Your Password Is Valid")

