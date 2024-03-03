def find_min_element(sorted_list):
    if not sorted_list:
        return None  # Return None for an empty list
    
    return sorted_list[0]

if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11, 13]

    result = find_min_element(sorted_list)

    if result is not None:
        print("Minimum element:", result)
    else:
        print("The list is empty.")
