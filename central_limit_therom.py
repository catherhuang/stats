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
