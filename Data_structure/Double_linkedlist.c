#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


typedef struct Node {
	int data;
	struct Node* prev;
	struct Node* next;
}Node;

typedef struct Double_Linkedlist {
	Node* head;
}Double_Linkedlist;


void init(Double_Linkedlist* list);
void insert_Node(Double_Linkedlist* list, int data);
void delete_Node(Double_Linkedlist* list, int data);
void print_Linkedlist(Double_Linkedlist* list);
bool search_Node(Double_Linkedlist* list, int data);



int main() {

	Double_Linkedlist* linked_list;
	init(&linked_list);

	while (true)
	{
		int data;
		int choice;

		printf("1.Insert Node  \t2.Delete Node  \t3.Search Data  \t4.Print Double Linked List  \t5.Initialize  \t6.Exit\n");
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
				printf("데이터 %d가 현재 list에 존재합니다.\n\n", data);
			}
			else {
				printf("데이터 %d가 현재 list에 존재하지 않습니다.\n\n", data);
			}
			break;
		case 4:	//Print list
			printf("현재 list에 있는 데이터는 아래와 같습니다.\n");
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

void init(Double_Linkedlist* list) {
	list->head = NULL;
}

void insert_Node(Double_Linkedlist* list, int data) {
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;
	newNode->prev = NULL;
	newNode->next = NULL;

	if (list->head == NULL) {
		list->head = newNode;
		printf("데이터 \'%d\'을 삽입했습니다.\n\n", data);
		return;
	}

	Node* current = list->head;
	while (current->next != NULL) {
		current = current->next;
	}

	current->next = newNode;
	newNode->prev = current;
	printf("데이터 \'%d\'을 삽입했습니다.\n\n", data);
}

void delete_Node(Double_Linkedlist* list, int data) {
	Node* curr = list->head;
	while (curr != NULL)
	{
		if (curr->data == data) {
			if (curr->prev != NULL) {
				curr->prev->next = curr->next;
			}
			else {
				list->head = curr->next;
			}
			
			if (curr->next != NULL) {
				curr->prev->next = curr->prev;
			}
			
			printf("데이터 \'%d\'을 삭제했습니다.\n\n", data);
			free(curr);
			return;
		}
		curr = curr->next;
	}
}

void print_Linkedlist(Double_Linkedlist* list) {
	Node* curr = list->head;

	while (curr != NULL) {
		printf("%d -> ", curr->data);
		curr = curr->next;
	}
	printf("NULL \n\n");
}


bool search_Node(Double_Linkedlist* list, int data) {
	Node* curr = list->head;
	while (curr != NULL) {
		if (curr->data == data) {
			return true;
		}
		curr = curr->next;
	}
	return false;
}