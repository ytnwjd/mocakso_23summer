#include <stdio.h>

void insertion_sorting(int list[], int n) {
	int i, j;
	int key;

	for (i = 0; i < n; i++) {
		key = list[i];

		/*i - 1번째부터 역순으로 크기 조사
			-> 현재 i-1번째까지 정렬되어 있기 때문 */ 
		for (j = i - 1; j > 0 && list[j] > key; j--) {
			list[j + 1] = list[j];
		}

		list[j + 1] = key;
	}
}