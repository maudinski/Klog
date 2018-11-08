#include <stdio.h>
#include <ncurses.h>
#include <stdlib.h>

void main() {

	FILE *out;

	if ((out = fopen("out.txt", "r+")) == NULL) {
		printf("Failed opening file\n");
		exit(1);
	}

	char c = '\n';
	while (c != '0') {
		// there's ways around having to use the screen
		initscr();
		c = getch();
		// backspaces arent represented in ascii, will have to do that ourselves
		// other special characters too
		// maybe with backspace just take a character for the file? not sure
		// also, dont need to pop up that screen
		// also, maybe  buffer up some characters then to print out
		// a string
		fprintf(out, "%c", c);

	}
	fclose(out);

	endwin();

}
