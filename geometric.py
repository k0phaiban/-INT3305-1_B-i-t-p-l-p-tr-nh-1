import math
def prob(n, p):
    return ((1 - p)**(n-1))*p

def infoMeasure(n, p):
    return -math.log(prob(n, p), 2)

def sumProb(N, p):
    # Để chứng minh tổng xác suất của phân bố geometric bằng 1, ta có thể cho N = 10000 và p = 0.5 để mô phỏng việc tung đồng xu. 
    # Kiểm chứng kết quả bằng cách in ra giá trị của hàm sumProb
    sumary = 0 
    for i in range(1, N + 1):
        sumary += prob(i, p)

    return sumary

def approxEntropy(N, p):
    # Vì entropy là giá trị trung bình của các nguồn tin nên hàm này sẽ tính được entropy của nguồn tin geometric. 
    # Để chứng minh entropy của nguồn tin này bằng 0.5, lấy N = 1000 và p = 0.5.
    sumary = 0
    for i in range(1, N + 1):
        sumary += prob(i, p)*infoMeasure(i, p)
    return sumary