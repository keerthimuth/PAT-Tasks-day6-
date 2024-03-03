def find_duplicates(list1, list2, list3):
    # Concatenate the three lists to create a single list
    combined_list = list1 + list2 + list3

    # Create a dictionary to count occurrences of each element
    element_count = {}
    duplicates = set()

    for element in combined_list:
        if element in element_count:
            duplicates.add(element)
        else:
            element_count[element] = 1

    return list(duplicates)

if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    list3 = [5, 6, 7, 8, 9]

    result = find_duplicates(list1, list2, list3)

    if result:
        print("Duplicates found:", result)
    else:
        print("No duplicates found.")
