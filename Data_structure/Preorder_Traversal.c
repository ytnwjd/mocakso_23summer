#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node {
  char data;
  struct node* left;
  struct node* right;
} Node;

void print_Preorder (Node* root) {
    if (root == NULL) {
        return;
    }
    
    printf("%c ", root->data);  // root 출력
    print_Preorder(root->left); // 왼쪽 서브트리 재귀
    print_Preorder(root->right);    // 오른쪽 서브트리 재귀
}