def is_happy_number(num):
    seen_numbers = set()

    while num != 1 and num not in seen_numbers:
        seen_numbers.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))

    return num == 1

def count_happy_numbers(input_list):
    happy_numbers = [num for num in input_list if is_happy_number(num)]
    return happy_numbers

if __name__ == "__main__":
    given_list = [10, 501, 22, 37, 100, 999, 87, 351]

    happy_numbers = count_happy_numbers(given_list)

    print("Happy numbers:", happy_numbers)
    print("Count of happy numbers:", len(happy_numbers))
