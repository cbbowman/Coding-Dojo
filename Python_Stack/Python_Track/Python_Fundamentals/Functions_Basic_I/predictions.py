#1
print("Prediction: 1")
print(5)

def a():
    return 5
print(a())

#2
print("Prediction: 2")
print(10)

def a():
    return 5
print(a()+a())

#3
print("Prediction: 3")
print(5)

def a():
    return 5
    return 10
print(a())

#4
print("Prediction: 4")
print(5)

def a():
    return 5
    print(10)
print(a())

#5
print("Prediction: 5")
print(5,"undefined")

def a():
    print(5)
x = a()
print(x)

#6
print("Prediction: 6")
print(3,5,"undefined")

def a(b,c):
    print(b+c)
#print(a(1,2) + a(2,3))

#7
print("Prediction: 7")
print("2 5")

def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#8
print("Prediction: 8")
print(100,10)

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#9
print("Prediction: 9")
print(7,14,21)

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#10
print("Prediction: 10")
print(8)

def a(b,c):
    return b+c
    return 10
print(a(3,5))

#11
print("Prediction: 11")
print(500,500,300,500)

b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#12
print("Prediction: 12")
print(500,500,300,500)

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

#13
print("Prediction: 13")
print(500,500,300,300)

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#14
print("Prediction: 14")
print(1,3,2)

def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#15
print("Prediction: 15")
print(1,3,5,10)

def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

