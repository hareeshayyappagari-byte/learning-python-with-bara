# NUMERIC :: Types : type() , int() , float(), complex()
import math
from random import randint

age = 32
height = 5.6
z = 3+9j

print(type(age))
print(type(height))
print(type(z))


# convert data to numerical
x = '24'
print('x is of type ::',type(x)) # type str
# convert to whole number
x = int(x)
print('x is of type ::',type(x))



x = 3.12
print('x is of type ::',type(x))
# convert to int
x = int(x)
print('x is of type ::',type(x))
x = float(x)
print('x is of type ::',type(x))
x = str(x)
print('x is of type ::',type(x))

x = 3
y = 4
z = 2
x = complex(x,y)
print('complex of x and y :: ',x)

print(complex(y,z))


# =======================================
# NUMERIC :: Math operator
# =======================================
print(2 + 1)
print(3 - 2)
print(4 * 3)
print(5 / 4)
print(6 // 5)
print(7 % 6)
print(8 ** 7)

x = 3
x = x+2




# =======================================
# NUMERIC :: Measure distance

print(abs(3 - 12)) # absolute - non negative

# Rounding
x = 22.563201
print(round(x)) # rounding to the even number

print("floor :: ",math.floor(x)) # rounding to down
print('ceil :: ',math.ceil(x)) # round to even
print('trunc :: ',math.trunc(x))
# =======================================
# NUMERIC :: random - randint
import random

print(random.random()) # get decimal number form 0.0 to 1.0
print(random.randint(2,10)) # get integer number with in start and end number

# ======================================
# Validation :: is integer - isinstance
x = 7.0
print(x.is_integer())

x = 7.3
print(x.is_integer())

# to check the type
n = 3
print(isinstance(n, int))

fl = 3.19
print(isinstance(fl, float))

cmp = 3+9j
print(isinstance(cmp, complex))

st = 'hari'
print(isinstance(st, str))
# ======================================