msg = "Hello Python!"
print(msg)
msg = "Change Hello Python --> Hello World! 1.2"
print(msg)
print(msg.capitalize())
print(msg.split())
a = msg.split()
b = ['Change','Hello','Python']
c = [1.2,'Hello','W', 2]

if str(c[0]) in a:
    print(a[2] + ' ' + str(len(a)))
else: print ('Not found!:' +str(len(a)) )

for abc in a:
    print("aLst: ", abc) 
print(a[0:22])
del a[1:5]
print(a)
# noi mang
print(a + c)
# append mang
a.append('HuynhDH')
# insert array
a.insert(2,'HuynhCutGa')
print(a)
print(a.index('HuynhDH'))
# Reverse array
a.reverse()
print(a)
# Sort array
# Sort tang dan
a.sort()
print(a)
# Dao mang sort giam gian
a.reverse()
print(a)
