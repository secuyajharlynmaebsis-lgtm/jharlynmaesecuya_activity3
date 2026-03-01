secuya_PI = 3.141592653

try:
    secuya_radius = float(input("Enter the value of the radius: "))
    if secuya_radius < 0:
        print("Radius cannot be negative.\n")
    secuya_area =   secuya_PI * secuya_radius ** 2
    print(f"The area of the circle is: {secuya_area:.2f}cm². \n")
except ValueError:
    print("Please enter a number. \n")