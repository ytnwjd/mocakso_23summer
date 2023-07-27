#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define _CRT_SECURE_NO_WARNINGS
#define MAX_STACK_SIZE 100

int stack[MAX_STACK_SIZE];
int top = -1;   // 스택이 비어있을 때 top의 기본 값

void push(int data);
void pop();
bool isEmpty();
bool isFull();



int main()
{
    int select;
    int data;

    while (true)
    {
        printf("원하는 연산을 고르세요.\n");
        printf("1.Push      2.Pop       3.Stack 확인       4.Exit\n");

        scanf_s("%d", &select);

        if (select == 1) {   // push
            printf("push할 정수형 데이터를 입력해주세요.\n>>> ");
            scanf_s("%d", &data);
            push(data);
        }
        else if (select == 2) {  // pop
            pop();
        }
        else if (select == 3) {  //확인
            if (isEmpty()) {
                printf("stack이 비어있습니다.\n");
            }
            else if (isFull()) {
                printf("stack이 꽉 찼습니다.\n");
            }
            else printf("Stack에 데이터가 있습니다.\n");

        }
        else if (select == 4) {  // exit
            printf("프로그램을 종료합니다.");
            return;
        }
        else {
            printf("유효하지 않은 선택입니다. 다시 선택해주세요.\n");

        }
    }

    return 0;
}



void push(int data) {
    if (isFull()) {
        printf("Stack이 꽉 찼습니다. 더 이상 push 할 수 없습니다!\n");
    }
    else {
        stack[++top] = data;
        printf("%d push에 성공했습니다!\n", data);
    }
}

void pop() {
    if (isEmpty()) {
        printf("Stack이 비어있습니다. pop 할 수 없습니다!\n");
    }
    else {
        int result = stack[top--];
        printf("pop 한 값은 \'%d\'입니다.", result);
    }
}

bool isEmpty() {
    if (top == -1) {
        return true;
    }
    else return false;
}

bool isFull() {
    if (top == -1) {
        return false;
    }
    else return true;
}