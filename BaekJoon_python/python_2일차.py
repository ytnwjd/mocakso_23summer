## 단계별 문제풀이

# <3단계-반복문>
# <2739>
# num = int(input())
# for i in range(1, 10):
#     print(num, "*", i, "=", num*i)

# <10950>
# cnt = int(input())
# for c in range(cnt):
#     A, B = map(int, input().split())
#     print(A+B)

# <8393>
# num = int(input())
# result = 0
# for n in range(num):
#     result += (n+1)
# print(result)

# <25304>
# sum = int(input())
# cnt = int(input())
# total = 0
# for i in range(cnt):
#     a, b = map(int, input().split())
#     total += (a*b)
# if(sum==total):
#     print("Yes")
# else:
#     print("No")

# <25314>
# num = int(input())
# num = num//4
# for n in range(num):
#     print("long", end=" ")
# print("int")

# <15552>
# import sys  # 파이썬 인터프린터가 제공하는 변수나 함수를 제어하는 모듈
# cnt = int(input())
# for c in range(cnt):
#     A, B = map(int, sys.stdin.readline().split())
#     print(A+B)

# <11021>
# num = int(input())
# for n in range(num):
#     a, b = map(int, input().split())
#     print("Case #{}: {}" .format(n+1, a+b))

# <11022>
# num = int(input())
# for n in range(num):
#     a, b = map(int, input().split())
#     print("Case #{}: {} + {} = {}" .format(n+1, a, b, a+b))

# <2438>
# cnt = int(input())
# for c in range(1, cnt+1):
#     print(" "*(cnt-c) + "*"*(c))

# <10952>
# while True:
#     a, b = map(int, input().split())
#     if(a==0 & b==0):
#         break
#     print(a+b)

# <10951>
# while True:
#     try:    
#         a, b = map(int, input().split())
#         print(a+b)
#     except:     # Eof == ctrl+z 를 위해 예외처리
#         break

# <4단계-1차원 배열>
# <10807>
# cnt = int(input())
# num_list = list(map(int, input().split()))
# num = int(input())
# total = 0
# for c in num_list:
#     if(c==num):
#         total += 1
# print(total)

# <10871>
# a, n = map(int, input().split())
# num_list = list(map(int, input().split()))
# for x in num_list:
#     if(n > x):
#         print("{} " .format(x), end="")

# <10818>
# num = int(input())
# num_list = list(map(int, input().split()))
# print(min(num_list), max(num_list))

# <2562>
# num_list = []
# for i in range(9):
#     num = int(input())
#     num_list.append(num)
#     num_max = max(num_list)
#     num_index = num_list.index(max(num_list))
# print(num_max)
# print(num_index+1)
