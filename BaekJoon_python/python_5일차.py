## 단계별 문제풀이

# <6단계-심화1>
# <25083>
# print("         ,r\'\"7")
# print("r`-_   ,\'  ,/")
# print(" \\. \". L_r\'")
# print("   `~\\/")
# print("      |")
# print("      |")

# <3003>
# king, queen, rook, bishop, knight, pawn
# piece = list(map(int, input().split()))
# cnt_array = [1, 1, 2, 2, 2, 8]
# for i in range(len(piece)):
#         piece[i] = (cnt_array[i]- piece[i])
# for i in range(len(piece)):
#     print(piece[i], end=' ')

# <2444>
# num = int(input())
# for i in range(1, num+1):
#     print(" "*(num-i) + "*"*(2*i-1))
# for i in range(num-1, 0, -1):
#     print(" "*(num-i) + "*"*(2*i-1))

# <10988>
# word = input()
# if(word == word[::-1]):
#     print(1)
# else:
#     print(0)

# <1157>
# input = list(input().lower())
# alphabat = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# cnt = [ ]
# for i in alphabat:
#     w = input.count(i)
#     cnt.append(w)
# if (cnt.count(max(cnt)) >= 2):
#     print("?")
# if (cnt.count(max(cnt)) == 1):
#     w = alphabat[cnt.index(max(cnt))]
#     print(w.upper())

# <7단계-2차원 배열>
# <2738>
# n, m = map(int, input().split())
# A = [] ;   B = [] ;  sum = []
# for i in range(n):
#     A.append([])
#     B.append([])
#     sum.append([])
#     for _ in range(m):
#         A[i].append(0)
#         B[i].append(0)
#         sum[i].append(0)
# for i in range(n):
#     num = list(map(int, input().split()))
#     for j in range(m):
#         A[i][j] = num[j]
# for i in range(n):
#     num = list(map(int, input().split()))
#     for j in range(m):
#         B[i][j] = num[j]
# for i in range(n):
#     for j in range(m):
#         sum[i][j] = (A[i][j] + B[i][j])
# for i in range(n):
#     for j in range(m):
#         print(sum[i][j], end=" ")
#     print()

# <2566>
# array = []
# max = 0
# x = 0 ; y = 0
# for _ in range(9):
#     array.append(list(map(int, input().split())))
# for i in range(9):
#     for j in range(9):
#         if(array[i][j] >= max):
#             max = array[i][j]
#             x = (i+1)
#             y = (j+1)
# print(max)
# print(x, y)

# <10798>
words = [ ]
length = [ ]
result = ""
for _ in range(5):
    word = input()
    words.append(word)
    length.append(len(word))
for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            result += words[j][i]
print(result)