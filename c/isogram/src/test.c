#include <stdbool.h>
#include <stdio.h>

int main(int argc, const char* argv[]){
  bool a = true;
  bool b = false;
  bool c = true;
  bool d = false;
  bool e = a + b;
  bool f = b + d;
  bool g = b + d + c;

  printf("%d\n",a);
  printf("%d\n",e);
  printf("%d\n",f);
  printf("%d\n",g);
}

