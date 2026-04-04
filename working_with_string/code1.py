print('LV-1 # types ::  type - str')
name = 'harish'
age = 32
print(f'name is the type of :: {type(name)}')
print(f'age is the type of :: {type(age)}')

# convert to str
print(f'hello this is {name} with age {str(age)} years old ...')

#  =====================================================================
print('LV-2 # MATH :: len - count')
print(f'length of name :: {len(name)} ')

feedback = """python is easy to learn and and simple english language python is easy pitiable language"""
print(f'word python repeats ::',feedback.count('python'))


pwd = 'hari@56789'
print(len(pwd))

if len(pwd) >= 10:
    print("weak pwd not allowed !")
else:
    print("strong set ...")



# COUNT ==>
py_lines = """
Python is easy to learn
python is powerful
python is popular
python is in demand
"""

print("Number of times 'python' appears in the py_lines:", py_lines.count('python'))
print(py_lines.count('Python'))

#  =====================================================================

print('LV-3 # Transformation - replace() ')

date = "2024/06/30"
final_output = date.replace('/', '')
print(f'final_output :: {final_output}')

# EX
price = '1234,98'
print(price.replace(',', '.'))
new_price = float(price.replace(',', '.'))
print(new_price)
print(type(new_price))

# EX
ph_no = '987-990-5432'
new_ph = ph_no.replace('-', '')
print(new_ph)

# EX
price = '$12,567.98'
new_price = float(price.replace('$', '').replace(',', ''))
print(new_price)
print(type(new_price))



# Q-1
"""Convert the messy phone number into a clean number format with only digits
"+49 (176) 123-4567"""

st_1 = """+49 (176) 123-4567$"""
print('*'* 100)
cleaned_st = st_1.replace('+', '').replace(' ', '').replace('(', '').replace(')', '').replace('-', '')
print(cleaned_st)
print('*'* 100)
ls_1 = ['+', ' ', '(', ')', '-','$']

for i in ls_1:
    st_1 = st_1.replace(i, '')

print(st_1)

print('*'* 100)

first_name = "harish"
last_name = "chowdary"

full_name = first_name + ' ' + last_name
print(full_name)

print('*'* 100)

folder = "c:/users/harish/desktop/"
file = "data.txt"
full_path = folder + file
print(full_path)

# f-string
name = 'sai'
age = 80
loc = 'puttaparthi'
print(f'hello {name} i knows you are {age} + years old and you are from {loc}')


print('*'* 100)

print(f'2 + 3 = {2 + 3}')
print(f'{{THIS IS NOT ME}}')


print('*'* 100)


# DATA TRANSFORMATION :: SPLIT() - split a string into a list of substrings based on a specified delimiter.

STAMP = "2024-06-30 14:30:00"
print(STAMP.split(' '))

Time_log = "2024-06-30 14:30:00"
date, time = Time_log.split(' ')
print("Date:", date)
print("Time:", time)

csv_file = '1234,HARI,INDIA,1997-01-21'
print(csv_file.split(','))

# multipler
st = 'ha'
eq = '='
print(st * 5)
print(eq * 20)


# DATA EXTRACTION :: Indexing & Slicing
name = "harish"
print(name[0])
print(name[5])

# extract year date month
date = "2026-04-04"
print(date[0:4]) # year
print(date[5:7]) # month
print(date[8:]) # day

#  =====================================================================

# clean white spaces
txt = "   hello world   "
print(txt.lstrip()) # removes leading and trailing whitespace

print(txt.rstrip()) # removes trailing whitespace

print(txt.strip(' ')) # removes leading and trailing whitespace

tx = "### ABC ###"
print(tx.strip('# ')) # removes leading and trailing whitespace and # characters



# CASE CONVERSION :: upper(), lower(), title(), capitalize()
txt = "hello WORLD"
print(txt.lower())
up = txt.upper()
print(up)


search = "WORLD".lower().strip()
data = 'woRld '.lower().strip()

print(search == data)



# Turn the messy string into a single clean summary with name, role, and age
# "968-Maria, ( Data Engineer ) ¡¡ 27y "
tx = "968-Maria, ( Data Engineer ) ¡¡ 27y"

name = tx[4:9]
print(name)
job = tx[13:27]
print(job)
age = tx[-4:-1]
print(age)

#  =====================================================================
# SEARCH
phone = "+91 7993799109"
print(phone.startswith('+91'))

email = 'harish@gmail.com'
print(email.endswith('@gmail.com'))

em_1 = 'harish@yahoo.com'
print(em_1.endswith('@gmail.com'))

# check '@' in email
print('@' in email)
print('@' in em_1)


url = 'https://api.company.com/v1/data'
print(url.startswith('https://'))
print('api' in url)


# searcing ::
phone_1 = '+91 7993709109'
phone_2 = '91 8125812902'
phone_3 = '91 6123456123'
phone_4 = '+91 9876543210'

print(phone_1[phone_1.find(' ')+1 : ])
print(phone_2[phone_2.find(' ')+1 : ])
print(phone_3[phone_3.find(' ')+1 : ])
print(phone_4[phone_4.find(' ')+1 : ])

#  =====================================================================
# VALIDATION ::  IS ALPHA & IS NUMERIC

name = "harish"
contact = "9876543210"

print(name.isalpha())
print(contact.isdigit())

# PRACTICE-1
username = "   Harish123   "
data_1 = username.strip()
print(data_1)

email = 'har@gmail.com'
if email.endswith('@gmail.com'):
    print("valid email")
else:
    print("invalid email")


phone = "+919876543210"
if phone.startswith('+91') and len(phone) == 13:
    print("valid phone number")
else:    print("invalid phone number")


gm = 'harish@gmail.com'
print(gm.find('@'))