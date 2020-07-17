print('TEST CODE HERE')
def solution(A):
    for n in range(1, 100000):
        if n not in A:
            return n 
            


A = [-1, -2, -3, 0, -5, 6, 3]
print(solution(A))
A = [1, 3, 4, 5, 6]
print(solution(A))
A = [3, 99, 109, 10000]
print(solution(A))
A = [1,2,3,4,5,5,6,6,6,7,7,8,8,9,10,11,12,13,15]
print(solution(A))