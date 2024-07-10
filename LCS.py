def LCS(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # بروز رسانی طولانی‌ترین دنباله
            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# مثال
nums = [2, 3, 1, 255, 1, 155]
result = LCS(nums)
print(result)  # خروجی باید 3 باشد، زیرا طولانی‌ترین دنباله متوالی [1, 2, 3] است.
