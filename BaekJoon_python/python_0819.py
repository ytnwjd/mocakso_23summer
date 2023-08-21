# 문제 풀이
# <1292>
# a, b = map(int, input().split())
# arr = [0]
# sum = 0
# for i in range(1, b+1):
#     for j in range(i):
#         arr.append(i)
# for k in range(a, b+1):
#     sum += arr[k]    
# print(sum)

# <5218>
# dic = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 
#        'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}
# num = int(input())
# for i in range(num):
#     str1, str2 = map(str, input().split())
#     print('Distances:', end=' ')
#     for j in range(len(str1)):
#         if dic[str1[j]] <= dic[str2[j]]:
#             print(dic[str2[j]]-dic[str1[j]], end=" ")
#         else:
#             print(26-(dic[str1[j]]-dic[str2[j]]), end=" ")
#     print()

# <1357>
# a, b = map(str, input().split())
# rev_a = int(a[::-1])
# rev_b = int(b[::-1])
# ab = rev_a+rev_b
# ab = str(ab)
# ab = ab[::-1]
# print(int(ab))

# <2587>
# arr = []
# for _ in range(5):
#     num = int(input())
#     arr.append(num)
#     arr = sorted(arr)
# print(int(sum(arr)/5))
# print(int(arr[int(len(arr)/2)]))

# <9076>
# num = int(input())
# m = 0
# n = 0
# for i in range(num):
#     arr = list(map(int, input().split()))
#     arr = sorted(arr)
#     arr.remove(arr[0])
#     arr.remove(arr[-1])
#     if (arr[-1]-arr[0] >= 4):
#         print("KIN")
#     else:
#         print(sum(arr))

# <4999>
# a = input()
# b = input()
# if (len(a) >= len(b)):
#     print("go")
# else:
#     print("no")

# <11948>
# arr = []
# arr2 = []
# tot = 0
# for _ in range(4):
#     gra = int(input())
#     arr.append(gra)
#     arr.sort()
# arr.remove(arr[0])
# tot = sum(arr)
# for _ in range(2):
#     gra = int(input())
#     arr2.append(gra)
# tot += max(arr2)
# print(tot)

# <5691>
# while True:
#     a, b = map(int, input().split())
#     if a==0 and b==0:
#         break
#     else:
#         print(a-(b-a))

# <11966>
