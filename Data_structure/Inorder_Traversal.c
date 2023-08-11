#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node {
  char data;
  struct node* left;
  struct node* right;
} Node;

void print_Inorder (Node* root) {
  if (root == NULL){
    return;
  }

  print_Inorder(root->left); // 왼쪽 서브트리로 재귀
  printf("%c ", root->data);  // root 출력
  print_Inorder(root->right);  // 오른쪽 서브트리로 재귀
}