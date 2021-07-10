# 1. Biggie Size 
def biggie_size(lst):
    print("Running Biggie Size")
    for i in range(len(lst)-1):
        if i > 0:
            lst[i] = "big"
    return lst
print(biggie_size([-1, 3, 5, -5]))


# 2. Count Positives
def count_positives(lst):
    print("Running Count Positives")
    count = 0
    for i in range(len(lst)):
        if lst[i] > 0:
            count+=1
    lst[len(lst)-1] = count
    return lst
print(count_positives([-1,1,1,1]) )
print(count_positives([1,6,-4,-2,-7,-2]))


# 3. Sum Total
def sum_total(lst):
    print("Running Sum Total")
    sum = 0
    for i in range(len(lst)):
        sum+= lst[i]
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]) )


# 4. Average
def average(lst):
    print("Running Average")
    sum = 0
    avg = 0
    for i in lst:
        sum+= i
    avg = float(sum)/float(len(lst))
    return avg
print(average([1,2,3,4]))


# 5. Length
def length(lst):
    print("Running Length")
    return len(lst)
print(length([37,2,1,-9]))
print(length([]))


# 6. Minimum
def minimum(lst):
    print("Running Minimum")
    if len(lst) == 0:
        return False
    min = lst[0]
    for i in lst:
        if i < min:
            min = i
    return min
print(minimum([37,2,1,-9]))
print(minimum([]))