print("hello Welcome to My module")
a=10
b='hello'

class A:
    pass
def fn():
    a=10
    b=20
    c=a+b
    return c


print(__name__)
if __name__=='__main__':
    print(fn())

    