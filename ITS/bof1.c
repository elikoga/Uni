#include <stdio.h>

void printTask() {
   printf("#########################################################\n");
   printf("#                                                       #\n");
   printf("#                      WELCOME                          #\n");
   printf("#                                                       #\n");
   printf("#         Your goal is to call the win function         #\n");
   printf("#                                                       #\n");
   printf("#                                                       #\n");
   printf("#########################################################\n\n");
}

void win() { printf("Good job, you win.\n"); }

int main() {
   setbuf(stdout, NULL);  // ignore this line
   printTask();

   char password = 'A';
   char buffer[4];

   printf("Provide your input: ");
   scanf("%s", buffer);
   printf("%c\n", password);

   if (password == 'B') {
      // YOU WIN
      win();
   } else {
      // YOU LOOSE
   }
}
