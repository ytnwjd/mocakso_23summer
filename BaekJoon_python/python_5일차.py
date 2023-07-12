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
input = list(input().lower())
alphabat = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
cnt = [ ]
for i in alphabat:
    w = input.count(i)
    cnt.append(w)
if (cnt.count(max(cnt)) >= 2):
    print("?")
if (cnt.count(max(cnt)) == 1):
    w = alphabat[cnt.index(max(cnt))]
    print(w.upper())