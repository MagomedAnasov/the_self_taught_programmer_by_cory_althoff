import statistics

# Mean
nums = [1, 5, 33, 12, 46, 33, 2]
print(statistics.mean(nums))

# Median
print(statistics.median(nums))

# Mode
print(statistics.mode(nums))

# Variance
print(statistics.variance(nums, xbar=None))

# Standard deviation
statistics.stdev(nums, xbar=None)