import math

#central limit therome 

def less_than_boundary_cdf(x, mean, std):
    return round(0.5 * (1 + math.erf((x - mean)/ (std * math.sqrt(2)))), 4)

print( less_than_boundary_cdf(9800, 49 * 205, math.sqrt(49) * 15))


total_ticket = int(input())
eager_student = int(input())
mean_eager = float(input())
std_eager = float(input())
cdf = (1+ math.erf((total_ticket - (mean_eager*eager_student)) / (std_eager*math.sqrt(eager_student)*math.sqrt(2)))) * 0.5
print(round(cdf,4))



nums=int(input())
num_lst=list(map(int, input().split()))

def mean(nums): 
    sum = 0 
    for i in nums: 
        sum = sum + i 
    mean = float(sum) / len (nums)
    return mean

def median(nums): 
    sorted_nums= sorted(nums)
    size_nums=len(nums)
    index = (size_nums - 1) // 2
    if (size_nums % 2 !=0):
        median= sorted_nums[index]
    else:
        median= (sorted_nums[index] + sorted_nums[index + 1])/2.0
    return median

def mode(nums): 
    mode = 0
    size = len(nums)
    count, max = 0, 0
    copy = sorted(nums) 
    current = 0
    for i in copy:
        if (i == current):
            count += 1
        else:
            count = 1
            current = i
        if (count > max):
            max = count
            mode = i
    return mode

