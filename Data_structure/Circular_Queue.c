#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define _CRT_SECURE_NO_WARNINGS
#define MAX_QUEUE_SIZE 100

int Queue[MAX_QUEUE_SIZE];
int front = -1;
int rear = -1;

void enQueue(int data);
void deQueue();
bool isEmpty();
bool isFull();



int main()
{
    int select;
    int data;

    while (true)
    {
        printf("원하는 연산을 고르세요.\n");
        printf("1.Insert      2.Delete       3.Queue 확인       4.Exit\n");

        scanf_s("%d", &select);

        if (select == 1) {   // insert
            printf("Insert할 정수형 데이터를 입력해주세요.\n>>> ");
            scanf_s("%d", &data);
            enQueue(data);
        }
        else if (select == 2) {  // Delete
            deQueue();
        }
        else if (select == 3) {  //확인
            if (isEmpty()) {
                printf("Queue가 비어있습니다.\n");
            }
            else if (isFull()) {
                printf("Queue가 꽉 찼습니다.\n");
            }
            else printf("Queue에 데이터가 있습니다.\n");

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



void enQueue(int data) {
    if (isFull()) {
        printf("Queue가 꽉 찼습니다. 더 이상 Insert 할 수 없습니다.\n");
    }
    else {
        rear = (rear + 1) % MAX_QUEUE_SIZE;
        Queue[rear] = data;
        printf("\'%d\' Insert에 성공했습니다!\n", data);
    }
}

void deQueue() {
    if (isEmpty()) {
        printf("Queue가 비어있습니다. delete 할 수 없습니다.\n");
    }
    else {
        front = (front + 1) % MAX_QUEUE_SIZE;
        int result = Queue[front];
        printf("Delete 한 값은 \'%d\'입니다.", result);
    }
}

bool isEmpty() {
    if (front == rear) {
        return true;
    }
    else return false;
}

bool isFull() {
    int chk;
    chk = (rear + 1) % MAX_QUEUE_SIZE;

    if (front == chk) {
        return true;
    }
    else return false;
}