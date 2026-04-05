print(True)
print(False)
print(bool(True))
print(bool(123))
print(bool("hello"))
print(bool(""))
print(bool(None))
print(bool(0))


user = 'harish'
email = 'h@gm.com'
add = ''
print(any([user,email,add]))
print(all([user,email,add]))

print(isinstance(user, str))
print('*'*100)


# logical operators
# and - or - not

print(8>3 and 5<7)
print('a' < 'b')
print('a' == 'b')

print('har' == 'har' or user == "harish")
print(5>4 or 5>7)



# check if the system is under pressure
cpu_usage = 65
ram_usage = 90

print(cpu_usage > 90 or ram_usage > 80)


# check user credentials before user login
user = True
pwd = True
print(user and pwd)





# chellange ::
# 1Check if a user's name is not empty and the age is greater than or equal to 18
# 2 - Check if the password is at least 8 characters long and does not contain spaces
# 3 - Check if a user's email is not empty, contains '@', and ends with com
# 4 - Check if a username is a string, is not None, and is longer than 5 characters
# 5 - Check if the user is either an admin or a moderator, and either they're not banned or they've
# verified their email

user = 'asdfghjkl'
pwd = ''
age = 18
email = 'h1@gmail.com'
print(user is not None and  len(user)>1 and age >=18)

print("*"*100)
pwd = 'qwertyui'
print(len(pwd)>=8 and ' ' not in pwd)

print(len(email)!= 0 and '@' in email and email.endswith('.com'))
print(isinstance(user,str) and user is not None and len(user)>=5)


is_admin = True
is_moderator = True
is_banned = False
is_verified = False
print((is_admin or is_moderator) and not is_banned or is_verified)
print("*"*100)


import random
# CONDITIONAL STATEMENTS ::
marks = random.randint(50,100)
print(marks)

if marks >= 90:

    print('GRADE-A')
elif marks >= 80 and marks <90:
    print('GRADE B')
elif marks >= 70 and marks <79:
    print('GRADE C')
elif marks >= 60 and marks <69:
    print('GRADE D')
elif marks < 60:
    print('GRADE E')
else:
    print('<< invalid >>>')



