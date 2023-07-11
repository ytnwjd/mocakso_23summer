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

# <10811>
