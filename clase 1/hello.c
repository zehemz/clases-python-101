#include <stdio.h>
#include <iostream>

void load();

void load(){
	const clock_t begin_time = clock();

	int i = 0;
	while(i< 1000000){
		i++;
	}
	
	std::cout << std::endl <<float( clock () - begin_time ) /  CLOCKS_PER_SEC<< std::endl;
}

int main(){
	load();
	return 0;
}
