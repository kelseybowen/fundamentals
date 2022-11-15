# 1. COUNTDOWN

def countdown(number):
    i = number
    result = []
    while i >= 0:
        result.append(i)
        i -= 1
    return result

countdown(5)

# 2. PRINT & RETURN

def print_and_return(nums):
    print(nums[0])
    return nums[1]

print_and_return([1,2])

# 3. FIRST PLUS LENGTH

def first_plus_length(lst):
    return lst[0] + len(lst)

first_plus_length([1,2,3,4,5])

# 4. VALUES GREATER THAN SECOND

def values_greater_than_second(l):
    total = 0
    new = []
    if len(l) < 2:
        return False
    else:
        for i in range(len(l)):
            if l[i] > l[1]:
                total += 1
                new.append(l[i])
    print(total)
    return new

values_greater_than_second([5,2,3,2,1,4])

# 5. THIS LENGTH, THAT VALUE

def length_and_value(n1, n2):
    return [n2 for i in range(n1)]

print(length_and_value(6,2))