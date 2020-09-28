#include <stdio.h>
#include <stdlib.h>

unsigned long sum_of_primes(unsigned a[], unsigned size) {
	unsigned long s = 0LU; // sum
	unsigned i = 0U, j = 0U; // index
	// initializing the array 
	for (i = 0U; i < size; i++) a[i] = i + 2U;
	// filtering the array
	for (i = 0U; i < size; i++) {
		if (a[i] == 0U) continue;
		for (j = i + a[i]; j < size; j += a[i]) {
			a[j] = 0U;
		}
	}
	// summing up
	for (i = 0U; i < size; i++) s += a[i];
	return s;
}

int main(void) {
	unsigned n = 0;
	scanf("%d", &n);
	unsigned *a = calloc(n - 1U, sizeof *a);
	printf("%lu \n", sum_of_primes(a, n - 1U));
	return 0;
}
