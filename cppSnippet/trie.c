#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "trie.h"

//========================================TRIE NODE========================================
/*
The task is write a program (implementing a Trie ADT) that reads strings from stdin and traverses it, autocompleting the string.

Input:
The program should read strings one per line, from stdin. 
A string will contain only letters of the alphabet in any case ([A-Za-z]).

Output:
The program should print out on stdout, all of the autocomplete word matches. Word matches are displayed in
ascending alphabetical order. It should be CASE SENSITIVE and it can assume that all strings entered are to be matched
in the case given.

Dictionary:
The dictionary is given in the format:
-1 word per line
-each word starts in column 1
-words are in alphabetical order
-each word contains only letters of the alphabet in any case ([A-Za-z]), and possibly one apostrophe
-no word is longer than 24 characters, including apostrophe

Example Runs:
>program
Enter String: de <--- I typed "de" on stdin
deer
deposit
desk

Implementation:
Code must be written in Ansi-C and must implement a Trie ADT. It should not use system calls.
It is recommended that you implement operations insert(), search() and traverse().
*/
TrieNode *trienode_initialize(char c, int end, int height) {
	TrieNode *t;
	t = (TrieNode *) malloc(sizeof(TrieNode *));

	//if t is assigned memory space and value is NULL, print error message
	if (t != NULL) {
		t->c = c;
		t->end = end;
		t->height = height;
		t->child = NULL;
		t->sibling = NULL;
	} else {
		printf("out of memory\n");
	}
	return t;
}

TrieNode *getSibling(TrieNode *t) {
	return t->sibling;
}

TrieNode *getChild(TrieNode *t) {
	return t->child;
}

TrieNode *trienode_search(TrieNode *t, char c) {
	TrieNode *tmp_t;
	tmp_t = t;

	//if given empty node argument, return it
	if (tmp_t != NULL) {

		while (tmp_t != 0) {
			if (tmp_t->c == c) {
				break;
			}
			tmp_t = getSibling(t);
		}
	}
	return tmp_t;
}

//========================================TRIE========================================
Trie *trie_initialize(void) {
	Trie *T;
	T = (Trie *) malloc(sizeof(Trie *));

	//if T is assigned memory space and value is NULL, print error message
	if (T != NULL) {
		//initialize max_length to longest string in trie
		T->max_length = 0;

		//initialize root trie node to value outside dictionary
		T->root = trienode_initialize('\0', -1, 0);
	} else {
		printf("out of memory\n");
	}
	return T;
}

int trie_insert(Trie *T, char *c) {
	int i = 0;
	int fail = 0;
	TrieNode *t;
	TrieNode *t_parent = T->root;
	TrieNode *t_parent_child = getChild(t_parent);

	for (i = 0; i < strlen(c); i++) {

		//search for trie node t among the siblings of t_parent_child with matching char *(c+j)
		if ((t = trienode_search(t_parent_child, *(c + i))) != NULL) {

			//set node t as a terminated node if (i == strlen(c))
			if (i == strlen(c)) {
				t->end = 1;
			}
		} else {

			//create trie node t if it doesnt exist
			//t has value t->c = *(c+j) and t->end = (i == strlen(c))
			t = trienode_initialize(*(c + i), i == strlen(c), i + 1);

			//t is a child if t_parent_child is NULL
			//t is a sibling if t_parent_child is not NULL
			if (t_parent_child != NULL) {

				//assign t as sibling of a trie node that currently has no siblings
				while ((t_parent_child = getSibling(t_parent_child)) != NULL) {
				}
				t_parent_child->sibling = t;
			} else {

				//assign t as child of t_parent
				t_parent->child = t;
			}
		}

		//move t_parent and t_parent_child down a level in trie
		t_parent = t;
		t_parent_child = getChild(t);

		//if t is NULL after assignment, print error message
		if (t == NULL) {
			printf("out of memory\n");
			return 0;
		}
	}

	//assign T->max_length if inserted string is longest string in trie
	if (i > T->max_length) {
		T->max_length = i;
	}
	return 1;
}

char_arr2D *trie_search(Trie *T, char *c) {
	int i = 0;
	int count = strlen(c) - 1;
	char string[T->max_length];
	TrieNode *t = getChild(T.root);
	char_arr2D *C = char_arr_2D_initialize();
	Stack S = stack_initialize();

	strncpy(string, c);

	//assign t to trie node with matching last character in string
	for (i = 0; i < strlen(c); i++) {

		//search trie node t's siblings for matching character *(c + i)
		//return if not found
		if ((t = trienode_search(t, *(c + i))) == NULL) {
			return C;
		}

		//move trie node t down a level to continue search if (i < strlen(c))
		if (i < strlen(c)) {
			t = getChild(t);
		}
	}

	//add input string to dynamic string array match if it is a word in trie
	if (t->end == 1) {
		char_arr2D_strncpy(C, c);
	}

	//use a stack to iterate through trie
	t = getChild(t);
	do {
		if (t != NULL) {
			push(S, t);
			t = getSibling(t);
			string[count + t->height] = t->c;
		} else {
			t = pop(S);
			string[count + t->height] = t->c;

			//when element is popped, check if it is an ending char
			//add it to 2D char array C
			if (t->end == 1) {
				string[count + t->height + 1] = '\0';
				char_arr2D_strncpy(C, string);
			}
		}
	} while (!isEmpty(S));

	free(S);
	return C;
}

//========================================STACK========================================
Stack *stack_initialize(int MAX_SIZE) {
	Stack *S;
	S = (Stack *) malloc( sizeof(Stack *));
	S->count = 0;
	S->MAX_SIZE = MAX_SIZE;
	S->item = (TrieNode **) malloc( S->MAX_SIZE * sizeof(TrieNode **));
	if (S == NULL || S->item == NULL) {
		printf("out of memory\n");
	}
	return S;
}

TrieNode *pop(Stack *S) {
	TrieNode *t;
	if (S->count <= 0) {
		printf("stack underflow\n");
	} else {
		S->count--;
		t = S->item[S->count];
		if (t == NULL) {
			printf("out of memory\n");
		}
	}
	return t;
}

void push(Stack *S, TrieNode *t) {
	if (S->count >= S->MAX_SIZE) {
		printf("stack overflow\n");
	} else if (t != NULL) {
		S->item[S->count] = t;
		S->count++;
	}
}

int isEmpty(Stack *S) {
	return S->count > 0;
}

void stack_free(Stack *S) {
	free(S->item);
	free(S);
}

//========================================char_arr_2D========================================
char_arr2D *char_arr2D_initialize() {
	char_arr2D *C;
	C = (char_arr2D *) malloc( sizeof(char_arr2D *));
	C->c = (char **) malloc( sizeof(char **));
	if (C == NULL) {
		printf("out of memory\n");
	} else {
		C->size = 0;
	}
	return C;
}

void char_arr2D_strcpy(char_arr2D *C, char *c) {
	C->size++;
	C->c = (char **) realloc( C->c, C->size * sizeof(char **));
	strcpy(*(C->c + C->size), c);
}

int char_arr2D_size(char_arr2D *C) {
	return C->size;
}

void char_arr2D_free(char_arr2D *C) {
	free(C->c);
	free(C);
}
