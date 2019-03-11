#include "acronym.h"

// taken from the FreeBSD source code
// http://fxr.watson.org/fxr/source/libkern/strlen.c?v=DFBSD<Paste>
// unsigned strlen(const char *str)
// {
//     const char *s;
//     for (s = str; *s; ++s);
//     return(s - str);
// }

char* abbreviate(const char * phrase){
  if(phrase == NULL || phrase[0] == '\0'){
    return NULL;
  }
	size_t phrase_len = strlen(phrase);
	char* result = malloc(1000);
	result[0] = toupper(phrase[0]);
  unsigned next_in_result = 1;
	bool next_char_part_of_acronym = false;
	for(size_t i = 1; i < phrase_len; i++){
    if (next_char_part_of_acronym){
      result[next_in_result] = toupper(phrase[i]);
      next_char_part_of_acronym = false;
      next_in_result++;
    }
		else if (phrase[i] == ' ' || phrase[i] == '-'){
      next_char_part_of_acronym = true;
		}
	}
	return result;
}

