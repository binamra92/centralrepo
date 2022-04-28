# (0°C × 9/5) + 32
# Celsius to Fahrenheit

# Asking the user to convert the Celsius to Fahrenheit.
user_input = input("What do you wish to convert C or F ? ")
while user_input == 'c' or user_input == 'C' or user_input == 'f' or user_input == 'F':
    try:
        # while userinput is C or F it executes, try and except is there for error.
        while user_input == 'c' or user_input == 'C':
            try:
                Cel = input("Enter your Celsius:")
                Cel_int = float(Cel)
                convert = (Cel_int * 9 / 5) + 32
                print('The Converted Fahrenheit is : ' + str(convert))
                break
            except:
                print("Please enter a Valid response, " + Cel + " ,is not a valid response")

        while user_input == 'F' or user_input == 'f':
            try:
                Cel = input("Enter your Fahrenheit:")
                Cel_int = float(Cel)
                convert = (Cel_int * 9 / 5) + 32
                print('The Converted Celsius is : ' + str(convert))
                break
            except:
                print("Please enter a Valid response, " + Cel + " ,is not a valid response")
                break
    except:
        print("hello")

print(" Not a valid Response, Thank you for using the converter.")
