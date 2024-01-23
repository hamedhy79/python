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


msg_dict = {"Q":"A", "S:":"Q", "F":"G", "G":"T", "T":"G", "W":"B", "M":"H"}
msg_crypted = input("enter your crypted message: ").upper()

msg_decrypted = ""

for letters in msg_crypted:
    if letters in msg_dict:
        msg_decrypted += msg_dict[letters]
    else:
        msg_decrypted += letters
        
print(msg_decrypted.lower())




