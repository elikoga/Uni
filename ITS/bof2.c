#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PASSWORDLENGTH 32

void printTask() {
   printf("#########################################################\n");
   printf("#                                                       #\n");
   printf("#                      WELCOME                          #\n");
   printf("#                                                       #\n");
   printf("#    Your goal is to login into the 'admin' account     #\n");
   printf("#    We only use super secure functions like strcmp     #\n");
   printf("#    https://cplusplus.com/reference/cstring/strcmp     #\n");
   printf("#                                                       #\n");
   printf("#                                                       #\n");
   printf("#########################################################\n\n");
}

int main() {
   setbuf(stdout, NULL);  // ignore this line
   printTask();

   char admin_password[32];
   char user_password[32];
   char user_name[16];

   // generate random password
   for (int i=0; i<31; i++) {
      admin_password[i] = 'A' + random() % 26;
   }
   admin_password[31] = (char)0; // (char)0 is equal to use '\0'

   printf("Provide your username: ");
   scanf("%s", user_name);

   printf("Provide your password: ");
   scanf("%s", user_password);

   if (strcmp(user_name, "admin") == 0) {
      if (strcmp(user_password, admin_password) == 0) {
         // YOU WIN
         printf("Good job, you win.\n");
      } else {
         // YOU LOOSE
         printf("Nah, computer says NO. WRONG PASSWORD.\n");
      }
   } else {
      // YOU LOOSE
      printf(
          "Your goal is to log into the >> admin << account.\n username = "
          "admin\n");
   }
}
