# 분할정복 거듭제곱 
# 수학
# XOR 연산에 대하여 아는지 묻는 문제 

def power_modular(base, power, mod):
    base %= mod
    result = 1
    while power:
        if power % 2:
            result = (result * base) % mod
        base = (base * base) % mod
        power //= 2
    return result

def main():
    a, b, n = map(int, input().split())
    mod = 1000000007
    # 2147483648을 n-1의 거듭제곱으로 계산
    result = power_modular(2147483648, n - 1, mod)
    print(result)

if __name__ == "__main__":
    main()

# 밑의 코드는 틀린 코드 
# a,b,n = map(int, input().split())
# result = 1
# a = a % n 
# while b > 0:
#     if b & 1 : 
#         result = (result * a) % n
#     b = b >> 1
#     a = (a*a) % n 
    
# print (result)    
