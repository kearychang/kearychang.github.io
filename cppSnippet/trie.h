typedef struct {
	char c;
	int end;
	int height;
	TrieNode *sibling;
	TrieNode *child;
} TrieNode;

	TrieNode *trienode_initialize(char c, int end, int height);
	//Creates trie node NULL sibling, child and members .c and .end set and returns it
	//Return NULL and error message if out of memory

	TrieNode *getSibling(TrieNode *t);
	//Returns trie node sibling

	TrieNode *getChild(TrieNode *t);
	//Returns trie node child

	TrieNode *trienode_search(TrieNode *t, char c);
	//Searches trie node and its siblings for trie node with matching c and returns it
	//Return NULL if not found

typedef struct {
	int max_length;
	TrieNode *root;
} Trie;

	Trie *trie_initialize(void);
	//Creates trie with default root trie node and returns it
	//Return NULL and error message if out of memory

	int trie_insert(Trie *T, char *c);
	//Inserts String into trie, creating new trie nodes and setting child and sibling if necessary
	//Returns 1 if insert successful

	char_arr2D *trie_search(Trie *T, char *c);
	//Searches trie for string with matching starting characters and returns all matches as 2D dynamic char array

typedef struct {
	int count;
	int MAX_SIZE;
	TrieNode **item;
} Stack;
//stack structure used by trie_search(...)

	Stack *stack_initialize(int MAX_SIZE);
	//Creates stack that can store at most MAX_SIZE elements
	//Return NULL and error message if out of memory

	TrieNode *pop(Stack *S);
	//Pop element from stack if it is not empty

	void push(Stack *S, TrieNode *t);
	//Push element to stack if it is not full

	int isEmpty(Stack *S);
	//Return 1 if stack is empty

	void stack_free(Stack *S);
	//free memory used by this structure

typedef struct {
	char **c;
	int size;
} char_arr2D;
//2D dynamic char array that keeps track of number of elements added

	char_arr2D *char_arr2D_initialize();
	//Creates 2D dynamic character array and returns it
	//Return NULL and error message if out of memory

	void char_arr2D_strcpy(char_arr2D *C, char *c);
	//Allocates space in 2D char array and adds string

	int char_arr2D_size(char_arr2D* C);
	//Returns size of array

	void char_arr2D_free(char_arr2D *C);
	//free memory used by this structure
