import random
chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZJ1234567890!@#$%^&*()_-+=<>?|\/~,."''"()[]"

password_len = 15 #Enter the number of characters in your password here
password_count = 2 #Enter the number of passwords you want as an output

#Password generator
password_list = []
for x in range(0,password_count):
    password = " "
    for y in range(0,password_len):
        password_char = random.choice(chars)
        password = password + password_char
    print(password)       
    password_list.append(password)
print(password_list)


        
        
