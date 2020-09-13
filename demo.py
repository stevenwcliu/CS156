import greeting

greeting.do_stuff()

dev = [1, -1, 2, -2, -18]
print(
    max(dev, key=abs))  # min/max is a higher order function; the function returns the ORIGINAL element of the sequence

# lambda expressions as key argument
print(max(dev, key=lambda d: d ** 2))

points = {(2, 2), (0, 3), (1, 4)}  # SET of points
# proxy values: 2 3 4
print(max(points, key=lambda p: p[1]))  # the function returns the original element of the set - !NOT the proxy value

# iClicker
print('\nPage 31 iClicker')


def mystery(anchor, point):
    x, y = point
    return abs(anchor - x)


point = {(2, 2), (0, 3), (1, 4)}
# proxy values: 1 3 2
result = min(point, key=lambda p: mystery(3, p))
print(type(result))
print(result)

print('\nPage 32 iClicker')
prices = {'apples': 2.25, 'oranges': 1.59, 'pears': 1.75}
# can't access item by index
print(3 * prices['pears'])
# when will answer E make sense??

dev = [4, -1, 5, 2, 12, -6, 18, -20]
# generator expressions - high performance, memory efficient; solve the memory restriction
# [] - list expression/comprehension
# eg. total = sum([x ** 2 fox x in rang(1000)])
# () - generator expression; don't need to store the results in memory
# eg. total = sum(x ** 2 fox x in rang(1000))
# general syntax: (element for variable in iterable)


# full qualified address: module name + class name

# when invoking an object
