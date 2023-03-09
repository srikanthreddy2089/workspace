"""
As the name suggests, filter creates a list of elements for which a function returns true
"""

number_list = range(-5, 5)
print filter(lambda x: x < 0, number_list)

