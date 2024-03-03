def sum_of_first_and_last_digit(number):
    # Convert the number to a string to easily access individual digits
    num_str = str(number)

    # Extract the first and last digits
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])

    # Calculate the sum
    total_sum = first_digit + last_digit

    return total_sum

if __name__ == "__main__":
    user_input = int(input("Enter an integer: "))

    result = sum_of_first_and_last_digit(user_input)

    print("Sum of first and last digit:", result)
