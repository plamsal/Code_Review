import math


def quad(a, b, c):

    a = int(input("Enter the coefficients of a,  separated by commas: "))
    b = int(input("Enter the coefficients of b, separated by commas: "))
    c = int(input("Enter the coefficients of c, separated by commas: "))
    d = ((b ** 2) - (4 * a * c))

    if d < 0:
        a = str("This equation has no real solution")
        return a
    elif d == 0:
        x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        return str("This equation has one solutions: ", x)
    else:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        return str("This equation has two solutions: ", x1, " and", x2)

print(quad(2,3,4))