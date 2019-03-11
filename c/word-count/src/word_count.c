#include "word_count.h"

int word_count(const char* input_text, word_count_word_t* words){
  unsigned uniqueWords = 1;
  for(unsigned i = 0; i < strlen(input_text); i++){
  // for(unsigned i = 0; i < sizeof(input_text)/sizeof(input_text[0]); i++){
    if(input_text[i] == ' '){
      uniqueWords++;
    }
    else {
      char currentWord[MAX_WORD_LENGTH];
      unsigned j = 0;
      do {
        currentWord[j] = input_text[i];
        j++;
        i++;
      } while (input_text[i] != ' ');
      currentWord[j] = '\0';

      bool wordNotInDict = true;
      for(unsigned i = 0; i < MAX_WORDS; i ++){
        if(strcmp(currentWord, words[i].text)){
          wordNotInDict = false;
          words[i].count++;
        }
      }
      // if word does not exist
      if (wordNotInDict){
        strcpy(words[uniqueWords - 1].text, currentWord);
        words[uniqueWords - 1].count = 1;
      }
    }
  }

  // just to make tests fail
  // unsigned x = strlen(input_text);
  // x *= uniqueWords;
  // words[0].text[0] = '1';
  // words[0].text[1] = '\0';
  // words[0].count = 1;
  return uniqueWords;
}
