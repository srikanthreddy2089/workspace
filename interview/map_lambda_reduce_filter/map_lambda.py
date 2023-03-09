"""
Doc: http://book.pythontips.com/en/latest/map_filter.html
applies a function to all the items in an input_list
Most of the times we want to pass all the list elements to a function one-by-one and then collect the output. For instance:
"""


items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
print squared


items = [1, 2, 3, 4, 5]
print map(lambda x: x**2, items)


"""
Instead of a list of inputs we can even have a list of functions
"""
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]

for i in range(5):
    print tuple(map(lambda x:x(i),funcs))
    print map(lambda x:x(i),funcs)
    print list(map(lambda x:x(i),funcs))

