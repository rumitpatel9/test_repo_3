#......string methods...........

s1 = "hello tridhya tech"
print(s1.replace(s1[0:5],''))
print(s1.index('h'))
print(s1.find('z'))
print(s1.upper())
print(s1.lower())
print(s1.capitalize())
print(s1.title())
print(len(s1))
string_to_list = s1.split()
print(string_to_list)
print(s1.isupper())
print(s1.islower())
print(s1.count('h'))
#removing blank space from the first and lat of the string
s2 = "       hyyyy          "
s3 = s2.strip()
print(s3)


##.....list methods..........
l1 = [1,2,3,4,5,6,7,8,9,10]
l1.append(11)
l1.insert(0,0)
l1.extend([12,13])
l1.reverse()
l1.pop(0)
# list_to_string =''.join(l1)
# print(list_to_string)
print(l1.index(1))
print(len(l1))
print(l1)
