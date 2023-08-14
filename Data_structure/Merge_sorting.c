#include <stdio.h>

#define MAX_SIZE 8
int sorted[MAX_SIZE];	// 여분의 배열

// 2개의 인접한 배열 합병
void merge(int list[], int left, int mid, int right) {
    int i, j, k, l;

    i = left;   // i: 정렬된 왼쪽 리스트에 대한 인덱스
    j = mid + 1;    // j: 정렬된 오른쪽 리스트에 대한 인덱스
    k = left;   // k: 정렬될 리스트에 대한 인덱스

    /* 분할 정렬된 list의 합병 */
    while (i <= mid && j <= right) {
        if (list[i] <= list[j])
            sorted[k++] = list[i++];
        else
            sorted[k++] = list[j++];
    }

    // 남아 있는 값들을 일괄 복사
    if (i > mid) {
        for (l = j; l <= right; l++)
            sorted[k++] = list[l];
    }
    // 남아 있는 값들을 일괄 복사
    else {
        for (l = i; l <= mid; l++)
            sorted[k++] = list[l];
    }

    // 배열 sorted[](임시 배열)의 리스트를 배열 list[]로 재복사
    for (l = left; l <= right; l++) {
        list[l] = sorted[l];
    }
}


void merge_sort(int list[], int left, int right) {
    int mid;

    if (left < right) {
        mid = (left + right) / 2;   // 리스트 균등 분할
        merge_sort(list, left, mid); // 앞쪽 부분 리스트 정렬
        merge_sort(list, mid + 1, right);   // 뒤쪽 부분 리스트 정렬
        merge(list, left, mid, right);  // 합병
    }
}