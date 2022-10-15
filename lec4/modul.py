x=5
y=3
def init(a,b):
    global x,y
    x=a
    y=b
def sum():
    return x+y
init(x,y)
print(x,y)