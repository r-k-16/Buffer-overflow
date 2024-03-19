#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int bowfunc(char *string){
	char buffer[1024];
	strcpy(buffer, string);
	return 1;
}

int main(int argc, char *argv[]){
	bowfunc(argv[1]);
	printf("Done.\n");
	return 1;
}
