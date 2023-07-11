## 단계별 문제풀이

# <4단계-1차원 배열>
# <10810>
# a, b = map(int, input().split())
# cnt_array =[0]*a
# for _ in range(b):
#     i, j, k = map(int, input().split())
#     for ball in range(i,j+1):
#         cnt_array[ball-1] = k
# for a in range(a):
#     print(cnt_array[a], end=' ')

# <10813>    
# n, m = map(int, input().split())
# tmp = 0
# array = [0]*n
# for ball in range(n):
#     array[ball] = ball+1
# for _ in range(m):
#     i, j = map(int, input().split())
#     tmp = array[i-1]
#     array[i-1] = array[j-1]
#     array[j-1] = tmp
# for ball in range(n):
#     print(array[ball], end=' ')

# <5597>
# attend = list(range(1, 31))
# for _ in range(28):
#     num = int(input())
#     attend.remove(num)
# attend.sort()
# for i in attend:
#     print(i)

# <3053>
# num_arr = [ ]
# div_arr = [ ]
# for i in range(10):
#     n = int(input())
#     if(n in num_arr):
#         continue
#     else:
#         num_arr.append(n)
# for j in range(len(num_arr)):
#     num = num_arr[j] % 42
#     if(num in div_arr):
#         continue
#     else:
#         div_arr.append(num)
# print(len(div_arr))

# <10811>
# n, m = map(int, input().split())
# basket = [ ]
# for i in range(n):
#     basket.append(i+1)
# for _ in range(m):
#     i, j = map(int, input().split())
#     tmp = basket[i-1:j]
#     tmp.reverse()
#     basket[i-1:j] = tmp
# for id in range(n):
#     print(basket[id], end=' ')

# <5단계-문자열>
# <27866>
# word = input()
# index = int(input())
# print(word[index-1])

# <2743>
# word = input()
# print(len(word))

# <9086>
# c = int(input())
# for i in range(c):
#     word = input()
#     leng = len(word)
#     print(word[0] + word[leng-1])

# <11654>
# ascc = input()
# print(ord(ascc))

# <11720>
# c = int(input())
# sum = 0
# num = input()
# for i in range(c):
#     n = int(num[i])
#     sum += n
# print(sum)

# <10809>
# word = input()
# alpha = [-1]*26
# for i in word:
#     alpha[ord(i)-97] = word.index(i)
# for i in alpha:
#     print(i, end=' ')

# <2675>
# c = int(input())
# for _ in range(c):
#     r, s = map(str, input().split())
#     r = int(r)
#     for i in range(0, len(s)):
#         print(s[i]*r, end='')
#     print()

# <1152>
# inputString = input().split()
# print(len(inputString))

# <2908>
# a, b = map(str, input(). split())
# a = int(a[::-1])
# b = int(b[::-1])
# if(a > b):
#     print(a)
# else:
#     print(b)

# <5622>
# alphbat_list = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
# input = list(input())
# time = 0
# for alphabat in input:
#     for word in alphbat_list:
#         if(alphabat in word):
#             time += (alphbat_list.index(word) + 3)
# print(time)

# <11718>
while(True):
    try: 
        string = input()
        print(string)
    except:
        break
