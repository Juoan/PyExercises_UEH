from ctypes import pythonapi

import math

# Ex1:
def area_of_tri():
    base = float(input("Enter Base: "))
    height = float(input("Enter Height: "))

    area = 0.5 * base *height

    print(f"\nArea of the triangle is: {area}")

# Ex2:
def peri_of_tri():
    side_a = float(input("Enter side A: "))
    side_b = float(input("Enter side B: "))
    side_c = float(input("Enter side C: "))

    perimeter = a + b + c

    print(f"\nPerimeter of a triangle is: {perimeter}")

# Ex3:
def area_n_peri_of_rec():
    length = float(input("Enter length: "))
    width = float(input("Engter width: "))

    print(f"Area of the rectangle is: {length*width}")
    print(f"Perimeter of the rectangle is: {2*(length+width)}")

# Ex4:
def area_n_circum():
    radius = float(input("Enter radius: "))

    print(f"Area of the circle is: {math.pi*radius*radius:.2f}")
    print(f"Circumference of the circle is: {2*math.pi.radius:.2f}")

# Ex5:
def calc_equation():
    # Equation: y = 2x - 2
    slope = 2
    y_intercept = -2
    x_intercept = y_intercept / -slope

    print(f"Slope: {slope}")
    print(f"Y-intercept: {y_intercept}")
    print(f"X-intercept: {x_intercept}")

# Ex 6:
def calc_points(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    print(f"Slope: {slope}")
    print(f"Euclidean Distance: {distance:.2f}")

# Ex8:
def calc_quadratic(a, b, c):
    for x in range(-10, 11):
        y = x**2 + 6*x + 9
        print(f"x = {x}, y = {y}")
        if y == 0:
            print(f"y equals 0 when x = {x}")

# Ex9:
def falsy_comp():
    x = "python"
    y = "dragon"

    print(len("python") != len("dragon"))  # Output: False

# Ex10:
def find_on():
    print('on' in 'python' and 'on' in 'dragon')

# Ex11:
def find_jargon():
    sentence = input("Enter a sentence: ")
    print('jargon' in sentence)

# Ex13:
def conv_str():
    text = "python"
    length = len(python)
    len_float = float(length)

    return str(len_float)

# Ex14.
def is_even():
    num = int(input("Enter a number: "))
    print("The number is even!") if num % 2== 0 else print("The number is odd!")

# Ex15.
def salary():
    hrs = int(input("Hours per day for work (in USD): "))
    rate = int(input("Pay per hour: "))

    print(f"Your salary per month is: {(rate*hrs)*30} USD")

# Ex16:
def cal_sec():
    age = int(input("Enter current age: "))

    print(f"you can live for the next {(100-age)*86400} seconds")

if __name__ == '__main__':
