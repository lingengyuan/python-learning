first_variable = 10
second_variable = 20

print(first_variable + second_variable)
print(first_variable - second_variable)
print(first_variable * second_variable)
print(first_variable / second_variable)
print(first_variable % second_variable)
print(first_variable ** second_variable)
print(first_variable // second_variable)

third_variable = 3
fourth_variable = 4
third_variable += fourth_variable
print(third_variable)
third_variable -= fourth_variable
print(third_variable)
third_variable *= fourth_variable + 2
print(third_variable)
third_variable /= fourth_variable
print(third_variable)

flag0 = 1 == 1
flag1 = 1 != 1
flag2 = 1 > 2
flag3 = 1 < 2
flag4 = flag0 and flag1
flag5 = flag0 or flag1
print(flag0)
print(flag1)
print(flag2)
print(flag3)
print(flag4)
print(flag5)

##caculate the fahrenheit temperature
##f = c * 9/5 + 32

celsius = 100
fahrenheit = celsius * 9/5 + 32
print("the fahrenheit temperature when celsius = 100 is : " + str(fahrenheit))