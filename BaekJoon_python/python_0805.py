# 그냥 문제풀이
# <5554>
# sum = 0
# for i in range(4):
#     time = int(input())
#     sum += time
# print(int(sum/60))
# print(sum%60)

# <2744>
# word = list(map(str, input()))
# for i in range(0, len(word)):
#     if(word[i].isupper()):
#         word[i] = word[i].lower()
#     elif(word[i].islower()):
#         word[i] = word[i].upper()
# for i in word:
#     print(i, end="")

# <2752>
# num_list = list(map(int, input().split()))
# num_list.sort()
# for i in num_list:
#     print(i, end=" ")

# <5543>
# buger = 2001
# drink = 2001
# for _ in range(3):
#     a = int(input())
#     if (a <= buger):
#         buger = a
# for _ in range(2):
#     a = int(input())
#     if (a <= drink):
#         drink = a
# print(buger+drink-50)

# <10808>
# alphabat = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# arr = []
# word = map(str, input())
# for i in range(26):
#     arr.append(0)
# for i in word:
#     if(i in alphabat):
#         arr[alphabat.index(i)] += 1
# for j in arr:
#     print(j, end=" ")

# <11365>
# while True:
#     line = str(input())
#     if (line == "END"):
#         break
#     else:
#         print(line[::-1])

# <10821>
# num = list(map(str, input().split(",")))
# print(len(num))
    
# <2592>
# import statistics as static
# ave = 0
# arr = []
# for i in range(10):
#     num = int(input())
#     ave += num
#     arr.append(num)
# print(int(ave/10))
# print(static.mode(arr))

# <10953>
# t = int(input())
# for i in range(t):
#     a, b = map(int, input().split(","))
#     print(a+b)

# <2460>
# p = 0
# arr = []
# for i in range(1, 11):
#     a, b = map(int, input().split())
#     p += b
#     p -= a
#     arr.append(p)
# print(max(arr))

# <2953>
# arr = []
# for i in range(5):
#     grade = 0
#     num = input().split()
#     for j in num:
#         grade += int(j)
#     arr.append(grade)
# m = max(arr)
# print(arr.index(m)+1, m)

# <11659>
# import sys as sys
# n, m = map(int, sys.stdin.readline().split())
# num = list(map(int, sys.stdin.readline().split()))
# p = [0]
# for i in range(n):
#     p.append(num[i]+p[i])
# for _ in range(m):
#     i, j = map(int, sys.stdin.readline().split())
#     print(p[j]-p[i-1])

# <2577>
# arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# a = int(input()); b = int(input()); c = int(input())
# num = a*b*c
# num = str(num)
# for i in num:
#     i = int(i)
#     arr[i] = arr[i]+1
# for j in arr:
#     print(j)

# <4344>
# c = int(input())
# for _ in range(c):
#     arr = list(map(int, input().split()))
#     ave = 0
#     cnt = 0
#     result = 0
#     num = arr[0]
#     for j in range(num):
#         ave += arr[j+1]
#     ave = (ave/num)
#     for k in range(num):
#         if (arr[k+1] > ave):
#             cnt += 1
#     result = (cnt/num) *100
#     print("%.3f" % (result)+ "%")