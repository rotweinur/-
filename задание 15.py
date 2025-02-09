#Задание 15
length_cm=float(input())
length_yard=length_cm/(3*12*2.54)
length_mile=length_cm/(1760*3*12*2.54)
length_foot=length_cm/(12*2.54)
length_inch=length_cm/2.54
print(length_yard,'ярдов\n',length_mile,'мили\n',length_foot,'футов\n',length_inch,'дюймов')