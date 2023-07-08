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

# <1408>
h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))
