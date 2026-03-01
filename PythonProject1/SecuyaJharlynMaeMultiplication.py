try:
    secuya_num1 = float(input("Enter the first number: "))
    secuya_num2 = float(input("Enter the second number: "))
    secuya_result = secuya_num1 * secuya_num2
    print(f"The product is: {secuya_result:.2f} \n")
except ValueError:
    print("A ValueError occurred. Please enter a number. \n")