def has_zero_sum_sublist(nums):
    prefix_sum = 0
    seen_sums = set()

    for num in nums:
        prefix_sum += num

        if prefix_sum == 0 or prefix_sum in seen_sums:
            return True

        seen_sums.add(prefix_sum)

    return False

if __name__ == "__main__":
    given_list = [4, 2, -3, 1, 6]

    result = has_zero_sum_sublist(given_list)

    if result:
        print("There is a sub-list with sum equal to zero.")
    else:
        print("No sub-list with sum equal to zero found.")
