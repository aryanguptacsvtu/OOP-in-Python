def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using this function.")
    return mfx
    
@greet
def hello():
    print("Hello world")

@ greet
def add(a,b):
    print(a+b)

hello()
# greet(hello)()

add(1,2)
# greet(add)(1,2)

# A 'Decorator' is a function that takes another function as argument & returns a new function that modifies the behaviour of original function.