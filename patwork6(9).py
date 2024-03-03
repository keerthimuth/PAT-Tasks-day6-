def find_triplet_with_sum(nums, target_sum):
    nums.sort()
    n = len(nums)

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target_sum:
                return nums[i], nums[left], nums[right]
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return None

if __name__ == "__main__":
    given_list = [10, 20, 30, 9]
    target_sum = 59

    result = find_triplet_with_sum(given_list, target_sum)

    if result:
        print("Triplet with sum", target_sum, ":", result)
    else:
        print("No triplet found with the specified sum.")
