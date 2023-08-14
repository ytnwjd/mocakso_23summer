#include <stdio.h>

#define MAX_ELEMENT 200 // 힙 안에 저장된 요소의 수

typedef struct element {
    int key;
} element;

typedef struct HeapType {
    element heap[MAX_ELEMENT];
    int heap_size;
} HeapType;


void insert_max_heap(HeapType* h, element item) {
    int i;
    i = ++(h->heap_size); // 힙 크기 증가

    /* 트리를 거슬러 올라가면서 부모 노드와 비교하는 과정
        i가 루트 노트(index = 1)가 아니고, 삽입할 값(item)이 i의 부모 노드(index = i/2)보다 크면
        i번째 노드와 부모 노드를 교환하고, 한 레벨 위로 */
    while ((i != 1) && (item.key > h->heap[i / 2].key)) {
        //
        h->heap[i] = h->heap[i / 2];
        i /= 2;
    }

    // 새로운 노드 삽입
    h->heap[i] = item; 
}

element delete_max_heap(HeapType* h) {
    int parent, child;
    element item, temp;

    item = h->heap[1]; // 루트 노드 값을 반환하기 위해 item에 할당
    temp = h->heap[(h->heap_size)--]; // 마지막 노드를 temp에 할당하고 힙 크기 하나 감소
    parent = 1;
    child = 2;

    /* 현재 노드의 자식 노드 중 더 큰 자식 노드를 찾기
       (루트 노드의 왼쪽 자식 노드(index: 2)부터 비교 시작) */
    while (child <= h->heap_size) {
        if ((child < h->heap_size) && ((h->heap[child].key) < h->heap[child + 1].key)) {
            child++;
        }

        // 더 큰 자식 노드보다 마지막 노드가 크면, while문 중지
        if (temp.key >= h->heap[child].key) {
            break;
        }

        // 더 큰 자식 노드보다 마지막 노드가 작으면, 부모 노드와 더 큰 자식 노드를 교환
        h->heap[parent] = h->heap[child];

        // 한 단계 아래로 이동
        parent = child;
        child *= 2;
    }

    // 마지막 노드를 재구성한 위치에 삽입 후 최댓값(root) 반환
    h->heap[parent] = temp;
    return item;
}

void heap_sort(element a[], int n) {
    // 배열 : 9, 7, 6, 5, 4, 3, 2, 2, 1, 3
    int i;
    HeapType h;

    init(&h);

    for (i = 0; i < n; i++) {
        insert_max_heap(&h, a[i]);
    }

    for (i = (n - 1); i >= 0; i--) {
        a[i] = delete_max_heap(&h);
    }
}