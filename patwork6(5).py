def distribute_mangoes(mango_bags, num_students):
    if num_students > len(mango_bags):
        print("Error: Not enough mango bags for each student.")
        return None

    mango_bags.sort()

    min_difference = float('inf')
    distribution = []

    for i in range(len(mango_bags) - num_students + 1):
        current_difference = mango_bags[i + num_students - 1] - mango_bags[i]

        if current_difference < min_difference:
            min_difference = current_difference
            distribution = mango_bags[i:i + num_students]

    return distribution

if __name__ == "__main__":
    mango_bags = [10, 5, 22, 37, 100, 99, 87, 351]
    num_students = 3

    result = distribute_mangoes(mango_bags, num_students)

    if result:
        print("Distribution of mangoes:", result)
    else:
        print("Unable to distribute mangoes.")
