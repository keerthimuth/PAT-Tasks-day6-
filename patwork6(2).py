def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_prime_numbers(input_list):
    prime_numbers = [num for num in input_list if is_prime(num)]
    return prime_numbers

if __name__ == "__main__":
    given_list = [10, 501, 22, 37, 100, 999, 87, 351]

    prime_numbers = get_prime_numbers(given_list)

    print("Prime numbers:", prime_numbers)
    print("Count of prime numbers:", len(prime_numbers))
