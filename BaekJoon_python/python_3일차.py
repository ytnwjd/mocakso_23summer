## 그냥 문제풀이 ..

# <10797>
# day = int(input())
# num_list = list(map(int, input().split()))
# cnt = 0
# for c in num_list:
#     if (day==c):
#         cnt += 1
# print(cnt)

# <2440>
# num = int(input())
# for i in range(num, 0, -1):
#     print("*"*(i))

# <2441>
# num = int(input())
# for i in range(num):
#     print(" "*(i) + "*"*(num-i))

# <9259>
# num = int(input())
# for i in range(num):
#     a, b = map(int, input().split())
#     print("Case {}: {}".format(i+1, a+b))

# <11098>
# num = int(input())
# for _ in range(num):
#     player = int(input())
#     max = 0
#     max_name = ""
#     for _ in range(player):
#         money, name = input().split()
#         money = int(money)
#         if(money > max):
#             max = money
#             max_name = name
#     print(max_name)

# <1546>
# cnt = int(input())
# score_list = list(map(int, input().split()))
# max = max(score_list)
# sum = 0
# for c in range(cnt):
#     score_list[c] = score_list[c] / max * 100
#     sum += score_list[c]
# print(sum/cnt)

# <5565>
# total = int(input())
# for _ in range(9):
#     total -= int(input())
# print(total)

# <10178>
# cnt = int(input())
# for i in range(cnt):
#     a, b = map(int, input().split())
#     num_1 = a//b
#     num_2 = a%b
#     print(f"You get {a//b} piece(s) and your dad gets {a%b} piece(s).")

# <2475>
# num_list = list(map(int, input().split()))
# sum = 0
# for i in num_list:
#     sum += (i*i)
# print(sum%10)

# <2455>
# sum = 0
# sum_li = []
# for _ in range(4):
#     i, o = map(int, input().split())
#     sum = sum-i+o
#     sum_li.append(sum)
# print(max(sum_li))

# <2506>
# num = int(input())
# cor_list = list(map(int, input().split()))
# sum = 0
# score = 1
# for i in range(num):
#     if(cor_list[i] == 1):
#         sum += score
#         score += 1
#     if(cor_list[i]==0):
#         score = 1
# print(sum)

# <2010>
# import sys
# cnt = sys.stdin.readline()
# cnt = int(cnt)
# total = 0
# for _ in range(cnt):
#     total += int(sys.stdin.readline())
# print(total - (cnt-1))

# <2442>
# cnt = int(input())
# for i in range(1, cnt+1):
#     print(" " * (cnt-i) + "*" * (2*i-1))

# <10984>
cnt = int(input())
for i in range(cnt):
    num = int(input())
    sum_c = 0
    c_mul_g = 0.0
    for j in range(num):
        c, g = input().split()
        c = int(c)
        g = float(g)
        sum_c += c
        c_mul_g += float(c*g)
    print("{} {.1f}".format(sum_c, c_mul_g/sum_c))
