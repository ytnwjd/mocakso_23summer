#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


typedef struct Node {
	int data;
	struct Node* link;
}Node;

typedef struct Linkedlist {
	Node* head;
}Linkedlist;


void init(Linkedlist* list);
void insert_Node(Linkedlist* list, int data);
void delete_Node(Linkedlist* list, int data);
void print_Linkedlist(Linkedlist* list);
bool search_Node(Linkedlist* list, int data);



int main() {

	Linkedlist linked_list;
	init(&linked_list);

	while (true)
	{
		int data;
		int choice;

		printf("1.Insert Node  \t2.Delete Node  \t3.Search Data  \t4.Print Linked List  \t5.Initialize  \t6.Exit\n");
		printf("Selection choice: ");
		scanf_s("%d", &choice);


		switch (choice)
		{
		case 1:	//Insert
			printf("삽입할 데이터를 알려주세요. > ");
			scanf("%d", &data);
			insert_Node(&linked_list, data);
			break;
		case 2:	//Delete
			printf("삭제할 데이터를 알려주세요. > ");
			scanf("%d", &data);
			delete_Node(&linked_list, data);
			break;
		case 3:	//Search
			printf("검색할 데이터를 알려주세요. > ");
			scanf("%d", &data);
			if (search_Node(&linked_list, data)) {
				printf("데이터 %d가 현재 list에 존재합니다.\n\n",data);
			}
			else {
				printf("데이터 %d가 현재 list에 존재하지 않습니다.\n\n",data);
			}
			break;
		case 4:	//Print
			printf("현재 list에 있는 데이터는 다음과 같습니다.\n");
			print_Linkedlist(&linked_list);
			break;
		case 5:	//Initialize
			init(&linked_list);
			printf("현재 list를 초기화 했습니다.\n\n");
			break;
		case 6:
			printf("프로그램을 종료하겠습니다.");
			return 0;
		}

	}
}




void init(Linkedlist* list) {
	list->head = NULL;
}

void insert_Node(Linkedlist* list, int data) {
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;
	newNode->link = NULL;

	if (list->head == NULL) {
		list->head = newNode;
		printf("데이터 \'%d\'을 삽입했습니다.\n\n", data);
		return;
	}

	Node* current = list->head;
	while (current->link != NULL) {
		current = current->link;
	}
	current->link = newNode;

	printf("데이터 \'%d\'을 삽입했습니다.\n\n", data);
}

void delete_Node(Linkedlist* list, int data) {
	if (list->head == NULL) {
		return;
	}

	if (list->head->data == data) {
		Node* tmp = list->head;
		list->head = list->head->link;
		printf("데이터 \'%d\'을 삭제했습니다.\n\n", data);
		free(tmp);
		return;
	}

	Node* curr = list->head;
	while (curr->link != NULL)
	{
		if (curr->link->data == data) {
			Node* tmp = curr->link;
			curr->link = curr->link->link;
			printf("데이터 \'%d\'을 삭제했습니다.\n\n", data);
			free(tmp);
			return;
		}
		curr = curr->link;
	}

	
}

void print_Linkedlist(Linkedlist* list) {
	Node* curr = list->head;
	while (curr != NULL) {
		printf("%d -> ", curr->data);
		curr = curr->link;
	}
	printf("NULL \n\n");
}

bool search_Node(Linkedlist* list, int data) {
	Node* curr = list->head;
	while (curr != NULL) {
		if (curr->data == data) {
			return true;
		}
		curr = curr->link;
	}
	return false;
}