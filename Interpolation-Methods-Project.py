#https://github.com/shiraz09/Interpolation-Methods-Project.git
#Shiraz Nagaoker 208324194
#Moran Avraham 211778634
#Gabriela brailovsky 318804291
#Ream levi 205866692
#Yarden skaked 206789885


import numpy as np


# Helper function to validate user input
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Helper function to calculate coefficients for quadratic interpolation
def solve_quadratic_coefficients(x_values, y_values):
    matrix = np.array([
        [x_values[0] ** 2, x_values[0], 1],
        [x_values[1] ** 2, x_values[1], 1],
        [x_values[2] ** 2, x_values[2], 1]
    ])
    return np.linalg.solve(matrix, y_values)


# Function to collect coordinates with optional label for customization
def collect_coordinates(method_name=""):
    points_required = 3 if method_name in {'quadratic', 'lagrange'} else 2
    points = []
    for i in range(points_required):
        x = get_float_input(f"Enter X coordinate for point {i + 1}: ")
        y = get_float_input(f"Enter Y coordinate for point {i + 1}: ")
        points.append((x, y))
    return points


# Linear interpolation function
def linear_interpolation(points, x_target):
    (x1, y1), (x2, y2) = points
    if x1 == x2:
        raise ValueError("X values must be distinct for linear interpolation.")

    gradient = (y2 - y1) / (x2 - x1)
    return y1 + gradient * (x_target - x1)


# Quadratic interpolation function with the help of a helper function
def quadratic_interpolation(points, x_target):
    x_values = [p[0] for p in points]
    y_values = [p[1] for p in points]

    a, b, c = solve_quadratic_coefficients(x_values, y_values)
    return a * x_target ** 2 + b * x_target + c


# Lagrange interpolation function
def lagrange_interpolation(points, x_target):
    result = 0
    for i in range(len(points)):
        xi, yi = points[i]
        li = 1
        for j in range(len(points)):
            if i != j:
                xj = points[j][0]
                li *= (x_target - xj) / (xi - xj)
        result += yi * li
    return result


# Function to map user selection to method names and functions
def select_interpolation_method(choice):
    method_mapping = {
        '1': ('linear', linear_interpolation),
        '2': ('quadratic', quadratic_interpolation),
        '3': ('lagrange', lagrange_interpolation)
    }
    return method_mapping.get(choice, (None, None))


# Main menu function with the display and logic for selection
def show_menu():
    while True:
        print("\nInterpolation Options:")
        print("1. Linear Interpolation")
        print("2. Quadratic Interpolation")
        print("3. Lagrange Interpolation")
        print("4. Exit")

        choice = input("Please select an option: ")
        if choice == '4':
            print("Exiting the program.")
            break

        method_name, method_function = select_interpolation_method(choice)
        if method_function is None:
            print("Invalid option, please choose again.")
            continue

        points = collect_coordinates(method_name)
        x_target = get_float_input("Enter the X value for interpolation: ")
        y_result = method_function(points, x_target)

        print(f"Interpolated Y value at X = {x_target} is {y_result}")


if __name__ == "__main__":
    show_menu()