#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int GetUserInput() {
   int num;
   printf("\nEnter your guess (1(Rock)/2(Paper)/3(Scissors)): ");
   if(!(scanf(" %d", &num))) {
      printf("Invalid Input");
      exit(EXIT_FAILURE);
   }
   return num;
}

int CompGuess() {
   int r = rand() % 3;
   return r;
}

void CompareNums(int guess, int c_guess) {
   // 0 = Rock
   // 1 = Paper
   // 2 = Scissors

   if (guess == c_guess) {
      printf("Tie");
   } else {
      if (guess == 0) {
         if (c_guess == 1) {
            printf("You said Rock, the Computer said Paper \nYou Lost");
                           
         } else {
            printf("You said Rock, the Computer said Scissors \n You Win!");               
         }
            
      } else if (guess == 1) {
         if (c_guess == 0) {
            printf("You said Paper, the Computer said Rock \nYou Win!");               
         } else {
            printf("You said Paper, the Computer said Scissors \nYou Lost");               
         }
            
      } else {
         if (c_guess == 0) {
            printf("You said Scissors, the Computer said Rock \n You Lost");               
         } else {
            printf("You said Scissors, the Computer said Paper \n You Won!");               
         }
            
      }
   }
}

int main() {
   srand(time(NULL));
   while (1) {
       int guess = GetUserInput();
       // Get Computer guess
       int c_guess = CompGuess();
       // Compare results
       CompareNums(guess, c_guess);
       // Ask to play again
       printf("\nDo you want to play again (y/n): ");
       char g;
       if (!(scanf("%s", &g))) {
         exit(EXIT_FAILURE);
       }

       if (g == 'n') {
         break;
       } else if (g == 'y') {

       } else {
          printf("Invalid Input \n");
       }
   }
   return 0;
}
