## 그냥 문제풀이 ..

# <2558>
# a = int(input())
# b = int(input())
# print(a+b)

# <2163>
# n, m = map(int, input().split())
# print(n*m-1)

# <3046>
# a, s = map(int, input().split())
# print(s*2-a)

# <10833>
# num = int(input())
# result = 0
# for i in range(num):
#     a, b = map(int, input().split())
#     result += b%a
# print(result)

# <2742>
# num = int(input())
# for i in range(num, 0, -1):
#     print(i)

# <10757>
# a, b = map(int, input().split())
# print(a+b)

# <2754>
# num = input()
# if("A" in num):
#     if(num == "A0"):
#         print(4.0)
#     elif(num == "A-"):
#         print(3.7)
#     else:
#         print(4.3)
# elif("B" in num):
#     if(num == "B0"):
#         print(3.0)
#     elif(num == "B-"):
#         print(2.7)
#     else:
#         print(3.3)
# elif("C" in num):
#     if(num == "C0"):
#         print(2.0)
#     elif(num == "C-"):
#         print(1.7)
#     else:
#         print(2.3)
# elif("D" in num):
#     if(num == "D0"):
#         print(1.0)
#     elif(num == "D-"):
#         print(0.7)
#     else:
#         print(1.3)
# else:
#     print(0.0)

# <7287>
# print("82")
# print("ysjsw")

# <4101>
# while True:
#     a, b = map(int, input().split())
#     if(a==0 and b==0):
#         break
#     if(a>b):
#         print("Yes")
#     else:
#         print("No")

# <1789>
# s = int(input())
# cnt = 0
# n = 0
# while True:
#     cnt += 1
#     n += cnt
#     if(n > s):
#         cnt -= 1
#         break
#     if(n==s):
#         break
# print(cnt)

# <2576>
# sum = 0
# odd = []
# for i in range(7):
#     num = int(input())
#     if (num%2 == 0):
#         continue
#     else:
#         odd.append(num)
# if(len(odd) == 0):
#     print(-1)
# else:
#     for j in odd:
#         sum += j
#     print(sum)
#     print(min(odd))

# <2490>
# for _ in range(3):
#     arr = list(map(int, input().split()))
#     a = arr.count(0)
#     if (a==0):
#         print("E")
#     elif (a==1):
#         print("A")
#     elif (a==2):
#         print("B")
#     elif (a==3):
#         print("C")
#     else:
#         print("D")

# <2443>
# cnt = int(input())
# for i in range(cnt, 0, -1):
#     print(" "*(cnt-i) + "*"*(2*i-1))

# <2741>
# num = int(input())
# for i in range(num):
#     print(i+1)

# <2522>
# num = int(input())
# for i in range(1, num+1):
#     print(" "*(num-i) + "*"*(i))
# for i in range(num-1, 0, -1):
#     print(" "*(num-i) + "*"*(i))

# <2941>
# word = input()
# alphabat = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# for i in alphabat:
#      word = word.replace(i, '*')
# print(len(word))

# <25206>
# rating = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
# score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
# sum = 0.0
# cnt = 0
# for i in range(20):
#     subject, s, grade = input().split()
#     s = float(s)
#     if (grade != "P"):
#         cnt += s
#         sum += (s*score[rating.index(grade)])
# print('%.6f' % (sum/cnt))

# <2563>


# <5635>
# num = int(input())
# for i in range(num):
#     name, d, m, y = input().split()

