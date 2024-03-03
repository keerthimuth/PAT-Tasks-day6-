def first_non_repeating_element(input_list):
    element_count = {}

    for num in input_list:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

    for num in input_list:
        if element_count[num] == 1:
            return num

    return None  # Return None if there is no non-repeating element

if __name__ == "__main__":
    given_list = [3, 5, 2, 7, 5, 3, 8, 10]

    result = first_non_repeating_element(given_list)

    if result is not None:
        print("First non-repeating element:", result)
    else:
        print("No non-repeating element found.")
