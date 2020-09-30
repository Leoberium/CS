all:
	gcc solution.c -fPIC -ldl '-Wl,-rpath=.' -o solution

lib:
	gcc -shared intfunc.c -fPIC -o libFunc.so

clean:
	rm solution libFunc.so 2>/dev/null
