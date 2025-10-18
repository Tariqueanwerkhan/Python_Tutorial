# casting in python
a = 1
print(type(a))

b = "1"
print(type(b))

c = int(b)
print(type(c))
print(a+c)

print(a+int(b))

mynum = 24
mynum2 = str(mynum)
print(type(mynum2))

f1 = 34.21
f2 = int(f1)
print(type(f2))
print(f2)

in1 = 30
print(type(float(in1)))


# implicit type casting
var1 = 10        # int type
var2 = 15.5      # float type
var3 = var1+var2
print(var3)
print(type(var3))


# explicit type casting
int_num = 200
str_num = str(int_num)
print(type(str_num))

a0 = bool(0)
print(a0)
print(type(a0))

