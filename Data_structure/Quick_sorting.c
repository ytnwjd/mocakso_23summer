#include <stdio.h>

#define MAX_SIZE 9
#define SWAP(x, y, temp) ( (temp)=(x), (x)=(y), (y)=(temp) )

/* pivot을 기준으로 2개의 부분 리스트로 나누고
   pivot보다 작은 값은 왼쪽, 큰 값은 오른쪽 부분 리스트로 옮긴다.*/
int partition(int list[], int left, int right) {
    int pivot, temp;
    int low, high;

    low = left;
    high = right + 1;
    pivot = list[left]; // 임의의 값을 피벗으로 선택

    /* low와 high가 교차할 때까지 반복(low < high) */
    do {
        // list[low]가 피벗보다 작으면 계속 low를 증가 //
        do {
            // left+1 에서 low 시작
            low++; 
        } while (low <= right && list[low] < pivot);

        /* list[high]가 피벗보다 크면 계속 high를 감소 */
        do {
            high--; 
        } while (high >= left && list[high] > pivot);

        // 만약 low와 high가 교차하지 않았으면 list[low]를 list[high] 교환
        if (low < high) {
            SWAP(list[low], list[high], temp);
        }
    } while (low < high);

    /* low와 high가 교차했으면 반복문을 나와서
       list[left]와 list[high]를 교환 후 pivot 반환 */
    SWAP(list[left], list[high], temp);

    return high;
}

void quick_sort(int list[], int left, int right) {

    // 리스트의 크기가 0이나 1이 아니면 //
    if (left < right) {
        // pivot을 기준으로 비균등 분할
        int q = partition(list, left, right); 

        // 피벗은 제외한 2개의 부분 리스트를 대상으로 순환 호출
        quick_sort(list, left, q - 1); // 앞쪽 부분 리스트 정렬
        quick_sort(list, q + 1, right); // 뒤쪽 부분 리스트 정렬
    }

}