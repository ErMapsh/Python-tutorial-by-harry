a, b = 2, 1
print(sum((a, b)))#this is a built in function in py

def docfuction(x, y):
    """this is doc string and here we will return about this function what do"""
    return (x+y)/2

print(docfuction(a, b))
print(docfuction.__doc__)#this is doc string function