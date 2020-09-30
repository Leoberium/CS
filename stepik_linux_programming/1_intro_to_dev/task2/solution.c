#include <stddef.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <dlfcn.h>

int (*func)(int);

bool init_library(char * lib_name, char * func_name) {
	void *hdl = dlopen(lib_name, RTLD_LAZY);
	if ( hdl == NULL )
		return false;
	
	func = (int (*)(int))dlsym(hdl, func_name);

	if ( func == NULL )
		return false;

	return true;
}

int main(int argc, char * argv[]) {
	if ( init_library(argv[1], argv[2]) )
		printf("%d\n", func(atoi(argv[3])));
	else
		printf("Library was not found\n");
	return 0;
}
