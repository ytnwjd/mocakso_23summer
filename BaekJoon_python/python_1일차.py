## 단계별 문제풀이

# <1단계-입출력>
# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

# name = input()
# print(name+"??!")

# date = int(input())
# print(date-543)

# A, B, C = map(int, input().split())
# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C)*(B%C))%C)

# num1 = int(input())
# num2 = int(input())
# num2_1 = (num2%100)%10
# num2_10 = (num2%100)//10
# num2_100 = num2//100
# print(num1*num2_1)
# print(num1*num2_10)
# print(num1*num2_100)
# print((num1*num2_1)+(num1*num2_10)*10+(num1*num2_100)*100)

# a, b, c = map(int, input().split())
# print(a+b+c)

# print("\\    /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \(__)|")

# print("|\_/|")
# print("|q p|   /}")
# print("( 0 )\"\"\"\\")
# print("|\"^\"\`   |")
# print("||_/=\\\\__|")


# <2단계-조건문>
# a, b = map(int, input().split())
# if(a > b):
#     print(">")
# elif(a == b):
#     print("==")
# else:
#     print("<")

# score = int(input())
# if(90<=score<=100):
#     print("A")
# elif(80<=score<=89):
#     print("B")
# elif(70<=score<=79):
#     print("C")
# elif(60<=score<=69):
#     print("D")
# else:
#     print("F")

# year = int(input())
# if((year%400)==0):
#     print("1")
# elif((year%4 == 0) and (year%100)!=0):
#     print("1")
# else:
#     print("0")

# x = int(input())
# y = int(input())
# if(x>0 and y>0):
#     print("1")
# elif(x>0 and y<0):
#     print("4")
# elif(x<0 and y>0):
#     print("2")
# else:
#     print("3")

# Hour, Minute = map(int, input().split())
# if (Minute < 45):
#     Minute_1 = 45-Minute
#     if (Hour == 0):
#         print("23", 60-Minute_1)
#     else:
#         print(Hour-1, 60-Minute_1)
# else:
#     print(Hour, Minute-45)

# H, M = map(int, input().split())
# Time = int(input())
# H += Time//60
# M += Time%60
# if(M>=60):
#     H += 1
#     M -= 60
# if(H>=24):
#     H -= 24
# print(H, M)

A, B, C = map(int, input().split())
if(A==B and A==C and B==C):
    print(10000+A*1000)
elif(A!=B and A!=C and B!=C):
    if(A>=B and A>=C):
        max = A
    elif(B>=A and B>=C):
        max = B
    else:
        max = C
    print(max*100)
else:
    if(A==B):
        print(1000+A*100)
    elif(B==C):
        print(1000+B*100)
    elif(A==C):
        print(1000+C*100)