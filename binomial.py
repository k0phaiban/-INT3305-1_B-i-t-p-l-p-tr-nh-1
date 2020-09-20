import math
#Hàm tính giai thừa
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def prob(n, p, N):
    return factorial(N)/(factorial(n)*factorial(N - n))*(p ** n)*(1 - p)**(N - n)

def infoMeasure(n, p, N):
    return -math.log(prob(n, p, N), 2)

def sumProb(N, p):
    #Tính tổng của xác suất của các symbol n của nguồn thông tin binomial n chạy từ 1 đến N
    sumary = 0 
    for i in range(1, N + 1):
        sumary += prob(i, p, N)

    return sumary

def approxEntropy(N, p):
    #Tính entropy của phân bố binomial
    sumary = 0
    for i in range(1, N + 1):
        sumary += prob(i, p, N)*infoMeasure(i, p, N)
    return sumary