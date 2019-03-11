#include "isogram.h"

bool is_isogram(const char phrase[]){
  int i = 0;
  // we can stop on the last character that is part of the actual string and not
  // the null terminator. This is because there is no where left in the string
  // for the last character in the string to be repeated.
  if (phrase == NULL){
    return false;
  }
  if (phrase[0] == '\0'){
    return true;
  }
  while (phrase[i + 1] != '\0') {
    if(isalpha(phrase[i])){
      int j = i + 1;
      while(phrase[j] != '\0'){
        if(tolower(phrase[i]) == tolower(phrase[j])){
          return false;
        }
        j++;
      }
    }
    i++;
  }
  return true;
}
