## 단계별 문제풀이

# <7단계-일반 수학>
# <2745>
# n, b = map(str, input().split())
# b = int(b)
# alphabat = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# num = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# result = 0
# for i in range(len(n)):
#     if(n[i] in alphabat):
#         result += (pow(b,i)*num[alphabat.index(n[i])])
#     else:
#         result += pow(b,i)*n[i]
# print(int(result))

# a, b = input().rstrip().split()
# print(int(a, int(b)))

# <11005>
