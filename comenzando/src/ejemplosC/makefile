all: main
clean:
	rm -f -r ./build/*.o
	rm -f -r ./build/*.so
	rm -f -r ./build/hello

main: helloLib.o cmasmas
		gcc -shared ./build/helloLib.o -o ./build/helloLib.so

helloLib.o:
		gcc -c -fPIC helloLib.c -o ./build/helloLib.o

cmasmas: 		
		g++ -g -Wall -o ./build/hello hello.cpp