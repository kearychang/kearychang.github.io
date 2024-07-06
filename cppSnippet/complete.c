#include <trie.c>

int main(void) {
	int i;
	char string[25];
	char_arr2D C;
	FILE *f = fopen("/american-english-no-accents.txt", "r");
	Trie *T = trie_initialize();
	if (f == NULL) {
		printf("error\n");
	}

	//read .txt file into trie
	while ((string = fgets(C, 25, f)) != NULL) {

		//delete newlines from string array
		if (strlen(string) > 0 && string[strlen(string) - 1] == '\n') {
			string[strlen(string) - 1] = '\0';
		}
		trie_insert(T, string);
	}
	while (1) {
		printf("Enter String: ");
		string = fgets(C, 25, stdin);

		//delete newlines from string array
		if (strlen(string) > 0 && string[strlen(string) - 1] == '\n') {
			string[strlen(string) - 1] = '\0';
		}

		//search trie for string matching stdin and iterate through them
		C = trie_search(T, string);
		for (i = 0; i < char_arr2D_size(C); i++) {
			printf("%s\n", *(C + i));
		}
		char_arr2D_free(C);
	}
	return 0;
}
