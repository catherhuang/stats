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

print (mean(num_lst))
print (median(num_lst))
print (mode(num_lst))


def weighted_mean(x, w): 
    divisor=0
    divident= 0
    for i in range(0, len(x)): 
            divident = divident + (x[i]*w[i])
            divisor = divisor+w[i]
    wm =round((divident / divisor), 1) 
    return wm

print (weighted_mean(x, w))


from statistics import median




quartiles 
n=int(input())
arr=[int(x) for x in input().split()]
arr.sort()
t=int(len(arr)/2)
if len(arr)%2==0:
    L=arr[:t]
    U=arr[t:]
else:
    L=arr[:t]
    U=arr[t+1:]
    
print(int(median(L)))
print(int(median(arr)))
print(int(median(U)))



n_lst = list(map(int, input().split()))

def stdv(lst): 
    size=len(lst)
    if size <1: 
        stdv=0
    else: 
        mean=sum(lst)/size
        diff_sum=0
        for i in lst: 
            diff= (i-mean)**2
            diff_sum = diff_sum+diff
        diff_avg=diff_sum/size
        stdv=round((diff_avg**.5), 1) 
    return print(stdv)

stdv(n_lst)


import math

def bi_dist(x, n, p):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
    return(b)

b, p, n = 0, 1.09/2.09, 6
for i in range(3,7):
    b += bi_dist(i, n, p)   
print("%.3f" %b)

#least square regression line 
x, y =[], []
for i in range ( 5): 
    student = [int(i) for i in input().split()]
    x=x+[student[0]]
    y=y+[student[1]]

mean_x=sum(x)/len(x)
mean_y=sum(y)/len(y)

x_squared=sum([x[i]**2 for i in range(5)])
xy = sum([x[i]*y[i] for i in range(5)])
b=(len(x)*xy - sum(x)*sum(y))/(len(x)*x_squared - sum(x)**2) 
a=mean_y-b*mean_x
ans=a+b*80
print(round(ans, 3))




