a = 0
i = 0
b = 1
c = a + b
r = int(input("Enter no. of entries in series "))
print(a)
print(b)
print(c)
for i in range(r - 3):
    a = b
    b = c 
    c = a + b
    print(c)
