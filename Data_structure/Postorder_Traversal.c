#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node {
  char data;
  struct node* left;
  struct node* right;
} Node;


void print_Postorder (Node *root) {
  if (root == NULL){
    return;
  }
  
  print_Postorder(root->left); // 왼쪽 서브트리로 재귀
  print_Postorder(root->right);  // 오른쪽 서브트리 재귀
  printf("%c ", root->data);  // root 출력
}