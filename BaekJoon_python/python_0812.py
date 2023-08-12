# 그냥 문제풀이
# <5717>
# while(True):
#     a, b = map(int, input().split())
#     if(a==0 and b==0):
#         break
#     print(a+b)

# <10156>
# k, n, m = map(int, input().split())
# if(k*n > m):
#     print(k*n-m)
# else:
#     print(0)

# <8958>
# case = int(input())
# for _ in range(case):
#     sum = 0
#     grad = 0
#     string = input()
#     for j in string:
#         if(j == "O"):
#             grad += 1
#             sum += grad
#         else:
#             grad = 0
#     print(sum)

# <10989>
# import sys
# input = sys.stdin.readline
# num = int(input())
# num_li = [0]*10001

# for _ in range(num):
#     num_li[int(input())] += 1    #입력받은 수에 해당하는 인덱스 값 +1
# for i in range(10001):
#     if (num_li[i] != 0):
#         for j in range(num_li[i]):
#             print(i)

# <5355>
# n = int(input())
# for _ in range(n):
#     s = list(map(str, input().strip().split()))
#     num = float(s[0])
#     for j in range(1, len(s)):
#         if(s[j] == "@"):
#             num *= 3
#         elif(s[j] == "%"):
#             num += 5
#         elif(s[j] == "#"):
#             num -= 7
#     print("%.2f" % num)

# <별찍기>
# for i in range(5):
#     for j in range(9):
#         if (i+j) % 2 == 0:
#             print("*", end="")
#         else:
#             print("-", end="")
#     print()

# <7657 >
# dish = input()
# total = 10
# for i in range(1, len(dish)):
#     h = 10
#     if (dish[i] == dish[i-1]):
#         h = 5
#         total += h
#     else:
#         total += h
# print(total)

# <10102>
# num = int(input())
# vote = input()
# cnt_a = 0
# cnt_b = 0
# for i in vote:
#     if (i == "A"):
#         cnt_a += 1
#     else:
#         cnt_b += 1
# if(cnt_a > cnt_b):
#     print("A")
# elif(cnt_a < cnt_b):
#     print("B")
# else:
#     print("Tie")

# <10817>
# num = list(map(int, input().split()))
# num = sorted(num)
# print(num[1])

# <2476>
# num = int(input())
# arr = []
# tot = 0
# for i in range(num):
#     a, b, c = map(int, input().split())
#     if (a == b and b == c and a == c):
#         tot = 10000 + a*1000
#         arr.append(tot)
#     elif (a != b and b != c and a != c):
#         tot = max(max(a,b),c)*100
#         arr.append(tot)
#     else:
#         if(a==b):
#             tot = 1000 + a*100
#         elif(b==c):
#             tot = 1000+b*100
#         else:
#             tot = 1000+c*100
#         arr.append(tot)
# print(int(max(arr)))

# <5063>
# num = int(input())
# for i in range(num):
#     r, e, c = map(int, input().split())
#     e -= c
#     if(r > e):
#         print("do not advertise")
#     elif(r < e):
#         print("advertise")
#     else:
#         print("does not matter")

# <2935>
# a = int(input())
# op = str(input())
# b = int(input())
# if(op == "*"):
#     print(a*b)
# elif(op == "+"):
#     print(a+b)

# <10886>
# num = int(input())
# cnt = 0
# for i in range(num):
#     a = int(input())
#     if(a == 1):
#         cnt += 1
# if(num/2 < cnt):
#     print("Junhee is cute!")
# else:
#     print("Junhee is not cute!")

# <10214>
# num = int(input())
# Y = 0
# K = 0
# for _ in range(num):
#     for j in range(9):
#         a, b = map(int, input().split())
#         Y += a
#         K += b
#     if(Y > K):
#         print('Yonsei')
#     elif(Y < K):
#         print("Korea")
#     else:
#         print("Draw")


# <11721>
# num = input()
# while (len(num) != 0):
#     print(num[:10])
#     num = num[10:]

# <1264>
# vowel = ['a', 'e', 'i', 'o', 'u']
# while(True):
#     cnt = 0
#     string = input()
#     string = string.lower()
#     if(string == "#"):
#         break
#     for i in string:
#         if (i in vowel):
#             cnt += 1
#     print(cnt)

# <3058>
# n = int(input())
# for _ in range(n):
#     even = []
#     num_arr = map(int, input().strip().split())
#     for i in num_arr:
#         if(i%2 == 0):
#             even.append(i)
#     print(sum(even), min(even))

# <5054>
# c = int(input())
# for _ in range(c):
#     visit = int(input())
#     locate = list(map(int, input().split()))
#     print(2 * (max(locate) - min(locate)))

# <5635>
# n = int(input())
# arr = []
# for _ in range(n):
#     name, day, month, year = map(str, input().split())
#     day = int(day)
#     month = int(month)
#     year = int(year)
#     arr.append((year, month, day, name))
# arr.sort()
# print(arr[-1][3])
# print(arr[0][3])

# <10897>
# vowel = ['a', 'e', 'i', 'o', 'u']
# cnt = 0
# string = input()
# for i in string:
#     if (i in vowel):
#         cnt += 1
# print(cnt)

# <4458>   
# num = int(input()) 
# for _ in range(num):
#     string = input()
#     print(string[0].upper() + string[1:])

# <2822>
# arr = []
# sum = 0
# lst = []
# for i in range(1, 9):
#     num = int(input()) 
#     arr.append((num, i))  
# arr.sort(reverse=True)  #큰 값부터 정렬 
# for k in range(5):
#     sum += arr[k][0]
#     lst.append(arr[k][1])
# print(sum)
# lst.sort()
# for k in range(len(lst)):
#     print(lst[k], end=" ")

# <1427>
# num = input()
# arr = []
# for i in range(len(num)):
#     arr.append(num[i])
# arr.sort(reverse=True)
# for j in arr:
#     print(j, end="")

# <5800>
# k = int(input())
# for i in range(1, k+1):
#     arr = []
#     grade = list(map(int, input().strip().split()))
#     grade.remove(grade[0])
#     grade.sort()
#     for j in range(1, len(grade)):
#         arr.append(grade[j]-grade[j-1])
#     print("Class {}".format(i))
#     print("Max {}, Min {}, Largest gap {}".format(max(grade), min(grade), max(arr)))

# <2711>
# t = int(input())
# for i in range(t):
#     index, string = input().strip().split()
#     index = int(index)
#     print(string[:index-1], string[index:], sep="")

# <11170>
t = int(input())
for _ in range(t):
    cnt = 0
    n, m = map(int, input().split())
    for i in range(n, m+1):
        cnt += str(i).count('0')
    print(cnt)